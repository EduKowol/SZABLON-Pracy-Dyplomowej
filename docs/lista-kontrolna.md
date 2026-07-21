# Lista kontrolna przed oddaniem pracy

## Konfiguracja

- [ ] Wybrano poprawny język i typ pracy.
- [ ] Uzupełniono oba tytuły, dane autora, kierunek i promotora.
- [ ] Uzupełniono oba streszczenia i zestawy słów kluczowych.
- [ ] Włączono tylko potrzebne wykazy i oświadczenia.
- [ ] Wybrano właściwy tryb `digital` albo `print`.

## Treść

- [ ] Problem, cel, zakres i wkład autora są jednoznaczne.
- [ ] Każdy rozdział pełni określoną funkcję i wynika z poprzedniego.
- [ ] Wyniki są oddzielone od ich interpretacji.
- [ ] Wnioski odpowiadają na problem i cele pracy.
- [ ] Usunięto teksty instruktażowe oraz przykładowe dane.

## Źródła

- [ ] Wszystkie zapożyczone informacje mają odwołania do źródeł.
- [ ] Cytaty dosłowne są jednoznacznie oznaczone.
- [ ] Rekordy bibliograficzne zawierają kompletne i poprawne dane.
- [ ] Źródła internetowe mają autora lub instytucję, tytuł i adres.
- [ ] Numery DOI, norm, patentów i dokumentacji zostały zweryfikowane.

## Elementy techniczne

- [ ] Każdy rysunek, tabela, równanie i listing ma podpis lub numer.
- [ ] Każdy numerowany element ma `\label` i odwołanie w tekście.
- [ ] Jednostki i liczby zapisano przez `siunitx`.
- [ ] Rysunki są czytelne przy powiększeniu 100% i po wydruku.
- [ ] Szerokie elementy nie wychodzą poza marginesy.
- [ ] Kod w treści ograniczono do istotnych fragmentów.

## Dane i odtwarzalność

- [ ] Opisano źródło danych oraz sposób ich przetwarzania.
- [ ] Zachowano skrypty generujące wyniki i wykresy.
- [ ] Podano wersje istotnego oprogramowania i bibliotek.
- [ ] Uzupełniono informację o dostępności danych i kodu, jeśli jest włączona.
- [ ] Uzupełniono finansowanie i deklarację AI, jeśli są włączone.

## Kontrola dokumentu

- [ ] Spis treści i wszystkie opcjonalne wykazy są aktualne.
- [ ] Nie ma niezdefiniowanych odwołań ani brakujących cytowań.
- [ ] Nagłówki, podpisy i numeracja są konsekwentne.
- [ ] Przejrzano każdą stronę końcowego PDF.
- [ ] Sprawdzono ortografię, interpunkcję i styl.

## Walidacja końcowa

- [ ] Przy kompilacji lokalnej przez `latexmk` polecenie `perl --version` działa poprawnie.
- [ ] Ustawiono `\thesisstatus` na `final`.
- [ ] Polecenie `python tools/validate_project.py --strict` kończy się powodzeniem.
- [ ] `latexmk main.tex` kończy się bez błędów.
- [ ] Gotowy plik znajduje się w `build/main.pdf`.
- [ ] Zachowano kopię źródeł, danych, kodu i końcowego PDF.
