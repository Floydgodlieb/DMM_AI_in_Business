#!/usr/bin/env python3
"""Locally transcribe an interview recording. (Translation is NOT done here — see below.)

Despite the filename (kept to match docs/build_plan.md and CLAUDE.md's scripts list),
this script only transcribes — it never translates and never calls any network
AI service. Transcription runs entirely on this laptop via faster-whisper, and
the output goes straight into 03_data/private/, same as the audio it came from.

Why translation isn't in this script: the consent/privacy chain this pipeline
follows is transcribe (local) -> anonymize.py (local, no AI) -> translate
(via Claude, on the ANONYMIZED transcript only). Translating here, before
anonymization, would mean sending raw interview content to an AI service —
exactly what the course's hard rule and 03_data/consent_checklist.md forbid.
Once 03_data/anonymized/<name>.txt exists, translate it by pasting it into
Claude (or having stage 3 / data-intake do so) — there is no script for that
step, deliberately, since it is judgment-assisted, not a deterministic
transformation.

Refuses to run unless 03_data/consent_checklist.md has every checkbox ticked
("- [x]") — this operationalizes the rule that nothing touches interview
material before consent is fully settled.

Requires faster-whisper (pip install faster-whisper). The first run for a
given --model downloads that model's weights from Hugging Face once (a
public model file, not your audio) and caches it; every run after that is
fully offline.

MANUAL FALLBACK: transcribe by ear, listening to the recording and typing
what you hear directly into 03_data/private/<name>_transcript.txt — still
locally, no cloud dictation tool. Everything after that (anonymize, then
translate the anonymized text) is unchanged.

Usage:
    python transcribe_translate.py --audio 03_data/private/interview.wav
    python transcribe_translate.py --audio 03_data/private/interview.wav --model small --language nl
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from faster_whisper import WhisperModel
except ImportError:
    WhisperModel = None

ROOT = Path(__file__).resolve().parent.parent
PRIVATE_DIR = ROOT / "03_data" / "private"
CONSENT_CHECKLIST = ROOT / "03_data" / "consent_checklist.md"


def consent_is_complete() -> tuple[bool, int, int]:
    if not CONSENT_CHECKLIST.exists():
        return False, 0, 0
    text = CONSENT_CHECKLIST.read_text(encoding="utf-8-sig")
    boxes = re.findall(r"- \[([ xX])\]", text)
    checked = sum(1 for b in boxes if b.lower() == "x")
    return checked == len(boxes) and len(boxes) > 0, checked, len(boxes)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--audio", required=True, help="Path to the recording (wav/mp3/m4a/...)")
    parser.add_argument("--model", default="small", help="faster-whisper model size (default: small)")
    parser.add_argument("--language", default=None, help="Force a language code, e.g. nl (default: auto-detect)")
    parser.add_argument(
        "--i-know-this-only-transcribes",
        action="store_true",
        help="Acknowledge that this script does not translate (see header). Required to run.",
    )
    args = parser.parse_args()

    if not args.i_know_this_only_transcribes:
        parser.error(
            "this script only transcribes, it never translates — pass "
            "--i-know-this-only-transcribes to confirm you've read why (see the script header)"
        )

    ok, checked, total = consent_is_complete()
    if not ok:
        sys.exit(
            f"Refusing to run: {CONSENT_CHECKLIST} has {checked}/{total} boxes checked. "
            "Every item must be checked and signed off before any interview material is processed."
        )

    if WhisperModel is None:
        sys.exit("faster-whisper is not installed (pip install faster-whisper). See the manual fallback in this script's header.")

    audio_path = Path(args.audio)
    if not audio_path.exists():
        sys.exit(f"{audio_path} not found.")
    try:
        audio_path.relative_to(PRIVATE_DIR)
    except ValueError:
        sys.exit(f"{audio_path} is not under {PRIVATE_DIR} — interview audio must stay in 03_data/private/.")

    print(f"Loading faster-whisper model '{args.model}' (downloads once, then cached locally)...")
    model = WhisperModel(args.model, device="cpu", compute_type="int8")

    print(f"Transcribing {audio_path.name} locally...")
    segments, info = model.transcribe(str(audio_path), language=args.language)

    lines = []
    for seg in segments:
        lines.append(f"[{seg.start:7.2f}-{seg.end:7.2f}] {seg.text.strip()}")

    out_path = PRIVATE_DIR / f"{audio_path.stem}_transcript.txt"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Detected language: {info.language} (p={info.language_probability:.2f})")
    print(f"Wrote {out_path} ({len(lines)} segment(s)).")
    print(
        "Next: run anonymize.py on this file, THEN translate the anonymized "
        "output — never this raw transcript."
    )


if __name__ == "__main__":
    main()
