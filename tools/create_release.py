#!/usr/bin/env python3
"""Tworzy minimalną, przenośną paczkę startową szablonu pracy."""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT_FILES = (
    ".gitignore",
    "README.md",
    "bibliografia.bib",
)
SOURCE_DIRS = (
    "assets",
    "backmatter",
    "config",
    "docs",
    "frontmatter",
)
IGNORED_NAMES = (
    "build",
    "dist",
    "legacy",
    "tmp",
    "__pycache__",
    "*.aux",
    "*.bbl",
    "*.bcf",
    "*.blg",
    "*.fdb_latexmk",
    "*.fls",
    "*.log",
    "*.out",
    "*.pdf",
    "*.pyc",
    "*.run.xml",
    "*.synctex.gz",
    "*.toc",
    ".DS_Store",
    "Thumbs.db",
)
TOOL_FILES = (
    "create_chapter.py",
    "create_release.py",
    "validate_project.py",
)
RESOURCE_DIRS = (
    "figures",
    "figures/source",
    "data",
    "code",
    "scripts",
    "tables",
)
DEFAULT_ARCHIVES = {
    "local": Path("dist/szablon-pracy-dyplomowej-local.zip"),
    "online": Path("dist/szablon-pracy-dyplomowej-online.zip"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Utwórz minimalny ZIP szablonu: wspólna konfiguracja, dokumentacja "
            "i jeden krótki rozdział, bez wyników kompilacji i przykładów."
        )
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="własna nazwa pliku wynikowego ZIP",
    )
    parser.add_argument(
        "--target",
        choices=("local", "online"),
        help="wariant paczki; bez tej opcji program zapyta o wybór",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="katalog projektu; domyślnie ustalany automatycznie",
    )
    return parser.parse_args()


def choose_target(requested: str | None) -> str:
    if requested:
        return requested
    if not sys.stdin.isatty():
        raise ValueError(
            "Brak interaktywnego terminala. Podaj --target local albo --target online."
        )

    print("Wybierz wariant paczki startowej:")
    print("  1. local  - komputer lokalny; zawiera latexmkrc i katalog build")
    print("  2. online - Prism/Overleaf; bez lokalnego latexmkrc")
    while True:
        answer = input("Wariant [1/2, domyślnie 1]: ").strip().lower()
        if answer in {"", "1", "local", "l"}:
            return "local"
        if answer in {"2", "online", "o"}:
            return "online"
        print("Wpisz 1 dla wariantu local albo 2 dla wariantu online.")


def copy_required(source: Path, destination: Path) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Brak wymaganego elementu: {source}")
    if source.is_dir():
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns(*IGNORED_NAMES),
        )
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def starter_main(source: str) -> str:
    """Pozostawia jeden rozdział i usuwa demonstracyjne załączniki."""
    lines = source.splitlines(keepends=True)
    result: list[str] = []
    in_appendix_list = False
    kept_chapter = False

    for line in lines:
        stripped = line.strip()
        if stripped == r"\startthesisappendices":
            in_appendix_list = True
            result.extend(
                (
                    "% Aby dodać załączniki, odkomentuj i uzupełnij poniższe polecenia.\n",
                    "% \\startthesisappendices\n",
                    "% \\include{chapters/08-zalacznik-a}\n",
                )
            )
            continue
        if in_appendix_list:
            if stripped == r"\end{document}":
                in_appendix_list = False
                result.append(line)
            continue
        if stripped.startswith(r"\include{chapters/"):
            if not kept_chapter:
                result.append(r"\include{chapters/01-wprowadzenie}" + "\n")
                kept_chapter = True
            continue
        result.append(line)

    if not kept_chapter or not any(line.strip() == r"\end{document}" for line in result):
        raise ValueError("Nie rozpoznano struktury main.tex; przerwano tworzenie paczki.")
    return "".join(result)


def starter_chapter() -> str:
    return r"""\chapter{\ploren{Wprowadzenie}{Introduction}}
\label{ch:wprowadzenie}

Ten krótki rozdział pokazuje miejsce przeznaczone na treść pracy. W polskiej
wersji dokumentu nie trzeba tłumaczyć całych rozdziałów na język angielski;
angielski odpowiednik w poleceniu \verb|\ploren| służy jako tytuł wybierany
automatycznie po zmianie języka całej pracy.

\section{Przykładowa sekcja}

Nowy akapit rozpoczyna pusty wiersz w pliku źródłowym. Rozdziały należy
przechowywać w oddzielnych plikach katalogu \texttt{chapters}, a ich kolejność
ustalać w oznaczonym miejscu pliku \texttt{main.tex}. Przed rozpoczęciem pracy
należy uzupełnić dane w \texttt{config/metadata.tex}.
"""


