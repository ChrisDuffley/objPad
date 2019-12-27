# ObjPad #

* Autorzy: Joseph Lee, Cleverson Uliana and others
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

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
* SPACE or ENTER: activate.

W aktywnym trybie sieciowym, można przemieszczać się po elementach
standardowo lub poruszać się po obiektach, linkach, polach formularza,
nagłówkach, ramkach, tabelach, listach, punktach orientacyjnych:

* Strzałka w prawo: następny element.
* Strzałka w lewo: poprzedni element.
* Strzałka w górę: poprzedni typ elementu.
* Strzałka w dół: następny typ elementu.
* SPACE or ENTER: activate.

W aktywnym trybie skanowania:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Strzałka w prawo: odczytaj następny znak.
* Strzałka w lewo: odczytaj poprzedni znak.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.09

* Added localizations.
* Enter key (regular and Numpad) can be used to activate objects.

## Wersja 18.03

* Lepsza zgodność z NVDA 2018.1.

## Wersja 16.12

* Dodano tryb sieciowy.

## wersja 16.10

* Pierwsza wersja stabilna

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev

[3]: https://addons.nvda-project.org/files/get.php?file=objPad-2019
