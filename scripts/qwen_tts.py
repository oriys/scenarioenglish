#!/usr/bin/env python3
"""Qwen3-TTS pipeline for Scenario English on macOS / Apple Silicon.

Workflow:
1. Generate several VoiceDesign candidates for a fixed UK role.
2. Listen and select one candidate as the role reference WAV.
3. Use Qwen3-TTS 1.7B Base through MLX-Audio to voice-clone that
   reference for all course lines.

Examples:
  python scripts/qwen_tts.py doctor
  python scripts/qwen_tts.py design-reference --profile uk_airport_f_01 --candidates 6
  python scripts/qwen_tts.py batch --manifest tts/manifest.example.json
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import soundfile as sf
from mlx_audio.tts.utils import load_model

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILES = ROOT / "tts" / "voice_profiles.json"

# Quality-first defaults. On lower-memory Macs these can be overridden with the
# corresponding mlx-community 8-bit model via --model.
DESIGN_MODEL = "mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16"
BASE_MODEL = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16"
DESIGN_MODEL_8BIT = "mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit"
BASE_MODEL_8BIT = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_platform() -> tuple[bool, str]:
    system = platform.system()
    machine = platform.machine().lower()
    ok = system == "Darwin" and machine in {"arm64", "aarch64"}
    return ok, f"{system} {machine}"


def require_apple_silicon() -> None:
    ok, description = check_platform()
    if not ok:
        raise SystemExit(
            "This TTS pipeline is configured for macOS on Apple Silicon (M1 or newer). "
            f"Detected: {description}."
        )


def get_profile(path: Path, profile_id: str) -> tuple[str, dict[str, Any]]:
    data = load_json(path)
    profiles = data.get("profiles", {})
    if profile_id not in profiles:
        available = ", ".join(sorted(profiles))
        raise SystemExit(f"Unknown profile '{profile_id}'. Available: {available}")
    ref_text = data["reference_text"]
    return ref_text, profiles[profile_id]


def collect_audio(results: Iterable[Any], fallback_sample_rate: int) -> tuple[np.ndarray, int]:
    chunks: list[np.ndarray] = []
    sample_rate = fallback_sample_rate

    for result in results:
        audio = np.asarray(result.audio, dtype=np.float32).reshape(-1)
        if audio.size:
            chunks.append(audio)
        result_sr = getattr(result, "sample_rate", None)
        if result_sr:
            sample_rate = int(result_sr)

    if not chunks:
        raise RuntimeError("Qwen3-TTS returned no audio samples.")

    if len(chunks) == 1:
        return chunks[0], sample_rate
    return np.concatenate(chunks), sample_rate


def save_results(results: Iterable[Any], model: Any, output: Path) -> None:
    audio, sample_rate = collect_audio(results, int(model.sample_rate))
    output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(output, audio, sample_rate, subtype="PCM_16")


def load_mlx_model(model_id: str) -> Any:
    require_apple_silicon()
    print(f"Loading MLX model: {model_id}")
    print("The first run may download model weights from Hugging Face.")
    return load_model(model_id)


def cmd_doctor(_: argparse.Namespace) -> None:
    ok, description = check_platform()
    print(f"Platform: {description}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Apple Silicon: {'yes' if ok else 'no'}")

    try:
        import mlx  # noqa: F401

        print("MLX: installed")
    except Exception as exc:
        print(f"MLX: unavailable ({exc})")

    try:
        import mlx_audio  # noqa: F401

        print("MLX-Audio: installed")
    except Exception as exc:
        print(f"MLX-Audio: unavailable ({exc})")

    print(f"Quality VoiceDesign model: {DESIGN_MODEL}")
    print(f"Quality Base model:        {BASE_MODEL}")
    print(f"Low-memory VoiceDesign:    {DESIGN_MODEL_8BIT}")
    print(f"Low-memory Base:           {BASE_MODEL_8BIT}")

    if not ok:
        raise SystemExit(1)


def cmd_design_reference(args: argparse.Namespace) -> None:
    profile_path = Path(args.profiles)
    ref_text, profile = get_profile(profile_path, args.profile)
    model = load_mlx_model(args.model)

    out_dir = Path(args.output_dir) / args.profile
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Profile: {args.profile} ({profile.get('role', 'unknown role')})")
    print(f"Instruction: {profile['description']}")
    print(f"Reference transcript: {ref_text}")

    for i in range(1, args.candidates + 1):
        results = model.generate_voice_design(
            text=ref_text,
            language="English",
            instruct=profile["description"],
        )
        out = out_dir / f"candidate-{i:02d}.wav"
        save_results(results, model, out)
        print(f"Wrote {out}")

    transcript_path = out_dir / "reference.txt"
    transcript_path.write_text(ref_text + "\n", encoding="utf-8")
    print("\nListen blindly and select the best candidate.")
    print(
        f"Copy the selected WAV to tts/references/{args.profile}.wav; "
        "keep reference.txt unchanged because clone quality depends on the exact transcript."
    )


def generate_clone(
    model: Any,
    reference: Path,
    reference_text: str,
    text: str,
    language: str,
    output: Path,
) -> None:
    # MLX-Audio's Qwen3-TTS Base model accepts reference audio + transcript
    # directly. Its implementation caches ICL/reference work internally.
    results = model.generate(
        text=text,
        language=language,
        ref_audio=str(reference),
        ref_text=reference_text,
    )
    save_results(results, model, output)


def cmd_synthesize(args: argparse.Namespace) -> None:
    profile_path = Path(args.profiles)
    ref_text, _ = get_profile(profile_path, args.profile)
    reference = Path(args.reference)
    if not reference.exists():
        raise SystemExit(f"Reference WAV not found: {reference}")

    model = load_mlx_model(args.model)
    output = Path(args.output)
    generate_clone(model, reference, ref_text, args.text, args.language, output)
    print(f"Wrote {output}")


def cmd_batch(args: argparse.Namespace) -> None:
    manifest_path = Path(args.manifest)
    manifest = load_json(manifest_path)
    profile_id = args.profile or manifest.get("voice")
    if not profile_id:
        raise SystemExit("Manifest must define 'voice' or --profile must be supplied.")

    profile_path = Path(args.profiles)
    ref_text, profile = get_profile(profile_path, profile_id)
    reference = Path(args.reference or ROOT / "tts" / "references" / f"{profile_id}.wav")
    if not reference.exists():
        raise SystemExit(
            f"Reference WAV not found: {reference}\n"
            f"First run: python scripts/qwen_tts.py design-reference --profile {profile_id}"
        )

    lines = manifest.get("lines", [])
    if not lines:
        raise SystemExit("Manifest has no lines.")

    model = load_mlx_model(args.model)
    print(f"Voice: {profile_id} ({profile.get('role', 'unknown role')})")

    language = manifest.get("language", "English")
    for index, line in enumerate(lines, start=1):
        text = line["text"].strip()
        output = ROOT / line["output"]
        if output.exists() and not args.overwrite:
            print(f"[{index}/{len(lines)}] skip existing {output}")
            continue
        print(f"[{index}/{len(lines)}] {line.get('id', output.stem)}: {text}")
        generate_clone(model, reference, ref_text, text, language, output)
        print(f"    -> {output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scenario English Qwen3-TTS pipeline for macOS / Apple Silicon"
    )
    parser.add_argument("--profiles", default=str(DEFAULT_PROFILES))

    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser("doctor", help="Check the local Apple Silicon / MLX environment")
    doctor.set_defaults(func=cmd_doctor)

    design = sub.add_parser("design-reference", help="Generate candidate role reference voices")
    design.add_argument("--profile", required=True)
    design.add_argument("--candidates", type=int, default=6)
    design.add_argument(
        "--model",
        default=DESIGN_MODEL,
        help=f"MLX VoiceDesign model (low-memory option: {DESIGN_MODEL_8BIT})",
    )
    design.add_argument("--output-dir", default=str(ROOT / "tts" / "candidates"))
    design.set_defaults(func=cmd_design_reference)

    synth = sub.add_parser("synthesize", help="Generate one line from a selected role reference")
    synth.add_argument("--profile", required=True)
    synth.add_argument("--reference", required=True)
    synth.add_argument("--text", required=True)
    synth.add_argument("--language", default="English")
    synth.add_argument("--output", required=True)
    synth.add_argument(
        "--model",
        default=BASE_MODEL,
        help=f"MLX Base model (low-memory option: {BASE_MODEL_8BIT})",
    )
    synth.set_defaults(func=cmd_synthesize)

    batch = sub.add_parser("batch", help="Generate all lines in an audio manifest")
    batch.add_argument("--manifest", required=True)
    batch.add_argument("--profile", help="Override manifest voice profile")
    batch.add_argument("--reference", help="Override role reference WAV")
    batch.add_argument(
        "--model",
        default=BASE_MODEL,
        help=f"MLX Base model (low-memory option: {BASE_MODEL_8BIT})",
    )
    batch.add_argument("--overwrite", action="store_true")
    batch.set_defaults(func=cmd_batch)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
