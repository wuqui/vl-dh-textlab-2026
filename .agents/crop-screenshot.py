#!/usr/bin/env python3
"""Reproducible screenshot crop helper for slide assets.

Requires ImageMagick 7 (`magick`) on PATH.

Examples:
  python3 .agents/crop-screenshot.py info input.png
  python3 .agents/crop-screenshot.py contact input.png /tmp/contact.png --strip-height 900
  python3 .agents/crop-screenshot.py crop input.png output.png --x 60 --y 3150 --width 2760 --height 900 --spec crops.json --label collocation
  python3 .agents/crop-screenshot.py candidates input.png /tmp/candidates --x 60 --width 2760 --height 900 --ys 2500,2800,3100
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path


FONT_CANDIDATES = [
    Path("/System/Library/Fonts/SFNS.ttf"),
    Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
    Path("/System/Library/Fonts/Supplemental/Courier New.ttf"),
    Path("/Library/Fonts/Arial.ttf"),
]


@dataclass(frozen=True)
class CropSpec:
    source: str
    output: str
    x: int
    y: int
    width: int
    height: int
    label: str | None = None


def run_magick(args: list[str]) -> None:
    if not shutil.which("magick"):
        raise SystemExit("ImageMagick `magick` not found on PATH.")
    subprocess.run(["magick", *args], check=True)


def image_size(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["magick", "identify", "-format", "%w %h", str(path)],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    width, height = result.stdout.strip().split()
    return int(width), int(height)


def available_font() -> str | None:
    for font in FONT_CANDIDATES:
        if font.exists():
            return str(font)
    return None


def ensure_input(path: str) -> Path:
    image = Path(path)
    if not image.exists():
        raise SystemExit(f"Input image not found: {image}")
    return image


def append_spec(spec_path: Path, spec: CropSpec) -> None:
    existing: list[dict[str, object]]
    if spec_path.exists():
        existing = json.loads(spec_path.read_text())
        if not isinstance(existing, list):
            raise SystemExit(f"Spec file must contain a JSON list: {spec_path}")
    else:
        existing = []
    existing.append(asdict(spec))
    spec_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n")


def command_info(args: argparse.Namespace) -> None:
    image = ensure_input(args.image)
    width, height = image_size(image)
    print(json.dumps({"image": str(image), "width": width, "height": height}, indent=2))


def make_labeled_crop(
    source: Path,
    output: Path,
    geometry: str,
    label: str,
    resize_width: int | None,
) -> None:
    magick_args = [str(source), "-crop", geometry, "+repage"]
    if resize_width:
        magick_args.extend(["-resize", f"{resize_width}x"])
    magick_args.extend(["-background", "#0f172a", "-gravity", "northwest", "-splice", "0x40"])
    font = available_font()
    if font:
        magick_args.extend(["-font", font])
    magick_args.extend(["-fill", "white", "-pointsize", "24", "-annotate", "+12+28", label, str(output)])
    run_magick(magick_args)


def command_contact(args: argparse.Namespace) -> None:
    source = ensure_input(args.image)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = image_size(source)
    strip_height = args.strip_height
    y_values = list(range(0, height, strip_height - args.overlap))
    if y_values[-1] != max(0, height - strip_height):
        y_values.append(max(0, height - strip_height))
    y_values = sorted(set(y for y in y_values if y >= 0))

    with tempfile.TemporaryDirectory(prefix="crop-contact-") as tmp:
        parts: list[str] = []
        for index, y in enumerate(y_values):
            part = Path(tmp) / f"strip-{index:03d}.png"
            actual_height = min(strip_height, height - y)
            geometry = f"{width}x{actual_height}+0+{y}"
            label = f"{index:02d}  x=0 y={y} w={width} h={actual_height}"
            make_labeled_crop(source, part, geometry, label, args.resize_width)
            parts.append(str(part))
        run_magick([*parts, "-append", str(output)])

    print(json.dumps({"output": str(output), "strips": len(y_values)}, indent=2))


def crop_image(source: Path, output: Path, x: int, y: int, width: int, height: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run_magick([str(source), "-crop", f"{width}x{height}+{x}+{y}", "+repage", str(output)])


def command_crop(args: argparse.Namespace) -> None:
    source = ensure_input(args.image)
    output = Path(args.output)
    crop_image(source, output, args.x, args.y, args.width, args.height)
    spec = CropSpec(
        source=str(source),
        output=str(output),
        x=args.x,
        y=args.y,
        width=args.width,
        height=args.height,
        label=args.label,
    )
    if args.spec:
        append_spec(Path(args.spec), spec)
    print(json.dumps(asdict(spec), indent=2, ensure_ascii=False))


def parse_csv_ints(value: str) -> list[int]:
    try:
        return [int(item.strip()) for item in value.split(",") if item.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def command_candidates(args: argparse.Namespace) -> None:
    source = ensure_input(args.image)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    y_values = parse_csv_ints(args.ys)
    candidate_files: list[str] = []

    for y in y_values:
        candidate = out_dir / f"candidate-x{args.x}-y{y}-w{args.width}-h{args.height}.png"
        make_labeled_crop(
            source,
            candidate,
            f"{args.width}x{args.height}+{args.x}+{y}",
            f"x={args.x} y={y} w={args.width} h={args.height}",
            args.resize_width,
        )
        candidate_files.append(str(candidate))

    contact = out_dir / "candidates-contact.png"
    run_magick([*candidate_files, "-append", str(contact)])
    print(json.dumps({"contact": str(contact), "candidates": candidate_files}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    info = subparsers.add_parser("info", help="Print image dimensions.")
    info.add_argument("image")
    info.set_defaults(func=command_info)

    contact = subparsers.add_parser("contact", help="Create a labeled vertical strip contact sheet.")
    contact.add_argument("image")
    contact.add_argument("output")
    contact.add_argument("--strip-height", type=int, default=900)
    contact.add_argument("--overlap", type=int, default=0)
    contact.add_argument("--resize-width", type=int, default=720)
    contact.set_defaults(func=command_contact)

    crop = subparsers.add_parser("crop", help="Create one reproducible crop.")
    crop.add_argument("image")
    crop.add_argument("output")
    crop.add_argument("--x", type=int, required=True)
    crop.add_argument("--y", type=int, required=True)
    crop.add_argument("--width", type=int, required=True)
    crop.add_argument("--height", type=int, required=True)
    crop.add_argument("--label")
    crop.add_argument("--spec", help="Append crop geometry to a JSON spec file.")
    crop.set_defaults(func=command_crop)

    candidates = subparsers.add_parser("candidates", help="Create labeled candidate crops and a contact sheet.")
    candidates.add_argument("image")
    candidates.add_argument("output_dir")
    candidates.add_argument("--x", type=int, required=True)
    candidates.add_argument("--width", type=int, required=True)
    candidates.add_argument("--height", type=int, required=True)
    candidates.add_argument("--ys", required=True, help="Comma-separated y offsets, e.g. 1200,1500,1800")
    candidates.add_argument("--resize-width", type=int, default=720)
    candidates.set_defaults(func=command_candidates)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
