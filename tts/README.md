# Scenario English — Local TTS on macOS

The course uses **Qwen3-TTS 1.7B through MLX-Audio** as the primary local speech engine.

The target environment is **macOS on Apple Silicon (M1 or newer)**. CUDA, PyTorch and FlashAttention are no longer required for the local course pipeline.

The design goal is not merely good-sounding TTS. It is to keep a small cast of believable British service workers consistent across hundreds of listening drills.

## Architecture

```text
Voice profile
    ↓
Qwen3-TTS-12Hz-1.7B-VoiceDesign (MLX)
    ↓
Generate 4–8 candidate reference clips
    ↓
Human blind selection
    ↓
Selected reference WAV
    ↓
Qwen3-TTS-12Hz-1.7B-Base voice clone (MLX)
    ↓
All Scene listening lines for that role
```

VoiceDesign is used only to create candidates. Once a role is approved, normal course generation uses the Base model with the selected reference audio. This gives much better speaker consistency than redesigning the voice for every line.

## Models

Quality-first defaults:

- Voice creation: `mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16`
- Production generation: `mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16`

Lower-memory alternatives:

- Voice creation: `mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit`
- Production generation: `mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit`

For this project, use **BF16 first** because final listening quality is the primary requirement. Switch to 8-bit only if memory pressure becomes a practical problem.

## Requirements

- macOS 14+ recommended
- Apple Silicon: M1 / M2 / M3 / M4 or newer
- Python 3.11+ recommended
- 16 GB unified memory recommended for the 1.7B models
- `ffmpeg` for later audio processing/export stages

MLX-Audio is optimized for Apple Silicon and currently supports Qwen3-TTS Base voice cloning and VoiceDesign directly.

## Installation

Recommended setup with `uv`:

```bash
brew install python@3.11 uv ffmpeg

uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r tts/requirements.txt
```

`pip` also works:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tts/requirements.txt
```

No CUDA toolkit, PyTorch CUDA wheel, or FlashAttention installation is needed.

Models are downloaded from Hugging Face on first use and cached locally.

## Check the environment

Run:

```bash
python scripts/qwen_tts.py doctor
```

You should see:

```text
Apple Silicon: yes
MLX: installed
MLX-Audio: installed
```

If you are on an Intel Mac, this pipeline is not supported as the primary local path.

## 1. Create voice candidates

The canonical UK roles are defined in `tts/voice_profiles.json`.

Example:

```bash
python scripts/qwen_tts.py design-reference \
  --profile uk_airport_f_01 \
  --candidates 6
```

The first run downloads the 1.7B VoiceDesign model.

Outputs:

```text
tts/candidates/uk_airport_f_01/
├── candidate-01.wav
├── candidate-02.wav
├── ...
└── reference.txt
```

Do not choose a voice from one clip alone. Generate several candidates and compare them blindly.

Selection criteria, in order:

1. pronunciation and word accuracy;
2. believable British accent;
3. natural rhythm, reductions and pauses;
4. correct professional role/personality;
5. no synthetic artefacts;
6. pleasant timbre.

The course should prefer **realistic public-facing speech** over an attractive announcer voice.

After selection:

```bash
mkdir -p tts/references
cp tts/candidates/uk_airport_f_01/candidate-03.wav \
   tts/references/uk_airport_f_01.wav
```

Keep the exact `reference_text` in `voice_profiles.json`. Qwen's ICL voice-clone path uses both the reference audio and its transcript.

## 2. Test one production line

```bash
python scripts/qwen_tts.py synthesize \
  --profile uk_airport_f_01 \
  --reference tts/references/uk_airport_f_01.wav \
  --text "Are you checking in any bags today?" \
  --output /tmp/check-in.wav
```

This uses the **1.7B Base BF16 MLX model**, not VoiceDesign.

## 3. Generate a Scene from a manifest

Copy and edit the example:

```bash
cp tts/manifest.example.json tts/001-counter-check-in.json
```

Then:

```bash
python scripts/qwen_tts.py batch \
  --manifest tts/001-counter-check-in.json
```

The manifest controls:

- stable audio ID;
- Listening level (`L1`–`L4`);
- intent;
- exact spoken text;
- output path;
- role voice.

Existing output files are skipped by default. Use `--overwrite` only when intentionally regenerating them.

## Lower-memory mode

If BF16 causes memory pressure, override the model without changing the pipeline.

Voice design:

```bash
python scripts/qwen_tts.py design-reference \
  --profile uk_airport_f_01 \
  --candidates 6 \
  --model mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit
```

Production voice cloning:

```bash
python scripts/qwen_tts.py batch \
  --manifest tts/001-counter-check-in.json \
  --model mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit
```

Do not default to the 0.6B model merely for speed. The course is quality-first.

## Voice cast

The initial profiles include:

- `uk_airport_f_01` — airport ground staff, neutral Southern British;
- `uk_airport_m_01` — airport security officer;
- `uk_rail_f_01` — light Northern English;
- `uk_rail_m_01` — light London / Estuary;
- `uk_hotel_f_01` — London hotel receptionist;
- `uk_restaurant_m_01` — London restaurant server;
- `uk_pharmacy_f_01` — calm neutral British pharmacist;
- `uk_scotland_m_01` — light, visitor-friendly Scottish accent.

Do not add a new speaker just because a new Scene starts. Reuse the cast so learners repeatedly encounter familiar and unfamiliar accents across different contexts.

## Quality policy

### L1 — Canonical

Use the clearest approved role voice at a natural, moderate pace. Do not artificially slow words down.

### L2 — Natural variants

Keep the same voice but vary sentence construction and use realistic contractions/reductions.

### L3 — Critical information

Prioritise accurate pronunciation of numbers, times, prices, gates, platforms, room numbers and postcodes. Every generated L3 asset should be manually spot-checked before release.

### L4 — Pressure

Do **not** ask TTS to simulate station noise or phone distortion. Generate a clean voice first, then add controlled ambience/EQ/codec effects in a separate audio-processing stage. This keeps speech generation reproducible and prevents pronunciation quality from being mixed with noise generation.

## Reproducibility

VoiceDesign is stochastic. The selected reference WAV is therefore the identity of a course role.

For released audio:

- never silently replace a role reference;
- version a role if its reference changes (`uk_airport_f_02`);
- store the exact text used to synthesize every asset in the manifest;
- regenerate an asset only deliberately;
- manually review P0 and L3/L4 assets before publishing.

## Current limitation

The scripts create clean WAV assets. Noise mixing, loudness normalization, Opus export, automatic pronunciation QA and Scene-to-manifest extraction should remain separate build stages rather than being hidden inside TTS generation.
