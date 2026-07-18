#!/usr/bin/env python3
"""Sprawdza metadane, pliki i pozostawione treści przykładowe szablonu."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULTS = {
    "authorname": "Imię i nazwisko",
    "albumid": "000000",
    "titlepl": "Tytuł pracy w języku polskim",
    "titleen": "Thesis title in English",
    "programmepl": "Nazwa kierunku",
    "programmeen": "Study programme",
    "supervisorname": "dr hab. inż. Imię Nazwisko, prof. uczelni",
    "keywordspl": "słowo kluczowe 1, słowo kluczowe 2, słowo kluczowe 3",
    "keywordsen": "keyword 1, keyword 2, keyword 3",
}

ALLOWED = {
    "thesislanguage": {"polish", "english"},
    "thesistype": {"engineering", "master", "doctoral"},
    "thesisprintmode": {"digital", "print"},
    "thesisstatus": {"draft", "final"},
}

BOOLEAN_OPTIONS = {
    "indentfirstparagraph",
    "showlistoffigures",
    "showlistoftables",
    "showlistoflistings",
    "showabbreviationlist",
    "showsymbollist",
    "showdedication",
    "showaideclaration",
    "showacknowledgements",
    "showfundingstatement",
    "showavailabilitystatement",
}

OPTIONAL_FILES = {
    "showdedication": "frontmatter/dedication.tex",
    "showaideclaration": "frontmatter/ai-declaration.tex",
    "showacknowledgements": "frontmatter/acknowledgements.tex",
    "showfundingstatement": "frontmatter/funding.tex",
    "showavailabilitystatement": "backmatter/availability.tex",
}

PLACEHOLDER_PATTERNS = (
    "Tutaj należy umieścić",
    "Provide a concise summary",
    "Ten tekst należy zastąpić",
    "Replace this text",
    "[nazwa instytucji finansującej]",
    "[funder name]",
    "[nazwa i wersja narzędzia]",
    "[tool name and version]",
    "[nazwa repozytorium]",
    "[repository name]",
    "% Treść rozdziału.",
)

COMMAND_RE = re.compile(r"\\newcommand\{\\([A-Za-z@]+)\}\{([^{}]*)\}")
INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^{}]+)\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="zwróć kod błędu, jeżeli znaleziono problemy",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="katalog projektu; domyślnie ustalany automatycznie",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    args = parse_args()
    root = args.project_root.resolve()
    metadata_path = root / "config" / "metadata.tex"
    problems: list[str] = []

    if not metadata_path.is_file():
        print(f"BŁĄD: nie znaleziono {metadata_path}", file=sys.stderr)
        return 2

    metadata = dict(COMMAND_RE.findall(read_text(metadata_path)))

    for field, default in DEFAULTS.items():
        if metadata.get(field) == default:
            problems.append(f"config/metadata.tex: pole {field} ma wartość przykładową")

    for field, allowed in ALLOWED.items():
        value = metadata.get(field)
        if value not in allowed:
            problems.append(
                f"config/metadata.tex: {field}={value!r}; dozwolone: {', '.join(sorted(allowed))}"
            )

    for field in sorted(BOOLEAN_OPTIONS):
        value = metadata.get(field)
        if value not in {"true", "false"}:
            problems.append(f"config/metadata.tex: {field} musi mieć wartość true albo false")

    logo = metadata.get("universitylogo")
    if not logo or not (root / logo).is_file():
        problems.append(f"nie znaleziono pliku logo: {logo!r}")

    main_path = root / "main.tex"
    if main_path.is_file():
        for included in INCLUDE_RE.findall(read_text(main_path)):
            candidates = (root / f"{included}.tex", root / included)
            if not any(candidate.is_file() for candidate in candidates):
                problems.append(f"main.tex: nie znaleziono dołączanego pliku {included}")

    files_to_scan = [root / "frontmatter" / "abstracts.tex"]
    for option, relative_path in OPTIONAL_FILES.items():
        if metadata.get(option) == "true":
            files_to_scan.append(root / relative_path)

    for path in files_to_scan:
        if not path.is_file():
            problems.append(f"nie znaleziono wymaganego pliku {path.relative_to(root)}")
            continue
        text = read_text(path)
        for marker in PLACEHOLDER_PATTERNS:
            if marker in text:
                problems.append(f"{path.relative_to(root)}: pozostawiono treść przykładową: {marker}")

    if problems:
        print("Znalezione problemy:")
        for problem in problems:
            print(f"  - {problem}")
        print(f"\nŁącznie: {len(problems)}")
        return 1 if args.strict else 0

    print("Walidacja zakończona: nie znaleziono problemów.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
