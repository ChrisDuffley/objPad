# ObjPad #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* Pobierz [wersja stabilna][1]
* NVDA compatibility: 2022.4 and later

Ta wtyczka dodaje szybkie komendy służące do zarządzania obiektami na
ekranie, między innymi nawigację i inne udogodnienia.

## Komendy

* Control+NVDA+TAB: przełącza między trybami nawigacji (Szczegóły znajdziesz
  poniżej).

## Tryby nawigacji

Dodatek pozwala używać klawiszy strzałek w czterech różnych trybach:

* Tryb klasyczny lub standardowy: Klawisze strzałek przemieszczają kursor.
* Tryb nawigacji obiektowej: klawisze strzałek przemieszczają do
  następnego/poprzedniego/nadrzędnego/pierwszego obiektu podrzędnego.
* Tryb sieciowy: klawisze strzałek przełączają cyklicznie między elementami
  lub służą do przemieszczania się między nimi.
* Tryb skanowania: klawisze strzałek służą do przemieszczania się między
  obiektami na ekranie, niezależnie od ich hierarchii.

Komendy trybu nawigacji:

* Strzałka w prawo: następny obiekt.
* Strzałka w lewo: poprzedni obiekt.
* Strzałka w górę: obiekt nadrzędny.
* Strzałka w dół: pierwszy obiekt podrzędny.
* SPACJA lub ENTER: aktywuj.

W aktywnym trybie sieciowym, można przemieszczać się po elementach
standardowo lub poruszać się po obiektach, linkach, polach formularza,
nagłówkach, ramkach, tabelach, listach, punktach orientacyjnych:

* Strzałka w prawo: następny element.
* Strzałka w lewo: poprzedni element.
* Strzałka w górę: poprzedni typ elementu.
* Strzałka w dół: następny typ elementu.
* SPACJA lub ENTER: aktywuj.

W aktywnym trybie skanowania:

* Strzałka w dół: następny obiekt lub następna linia.
* Strzałka w górę: poprzedni obiekt lub poprzedni wiersz.
* Strzałka w prawo: odczytaj następny znak.
* Strzałka w lewo: odczytaj poprzedni znak.
* Control+strzałka w prawo: następne słowo.
* Control+strzałka w lewo: Poprzednie słowo.
* SPACJA lub ENTER: aktywuj.

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.06

* Requires NVDA 2021.3 or later.

## Wersja 21.04

* Wymaga NVDA 2020.1 lub nowszego.

## Wersja 20.01

* Wymaga NVDA 2019.3 lub nowszej.

## Wersja 18.12

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Wersja 18.09

* Dodano tłumaczenia.
* Normalny klawisz enter lub numeryczny może być użyty do aktywownia
  obiektu.

## Wersja 18.03

* Lepsza zgodność z NVDA 2018.1.

## Wersja 16.12

* Dodano tryb sieciowy.

## Wersja 16.10

* Pierwsza wersja stabilna.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
