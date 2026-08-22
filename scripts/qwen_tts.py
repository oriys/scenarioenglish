#!/usr/bin/env python3
"""Local Qwen3-TTS pipeline for Scenario English.

Workflow:
1. Generate several VoiceDesign candidates for a fixed UK role.
2. Listen and select one candidate as the role reference WAV.
3. Use Qwen3-TTS 1.7B Base to voice-clone that reference for all course lines.

Examples:
  python scripts/qwen_tts.py design-reference --profile uk_airport_f_01 --candidates 4
  python scripts/qwen_tts.py batch --manifest tts/manifest.example.json \
      --reference tts/references/uk_airport_f_01.wav
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILES = ROOT / "tts" / "voice_profiles.json"
DESIGN_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
BASE_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"

DEFAULT_GEN_KWARGS = {
    "max_new_tokens": 2048,
    "do_sample": True,
    "top_k": 50,
    "top_p": 1.0,
    "temperature": 0.9,
    "repetition_penalty": 1.05,
    "subtalker_dosample": True,
    "subtalker_top_k": 50,
    "subtalker_top_p": 1.0,
    "subtalker_temperature": 0.9,
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def choose_device(requested: str) -> str:
    if requested != "auto":
        return requested
    if torch.cuda.is_available():
        return "cuda:0"
    # Qwen3-TTS currently has the most predictable local path on CUDA.
    # CPU fallback is intentionally supported for correctness, not speed.
    return "cpu"


def load_model(model_id: str, device: str, no_flash_attn: bool) -> Qwen3TTSModel:
    kwargs: dict[str, Any] = {"device_map": device}

    if device.startswith("cuda"):
        kwargs["dtype"] = torch.bfloat16
        if not no_flash_attn:
            kwargs["attn_implementation"] = "flash_attention_2"
    else:
        kwargs["dtype"] = torch.float32

    try:
        return Qwen3TTSModel.from_pretrained(model_id, **kwargs)
    except Exception as exc:
        if device.startswith("cuda") and not no_flash_attn:
            print(
                "FlashAttention model load failed; retrying without flash_attention_2. "
                f"Original error: {exc}",
                file=sys.stderr,
            )
            kwargs.pop("attn_implementation", None)
            return Qwen3TTSModel.from_pretrained(model_id, **kwargs)
        raise


def get_profile(path: Path, profile_id: str) -> tuple[str, dict[str, Any]]:
    data = load_json(path)
    profiles = data.get("profiles", {})
    if profile_id not in profiles:
        available = ", ".join(sorted(profiles))
        raise SystemExit(f"Unknown profile '{profile_id}'. Available: {available}")
    ref_text = data["reference_text"]
    return ref_text, profiles[profile_id]


def cmd_design_reference(args: argparse.Namespace) -> None:
    profile_path = Path(args.profiles)
    ref_text, profile = get_profile(profile_path, args.profile)
    device = choose_device(args.device)

    print(f"Loading VoiceDesign model on {device}...")
    model = load_model(args.model, device, args.no_flash_attn)

    out_dir = Path(args.output_dir) / args.profile
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Profile: {args.profile} ({profile.get('role', 'unknown role')})")
    print(f"Instruction: {profile['description']}")
    print(f"Reference transcript: {ref_text}")

    for i in range(1, args.candidates + 1):
        wavs, sr = model.generate_voice_design(
            text=ref_text,
            language="English",
            instruct=profile["description"],
            **DEFAULT_GEN_KWARGS,
        )
        out = out_dir / f"candidate-{i:02d}.wav"
        sf.write(out, wavs[0], sr)
        print(f"Wrote {out}")

    transcript_path = out_dir / "reference.txt"
    transcript_path.write_text(ref_text + "\n", encoding="utf-8")
    print("\nListen blindly and select the best candidate.")
    print(
        f"Copy the selected WAV to tts/references/{args.profile}.wav; "
        "keep reference.txt unchanged because clone quality depends on the exact transcript."
    )


def create_clone_prompt(
    model: Qwen3TTSModel,
    reference: Path,
    reference_text: str,
):
    return model.create_voice_clone_prompt(
        ref_audio=str(reference),
        ref_text=reference_text,
        x_vector_only_mode=False,
    )


def generate_one(
    model: Qwen3TTSModel,
    prompt,
    text: str,
    language: str,
    output: Path,
) -> None:
    wavs, sr = model.generate_voice_clone(
        text=text,
        language=language,
        voice_clone_prompt=prompt,
        **DEFAULT_GEN_KWARGS,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(output, wavs[0], sr)


def cmd_synthesize(args: argparse.Namespace) -> None:
    profile_path = Path(args.profiles)
    ref_text, _ = get_profile(profile_path, args.profile)
    reference = Path(args.reference)
    if not reference.exists():
        raise SystemExit(f"Reference WAV not found: {reference}")

    device = choose_device(args.device)
    print(f"Loading Base voice-clone model on {device}...")
    model = load_model(args.model, device, args.no_flash_attn)
    prompt = create_clone_prompt(model, reference, ref_text)

    output = Path(args.output)
    generate_one(model, prompt, args.text, args.language, output)
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

    device = choose_device(args.device)
    print(f"Loading Base voice-clone model on {device}...")
    print(f"Voice: {profile_id} ({profile.get('role', 'unknown role')})")
    model = load_model(args.model, device, args.no_flash_attn)
    prompt = create_clone_prompt(model, reference, ref_text)

    language = manifest.get("language", "English")
    for index, line in enumerate(lines, start=1):
        text = line["text"].strip()
        output = ROOT / line["output"]
        if output.exists() and not args.overwrite:
            print(f"[{index}/{len(lines)}] skip existing {output}")
            continue
        print(f"[{index}/{len(lines)}] {line.get('id', output.stem)}: {text}")
        generate_one(model, prompt, text, language, output)
        print(f"    -> {output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scenario English Qwen3-TTS pipeline")
    parser.add_argument("--device", default="auto", help="auto, cuda:0, cpu, etc.")
    parser.add_argument(
        "--no-flash-attn",
        action="store_true",
        help="Do not request flash_attention_2 when loading CUDA models.",
    )
    parser.add_argument("--profiles", default=str(DEFAULT_PROFILES))

    sub = parser.add_subparsers(dest="command", required=True)

    design = sub.add_parser("design-reference", help="Generate candidate role reference voices")
    design.add_argument("--profile", required=True)
    design.add_argument("--candidates", type=int, default=4)
    design.add_argument("--model", default=DESIGN_MODEL)
    design.add_argument("--output-dir", default=str(ROOT / "tts" / "candidates"))
    design.set_defaults(func=cmd_design_reference)

    synth = sub.add_parser("synthesize", help="Generate one line from a selected role reference")
    synth.add_argument("--profile", required=True)
    synth.add_argument("--reference", required=True)
    synth.add_argument("--text", required=True)
    synth.add_argument("--language", default="English")
    synth.add_argument("--output", required=True)
    synth.add_argument("--model", default=BASE_MODEL)
    synth.set_defaults(func=cmd_synthesize)

    batch = sub.add_parser("batch", help="Generate all lines in an audio manifest")
    batch.add_argument("--manifest", required=True)
    batch.add_argument("--profile", help="Override manifest voice profile")
    batch.add_argument("--reference", help="Override role reference WAV")
    batch.add_argument("--model", default=BASE_MODEL)
    batch.add_argument("--overwrite", action="store_true")
    batch.set_defaults(func=cmd_batch)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
