# Poradnik przygotowania pracy dyplomowej

> Ten dokument opisuje zalecany sposób pracy. Szczegółowe wymagania uczelni,
> wydziału i promotora mają zawsze pierwszeństwo.

## 1. Pierwsze uruchomienie szablonu

Zakres rozdziału: wymagane narzędzia, otwarcie projektu, pierwsza kompilacja,
lokalizacja pliku PDF oraz katalogu `build/`.

## 2. Konfiguracja pracy i wybór języka

Zakres rozdziału: `config/metadata.tex`, typ pracy, język, tryb `digital` lub
`print`, dane autora, tytuły, promotor, słowa kluczowe i elementy opcjonalne.

### 2.1. Praca polska i angielska

Wybór języka oznacza wybór języka całej pracy, a nie obowiązek przygotowania
dwóch wersji rozdziałów. W pracy polskiej po angielsku przygotowuje się tylko
wymagane elementy, przede wszystkim angielski tytuł, `Abstract` i `Keywords`.
Rozdziały, sekcje, podpisy rysunków, tabel i listingów pisze się wyłącznie po
polsku. Analogiczna zasada obowiązuje dla pracy angielskiej.

Polecenie `\ploren{tekst polski}{English text}` służy głównie do elementów
wspólnych szablonu. Student nie musi stosować go w zwykłej treści rozdziałów.

## 3. Organizacja plików i rozdziałów

Zakres rozdziału: `main.tex`, `chapters/`, katalogi `figures`, `data`, `code`,
`scripts` i `tables`, nazewnictwo plików oraz `tools/create_chapter.py`.

## 4. Jak planować strukturę pracy

Zakres rozdziału: zależność struktury od problemu, rodzaju pracy i metodyki;
logiczna kolejność rozdziałów; unikanie zbyt krótkich części i powtórzeń.

## 5. Wprowadzenie

Zakres rozdziału: kontekst, znaczenie problemu, istniejące rozwiązania, luka,
motywacja, wkład autora oraz zapowiedź struktury pracy. Przedstawiony układ jest
propozycją i może zostać zmieniony po uzgodnieniu z promotorem.

## 6. Cel, zakres, założenia i ograniczenia

Zakres rozdziału: cel główny i cele szczegółowe, zakres rzeczowy, założenia,
ograniczenia, wymagania oraz mierzalne kryteria oceny rozwiązania.

## 7. Przegląd literatury i podstawy teoretyczne

Zakres rozdziału: wyszukiwanie źródeł, porównywanie rozwiązań, identyfikacja
luki, synteza literatury, normy i dokumentacja techniczna. Przegląd literatury
nie jest streszczeniem kolejnych publikacji ani końcowym wykazem bibliografii.

## 8. Metodyka, projekt i implementacja

Zakres rozdziału: uzasadnienie wyboru metod, architektura rozwiązania,
stanowisko badawcze, sprzęt, oprogramowanie, algorytmy i sposób implementacji.

## 9. Badania i prezentowanie wyników

Zakres rozdziału: plan eksperymentu, warunki badań, powtarzalność, miary,
niepewność, prezentacja danych oraz rozdzielenie wyników od ich interpretacji.

## 10. Dyskusja wyników

Zakres rozdziału: interpretacja wyników, porównanie z literaturą, analiza
ograniczeń, źródła błędów, znaczenie praktyczne i możliwość uogólnienia.

## 11. Podsumowanie i wnioski

Zakres rozdziału: odpowiedź na postawiony problem, stopień realizacji celów,
najważniejsze rezultaty, ograniczenia oraz uzasadnione kierunki dalszych prac.

## 12. Cytowania i bibliografia

Zakres rozdziału: `\cite`, parafraza, cytat dosłowny, dobór wiarygodnych
źródeł, rekordy BibLaTeX, DOI i adresy internetowe. Bibliografia jest tworzona
automatycznie i zawiera cytowane pozycje.

## 13. Rysunki, wykresy i schematy

Zakres rozdziału: formaty PDF/PNG/JPEG, `\thesisgraphic`, podpisy, źródła,
etykiety, `\ref` i `\cref`, wykresy z MATLAB-a i Pythona, schematy oraz strony poziome.

## 14. Tabele

Zakres rozdziału: `booktabs`, jednostki w nagłówkach, wyrównanie liczb,
`tabularx`, `longtable`, `thesiswidetable` oraz unikanie nadmiernego skalowania.

## 15. Równania, symbole i jednostki

Zakres rozdziału: środowiska matematyczne, numeracja, `\label`, `\ref`, `\cref`,
wyjaśnianie symboli, `siunitx`, niepewności i wykaz oznaczeń.

## 16. Kod źródłowy i listingi

Zakres rozdziału: `\lstinputlisting`, style Python/MATLAB/C/C++/shell,
podpisy, etykiety, wybór zakresu wierszy, długie listingi i repozytorium kodu.

## 17. Dane, skrypty i odtwarzalność wyników

Zakres rozdziału: dane surowe i przetworzone, CSV, skrypty MATLAB/Python,
parametry eksperymentu, wersje oprogramowania, repozytoria, DOI i licencje.

## 18. Najczęstsze błędy LaTeX-a

Zakres rozdziału: brakujące pliki, niedomknięte środowiska, niezdefiniowane
etykiety, błędy bibliografii, znaki specjalne, przepełnione wiersze i logi.

## 19. Wersja elektroniczna i drukowana

Zakres rozdziału: `digital` i `print`, marginesy, druk dwustronny, puste strony,
kontrola osadzonych czcionek, metadane PDF i archiwizacja.

## 20. Walidacja i przygotowanie do oddania

Zakres rozdziału: tryby `draft` i `final`, `tools/validate_project.py`, kontrola
odnośników, spisów, bibliografii, danych autora i końcowa korekta dokumentu.

Skrócona procedura znajduje się w [liście kontrolnej](lista-kontrolna.md).
