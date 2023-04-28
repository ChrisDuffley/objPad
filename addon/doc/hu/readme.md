# Nyílmódok #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* [stabil verzió][1] letöltése
* NVDA compatibility: 2022.4 and later

Ez a bővítmény alternatívát nyújt az NVDA különböző navigációs módjainak
kezelésére. Az NVDA különböző kurzorainak mozgatását mind a nyílbillentyűkre
koncentrálja. Hogy a nyílbillentyűk mikor melyik kurzort, hogy s mint
mozgatják attól függ, hogy a felhasználó egy billentyűparanccsal melyik
navigációs módra vált.

## Parancsok

* Ctrl+NVDA+Tab: Vált a nyílbillentyűk kezelésének módjai (a továbbiakban:
  nyílmódok) között, lásd alább.

## Nyílmódok

A bővítmény használatával a nyílbillentyűk viselkedése az alábbi módon
változtatható:

* Normál: a nyílbillentyűk a kurzort mozgatják.
* Elemnavigáció: a nyílbillentyűkkel az előző vagy következő elemre, illetve
  a szülő- vagy gyermekelemre lehet lépni.
* Webmód: a nyílbillentyűkkel lehet váltogatni a webes elemtípusokat és az
  egyes elemek közt navigálni.
* áttekintőmód: a nyílbillentyűkkel lehet az egyes képernyőelemeken mozogni
  a köztük fennálló kapcsolattól függetlenül.

Elemnavigációs módban a következő parancsok érhetők el:

* Jobbnyíl: következő elem.
* Balnyíl: előző elem.
* Felnyíl: szülőelem.
* Lenyíl: az első gyermekelem.
* Szóköz vagy enter: elem aktiválása

Webmódban elérhető a normál és az elemenkénti navigáció. A választható
elemek: hivatkozás, űrlapmező, címsor, keret, táblázat, lista, jelzőpont.

* Jobbra nyíl: következő webes elem.
* Balra nyíl: előző webes elem.
* Felnyíl: előző webes elemtípus.
* Lenyíl: következő webes elemtípus.
* Szóköz vagy enter: elem aktiválása

Áttekintőmód:

* lenyíl: következő elem vagy következő sor.
* felnyíl: előző elem vagy előző sor.
* Jobbnyíl: következő karakter.
* Balnyíl: előző karakter.
* Ctrl+Jobbnyíl: következő szó.
* Ctrl+balnyíl: előző szó.
* Szóköz vagy enter: elem aktiválása

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

## A 20.01 verzió változásai:

* Az NVDA 2019.3 vagy újabb kiadására van szükség.

## A 18.12 verzió változásai:

* Belső változások, hogy a bővítmény kompatibilis legyen a későbbi NVDA
  kiadásokkal.

## A 18.09 verzió változásai:

* Fordításokat adtak hozzá.
* Az Enterrel vagy a Numpad billentyűivel lehet az elemeket aktiválni.

## A 18.03 verzió változásai:

* Jobb együttműködés az NVDA 2018.1 verziójával.

## A 16.12 verzió változásai:

* Hozzáadták a webmódot.

## A 16.10 verzió változásai:

* Első stabil verzió.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