def variant_readme(target: str) -> str:
    if target == "local":
        return """# Wariant lokalny

Ta paczka zawiera `latexmkrc` i jest przeznaczona do kompilacji na komputerze.

Na Windows zainstaluj MiKTeX oraz interpreter Perl (np. Strawberry Perl),
ponieważ `latexmk` jest skryptem napisanym w Perlu. Sprawdź środowisko:

```text
perl --version
latexmk -v
```

Kompiluj ją poleceniem:

```text
latexmk main.tex
```

LuaLaTeX oraz katalog `build/` zostaną wybrane automatycznie.
"""
    return """# Wariant internetowy

Ta paczka jest przeznaczona do Prism, Overleaf lub podobnego edytora. Nie zawiera
lokalnego pliku `latexmkrc`. Po imporcie ustaw:

- dokument główny: `main.tex`;
- kompilator: LuaLaTeX.

Katalogiem plików pomocniczych zarządza platforma internetowa. Lokalna
instalacja Perla nie jest potrzebna.
"""


def write_starter_tree(project_root: Path, staging: Path, target: str) -> None:
    for name in ROOT_FILES:
        copy_required(project_root / name, staging / name)
    if target == "local":
        copy_required(project_root / "latexmkrc", staging / "latexmkrc")
    for name in SOURCE_DIRS:
        copy_required(project_root / name, staging / name)

    (staging / "WARIANT.md").write_text(variant_readme(target), encoding="utf-8")

    tools_dir = staging / "tools"
    tools_dir.mkdir(parents=True)
    for name in TOOL_FILES:
        copy_required(project_root / "tools" / name, tools_dir / name)

    chapters_dir = staging / "chapters"
    chapters_dir.mkdir()
    copy_required(project_root / "chapters" / "README.md", chapters_dir / "README.md")
    (chapters_dir / "01-wprowadzenie.tex").write_text(starter_chapter(), encoding="utf-8")
    resources = chapters_dir / "01-wprowadzenie"
    for relative in RESOURCE_DIRS:
        directory = resources / relative
        directory.mkdir(parents=True, exist_ok=True)
        (directory / ".gitkeep").touch()

    main_source = (project_root / "main.tex").read_text(encoding="utf-8")
    (staging / "main.tex").write_text(starter_main(main_source), encoding="utf-8")


def create_zip(staging: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    temporary = archive.with_suffix(archive.suffix + ".tmp")
    if temporary.exists():
        temporary.unlink()
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as handle:
            for path in sorted(staging.rglob("*")):
                if path.is_file():
                    handle.write(path, path.relative_to(staging).as_posix())
        temporary.replace(archive)
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve()
    try:
        target = choose_target(args.target)
    except ValueError as error:
        print(f"Błąd: {error}", file=sys.stderr)
        return 2

    output = args.output or DEFAULT_ARCHIVES[target]
    if not output.is_absolute():
        output = project_root / output
    output = output.resolve()

    if not (project_root / "main.tex").is_file():
        print(f"Błąd: nie znaleziono main.tex w {project_root}", file=sys.stderr)
        return 2
    if output == project_root or project_root in output.parents and output.is_dir():
        print("Błąd: plik wynikowy musi wskazywać archiwum ZIP.", file=sys.stderr)
        return 2
    if output.suffix.lower() != ".zip":
        print("Błąd: plik wynikowy musi mieć rozszerzenie .zip.", file=sys.stderr)
        return 2

    try:
        with tempfile.TemporaryDirectory(prefix="thesis-release-") as temporary:
            staging = Path(temporary) / "szablon-pracy-dyplomowej"
            staging.mkdir()
            write_starter_tree(project_root, staging, target)
            create_zip(staging, output)
    except (FileNotFoundError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Błąd: {error}", file=sys.stderr)
        return 1

    with zipfile.ZipFile(output) as handle:
        file_count = len([item for item in handle.infolist() if not item.is_dir()])
    print(f"Utworzono: {output.relative_to(project_root) if project_root in output.parents else output}")
    print(f"Wariant: {target}")
    print(f"Liczba plików: {file_count}")
    print(f"Rozmiar: {output.stat().st_size / 1024:.1f} KiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
