# ObjPad #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* Stiahnuť [stabilnú verziu][1]
* NVDA compatibility: 2022.4 and later

Pridáva klávesové skratky  na navigáciu a prácu s prvkami.

## Príkazy

* Ctrl+NVDA+TAB: prepína medzi dostupnými režimami (popísané nižšie).

## Režimi prezerania

Dostupné sú 4 režimi:

* Predvolený: Šípky pohybujú kurzorom tak, ako ste zvyknutí.
* Objektový: Šípky prechádzajú na nasledujúci alebo predchádzajúci objekt
  resp. na rodiča alebo potomka objektu.
* Webový: Šípky prechádzajú medzi prvkami v režime prehliadania.
* skenovací: prechádza medzi objektmi, pričom ignoruje hierarchiu objektov.

V objektovom režime sú dostupné tieto príkazy:

* Pravá šípka: Nasledujúci objekt.
* Ľavá šípka: predchádzajúci objekt.
* Šípka hore: Rodičovský (nadradený objekt).
* Šípka dole: Potomok (podradený objekt).
* Medzera alebo enter: Aktivovať.

Webový režim (môžete sa pohybovať po prvkoch ako oblasti, prvky formulára,
nadpisy, rámce, tabuľky a zoznamy).

* Pravá šípka: Nasledujúci prvok.
* Ľavá šípka: Predchádzajúci prvok.
* Šípka hore: Prejdi na predchádzajúci typ prvku.
* Šípka dole: Prejdi na nasledujúci typ prvku.
* Medzera alebo enter: Aktivovať.

Skenovací režím:

* Šípka dole: Nasledujúci objekt, nasledujúci riadok.
* Šípka hore: Predchádzajúci objekt, predchádzajúci riadok.
* Pravá šípka: Nasledujúci znak.
* Ľavá šípka: Predchádzajúci znak.
* Ctrl+pravá šípka: Nasledujúce slovo.
* Ctrl+ľavá šípka: Predchádzajúce slovo.
* Medzera alebo enter: Aktivovať.

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

## Version 21.04

* Requires NVDA 2020.1 or later.

## Verzia 20.01

* Vyžaduje NVDA od verzie 2019.3.

## Verzia 18.12

* Príprava na podporu nasledujúcich verzií NVDA.

## Verzia 18.09

* Pridané preklady.
* Objekty je možné aktivovať klávesom enter (aj na numerickom bloku).

## Verzia 18.03

* Prispôsobené pre NVDA 2018.1.

## Verzia 16.12

* Pridaný webový režim.

## Verzia 16.10

* Prvé vydanie.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
