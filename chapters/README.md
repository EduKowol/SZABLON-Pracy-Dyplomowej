# Materiały rozdziałów

Każdy główny plik rozdziału ma katalog o tej samej nazwie. Przykład:

```text
05-implementacja-badania.tex
05-implementacja-badania/
├── figures/        # gotowe pliki do wstawienia: PDF, PNG, JPEG
│   └── source/     # pliki edytowalne: SVG, drawio, FIG, projekty CAD itp.
├── data/           # CSV, dane pomiarowe i wejścia do wykresów
├── code/           # kod opisywany lub prezentowany w pracy
├── scripts/        # skrypty MATLAB/Python generujące wykresy i wyniki
└── tables/         # duże tabele wydzielone do plików TEX
```

## Zalecane formaty

- wykresy, schematy i diagramy wektorowe: PDF;
- fotografie: JPEG;
- zrzuty ekranu i grafika rastrowa z ostrymi krawędziami: PNG;
- dane tabelaryczne: CSV z nagłówkiem;
- kod źródłowy: oryginalne rozszerzenie języka;
- duże tabele LaTeX: TEX bez preambuły dokumentu.

Pliki źródłowe grafiki zachowuj w `figures/source/`, a wyeksportowany plik
PDF, PNG lub JPEG umieszczaj bezpośrednio w `figures/`.

## Nazewnictwo

Stosuj małe litery, cyfry i łączniki, bez spacji oraz polskich znaków, np.
`charakterystyka-czestotliwosciowa.pdf`, `pomiary-obciazenia.csv` i
`generuj-wykres.m`.

## Przykładowe użycie

```tex
\includegraphics[width=0.8\textwidth]
  {chapters/05-implementacja-badania/figures/stanowisko-pomiarowe.pdf}

\lstinputlisting[language=Python,caption={Implementacja regulatora}]
  {chapters/05-implementacja-badania/code/regulator.py}

\input{chapters/05-implementacja-badania/tables/wyniki-pomiarow}
```

Ścieżki w LaTeX-u są zawsze liczone względem katalogu zawierającego
`main.tex`, a nie względem aktualnego pliku rozdziału.

## Tworzenie kolejnego rozdziału

Z katalogu głównego projektu uruchom:

```powershell
python tools/create_chapter.py 07-wyniki-badan --title-pl "Wyniki badań" --title-en "Research results"
```

Skrypt tworzy plik TEX i wszystkie katalogi materiałów. Nie nadpisuje
istniejących plików, a po zakończeniu wyświetla gotowe polecenie `\include`.
