# Profesjonalny szablon pracy dyplomowej (LaTeX)

Szablon obsługuje prace inżynierskie, magisterskie i doktorskie, pisane po polsku lub angielsku. Dane autora, język i typ pracy konfiguruje się wyłącznie w `config/metadata.tex`.

Rozbudowana dokumentacja dla studenta znajduje się w katalogu `docs/`:
[poradnik](docs/poradnik-studenta.md), [przykłady LaTeX-a](docs/latex-przyklady.md)
i [lista kontrolna](docs/lista-kontrolna.md).

## Powiązany szablon prezentacji

Do przygotowania prezentacji na obronę pracy można wykorzystać powiązany
szablon LaTeX Beamer: [EduKowol/SZABLON-Prezentacji](https://github.com/EduKowol/SZABLON-Prezentacji.git).

## Szybki start

1. Uzupełnij `config/metadata.tex`.
2. Ustaw `\thesislanguage` na `polish` albo `english`.
3. Ustaw `\thesistype` na `engineering`, `master` albo `doctoral`.
4. Zastąp teksty instruktażowe w `chapters/` własną treścią.
5. Dodawaj źródła do `bibliografia.bib` i cytuj je przez `\cite{klucz}`.
6. Uruchom `latexmk main.tex`. Gotowy dokument oraz wszystkie pliki pomocnicze znajdą się w katalogu `build/`.

## Tryb elektroniczny i druk dwustronny

Ustawienie `\thesisprintmode` w `config/metadata.tex` przyjmuje jedną z wartości:

- `digital` — domyślny PDF z równymi marginesami bocznymi 2,5 cm;
- `print` — druk dwustronny z marginesem wewnętrznym 3 cm i zewnętrznym 2 cm.

W trybie `print` rozdziały zaczynają się na stronach nieparzystych. Szablon może
więc dodać puste strony; jest to zamierzone i potrzebne przy druku dwustronnym.
Suma marginesów bocznych w obu trybach wynosi 5 cm, dlatego szerokość pola
tekstu i łamanie wierszy pozostają takie same.

## Opcjonalne wykazy

W pliku `config/metadata.tex` można niezależnie włączyć automatyczny spis
rysunków, spis tabel, spis listingów, wykaz skrótów oraz wykaz oznaczeń,
zmieniając odpowiednie wartości z
`false` na `true`:

```tex
\newcommand{\showlistoffigures}{true}
\newcommand{\showlistoftables}{true}
\newcommand{\showlistoflistings}{true}
\newcommand{\showabbreviationlist}{true}
\newcommand{\showsymbollist}{true}
```

Spisy rysunków i tabel powstają automatycznie z poleceń `\caption`, a spis
listingów z podpisów `caption` środowiska `lstlisting`. Symbole,
ich opisy i jednostki należy uzupełnić w `frontmatter/symbols.tex`, a skróty
w `frontmatter/abbreviations.tex`.

## Opcjonalne strony i oświadczenia

W `config/metadata.tex` można niezależnie włączyć dedykację, deklarację użycia
AI, podziękowania, informację o finansowaniu oraz dostępności danych i kodu:

```tex
\newcommand{\showdedication}{true}
\newcommand{\showaideclaration}{true}
\newcommand{\showacknowledgements}{true}
\newcommand{\showfundingstatement}{true}
\newcommand{\showavailabilitystatement}{true}
```

Treść należy uzupełnić w odpowiednich plikach katalogów `frontmatter/` i
`backmatter/`. Przykładowe oświadczenia trzeba zawsze dostosować do regulaminu
uczelni, zasad finansującego oraz warunków repozytorium danych lub kodu.

## Kompilacja i porządek w katalogu

Konfiguracja `latexmkrc` kieruje PDF, logi, bibliografię i wszystkie pliki pomocnicze do katalogu `build/`. Katalog główny pozostaje dzięki temu czysty.

```text
latexmk main.tex       # kompilacja
latexmk -C main.tex    # usunięcie wszystkich artefaktów kompilacji
```

Gotowy dokument po kompilacji: `build/main.pdf`.

### Ponowna kompilacja po usunięciu błędu

Po nieudanej kompilacji `latexmk` może zachować informację o błędzie w swojej
bazie zależności. Jeżeli przyczyna została już usunięta — na przykład zamknięto
przeglądarkę blokującą `build/main.pdf` — ale zwykłe `latexmk main.tex` zgłasza,
że nie ma nic do wykonania, należy wymusić pełne przeliczenie projektu:

```text
latexmk -g main.tex
```

Taka sytuacja nie oznacza, że błąd nadal znajduje się w źródłach. Opcja `-g`
nakazuje ponownie wykonać reguły kompilacji bez usuwania plików pomocniczych.
Opcja `-C` ma inne zastosowanie: usuwa artefakty kompilacji i nie jest potrzebna
do zwykłego ponownego zbudowania dokumentu.

## Czysta paczka startowa

Pełny projekt zawiera rozdziały i załączniki demonstracyjne. Minimalną paczkę
dla nowej pracy, zawierającą jeden krótki rozdział i bez artefaktów kompilacji,
tworzy polecenie:

```text
python tools/create_release.py
```

Generator zapyta, czy utworzyć wariant `local`, przeznaczony do kompilacji na
komputerze i zawierający `latexmkrc`, czy wariant `online` dla Prism i Overleaf,
bez lokalnej konfiguracji LatexMk. Wynik otrzyma odpowiednio nazwę
`dist/szablon-pracy-dyplomowej-local.zip` albo
`dist/szablon-pracy-dyplomowej-online.zip`.

W skrypcie lub automatyzacji wybór można podać bez pytania:

```text
python tools/create_release.py --target local
python tools/create_release.py --target online
```

Generator kopiuje wspólną konfigurację bez tworzenia odrębnej wersji stylu,
dlatego po zmianach szablonu wystarczy ponownie go uruchomić.

Katalog `dist/` nie jest wykluczony przez `.gitignore`. Obie gotowe paczki ZIP
mogą dzięki temu być przechowywane w repozytorium i udostępniane użytkownikom
bez konieczności lokalnego uruchamiania generatora. Po każdej zmianie plików
wchodzących w skład wydania należy ponownie wygenerować oba warianty i zapisać
zaktualizowane archiwa w repozytorium.

### TeXstudio

W zakładce `Budowanie` można wybrać `Latexmk` jako kompilator. Plik `main.tex` zawiera projektową dyrektywę TeXstudio, która usuwa z wbudowanego polecenia wyłącznie opcję `-pdf`, aby nie wymuszać pdfLaTeX. Dodawane przez TeXstudio `-auxdir=build` jest zgodne z konfiguracją projektu. Silnik LuaLaTeX i katalog wynikowy są konfigurowane centralnie w `latexmkrc`.

Przy pierwszym otwarciu dokumentu TeXstudio może poprosić o zgodę na zmianę polecenia kompilacji. Należy wybrać zgodę tylko dla tego dokumentu.

## Struktura i utrzymanie

- `main.tex` — kolejność elementów;
- `config/metadata.tex` — dane i ustawienia pracy;
- `config/document-class.tex` — wewnętrzny wybór klasy dla trybu `digital` lub `print`;
- `config/thesis-style.sty` — typografia, marginesy i lokalizacja;
- `frontmatter/` — oświadczenie i streszczenia PL/EN;
- `chapters/` — treść rozdziałów;
- `chapters/<nazwa-rozdziału>/` — rysunki, ich pliki źródłowe, dane, kod,
  skrypty MATLAB/Python i duże tabele danego rozdziału; szczegóły opisano w
  `chapters/README.md`;
- `tools/create_chapter.py` — bezpieczne tworzenie pliku i struktury nowego
  rozdziału;
- `assets/branding/` — logo uczelni i inne elementy identyfikacji wizualnej;
- `bibliografia.bib` — jedna baza bibliografii;
- `legacy/` — zachowana wersja pierwotna.

Zmiany wizualne wprowadzaj centralnie w `config/thesis-style.sty`. Nie wpisuj danych autora do `main.tex`, nie twórz bibliografii ręcznie i używaj `\label`, `\cref`, `\Cref` oraz `\cite`. Przed oddaniem pracy zawsze sprawdź aktualne wymagania uczelni.

Do zapisu liczb i jednostek używaj `siunitx`, np. `\qty{230}{\volt}`,
`\qty{50}{\hertz}`, `\num{1.25e-3}` i `\qtyrange{10}{20}{\milli\ampere}`.
Separator dziesiętny jest automatycznie dopasowywany do języka pracy.
Odwołania twórz przez `\cref{fig:etykieta}` lub `\Cref{fig:etykieta}`;
rodzaj elementu i jego polska albo angielska nazwa zostaną dobrane automatycznie.

Akapity oddzielaj pustym wierszem wyłącznie w kodzie źródłowym LaTeX-a.
W dokumencie akapit jest oznaczany wcięciem `0,75 cm`, bez dodatkowego odstępu
pionowego; pierwszy akapit po nagłówku nie ma wcięcia. Nie dodawaj ręcznie
`\\`, `\vspace` ani kilku pustych wierszy między zwykłymi akapitami.
Jeżeli również pierwszy akapit po nagłówku ma być wcięty, ustaw w
`config/metadata.tex` wartość `\indentfirstparagraph` na `true`.

## Duże elementy i strony poziome

Duże rysunki wstawiaj przez `\thesisgraphic`, które zachowuje proporcje i
ogranicza grafikę do szerokości oraz wysokości pola tekstowego:

```tex
\begin{figure}[htbp]
  \centering
  \thesisgraphic{chapters/05-implementacja-badania/figures/schemat.pdf}
  \caption{Schemat badanego systemu}
  \label{fig:schemat-systemu}
\end{figure}
```

Szerokie tabele `tabular` można objąć środowiskiem `thesiswidetable`.
Tabel `longtable` nie należy skalować, ponieważ są przeznaczone do podziału
między stronami. Dla pełnej strony poziomej użyj `thesislandscape`:

```tex
\begin{thesislandscape}
  \begin{figure}[p]
    \centering
    \thesisgraphic[max height=0.72\textheight]{sciezka/do/schematu.pdf}
    \caption{Rozbudowany schemat systemu}
    \label{fig:schemat-poziomy}
  \end{figure}
\end{thesislandscape}
```

Polecenie `\FloatBarrier` zatrzymuje wcześniejsze rysunki i tabele przed
przejściem do kolejnej części tekstu. Stosuj je tylko na logicznych granicach;
nie wymuszaj powszechnie położenia elementów opcją `[H]`.

## Kod i listingi

Kod przechowuj w katalogu `code/` danego rozdziału i wczytuj bez kopiowania:

```tex
\lstinputlisting[
  style=thesis-python,
  caption={Implementacja regulatora},
  label={lst:regulator}
]{chapters/05-implementacja-badania/code/regulator.py}
```

Dostępne style to `thesis-python`, `thesis-matlab`, `thesis-c`, `thesis-cpp`
i `thesis-shell`. Wybrany fragment pliku można ograniczyć opcjami
`firstline` i `lastline`. Listing otrzymuje numer rozdziałowy, trafia do
opcjonalnego spisu listingów i może być przywołany przez `\cref{lst:regulator}`.

Krótki przykład można umieścić bezpośrednio:

```tex
\begin{lstlisting}[
  style=thesis-matlab,
  caption={Wyznaczenie charakterystyki},
  label={lst:charakterystyka}
]
f = linspace(0, 1000, 500);
H = freqresp(sys, 2*pi*f);
\end{lstlisting}
```

Długich listingów nie ustawiaj jako elementów pływających: bez opcji `float`
mogą naturalnie dzielić się między stronami. Pełne programy lepiej udostępnić
w repozytorium lub dodatku, a w treści pokazywać tylko analizowane fragmenty.

## Walidacja przed oddaniem pracy

Podczas pisania pozostaw w `config/metadata.tex`:

```tex
\newcommand{\thesisstatus}{draft}
```

W tym trybie przykładowe dane powodują ostrzeżenia. Przed oddaniem ustaw
`final`; nieuzupełnione podstawowe metadane spowodują wtedy błąd kompilacji.
Pełną kontrolę treści zastępczych i plików uruchom poleceniem:

```text
python tools/validate_project.py --strict
```

Bez `--strict` skrypt drukuje raport, ale zwraca kod powodzenia, co jest wygodne
w trakcie pisania. Walidacja nie zastępuje sprawdzenia aktualnych wymagań
uczelni ani korekty merytorycznej i językowej.
