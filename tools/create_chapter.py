#!/usr/bin/env python3
"""Tworzy plik rozdziału i katalogi na jego materiały."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CHAPTER_NAME_PATTERN = re.compile(r"^[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_DIRS = (
    "figures",
    "figures/source",
    "data",
    "code",
    "scripts",
    "tables",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Utwórz plik chapters/NN-nazwa.tex oraz katalogi figures, data, "
            "code, scripts i tables."
        )
    )
    parser.add_argument(
        "name",
        help="nazwa w formacie NN-nazwa-rozdzialu, np. 07-wyniki-badan",
    )
    parser.add_argument("--title-pl", help="polski tytuł rozdziału")
    parser.add_argument("--title-en", help="angielski tytuł rozdziału")
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="katalog projektu; domyślnie ustalany automatycznie",
    )
    return parser.parse_args()


def default_title(name: str) -> str:
    return name.split("-", 1)[1].replace("-", " ").capitalize()


def main() -> int:
    args = parse_args()
    if not CHAPTER_NAME_PATTERN.fullmatch(args.name):
        print(
            "Błąd: nazwa musi mieć format NN-nazwa-rozdzialu i zawierać "
            "wyłącznie małe litery ASCII, cyfry oraz łączniki.",
            file=sys.stderr,
        )
        return 2

    project_root = args.project_root.resolve()
    chapters_dir = project_root / "chapters"
    if not chapters_dir.is_dir():
        print(f"Błąd: nie znaleziono katalogu rozdziałów: {chapters_dir}", file=sys.stderr)
        return 2

    chapter_file = chapters_dir / f"{args.name}.tex"
    resource_root = chapters_dir / args.name
    title_pl = args.title_pl or default_title(args.name)
    title_en = args.title_en or default_title(args.name)

    created: list[Path] = []
    if not chapter_file.exists():
        chapter_file.write_text(
            f"\\chapter{{\\ploren{{{title_pl}}}{{{title_en}}}}}\n\n"
            "% Treść rozdziału.\n",
            encoding="utf-8",
        )
        created.append(chapter_file)

    for relative_dir in RESOURCE_DIRS:
        directory = resource_root / relative_dir
        if not directory.exists():
            directory.mkdir(parents=True)
            created.append(directory)
        (directory / ".gitkeep").touch(exist_ok=True)

    if created:
        print("Utworzono:")
        for path in created:
            print(f"  {path.relative_to(project_root)}")
    else:
        print("Struktura już istnieje; nie nadpisano żadnych plików.")

    print("\nDodaj w odpowiednim miejscu pliku main.tex:")
    print(f"\\include{{chapters/{args.name}}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
