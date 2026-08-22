# Nyílmódok

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Ez a bővítmény alternatívát nyújt az NVDA különböző navigációs módjainak kezelésére. Az NVDA különböző kurzorainak mozgatását mind a nyílbillentyűkre koncentrálja. Hogy a nyílbillentyűk mikor melyik kurzort, hogy s mint mozgatják attól függ, hogy a felhasználó egy billentyűparanccsal melyik navigációs módra vált.

## Parancsok

* Ctrl+NVDA+Tab: Vált a nyílbillentyűk kezelésének módjai (a továbbiakban: nyílmódok) között, lásd alább.

## Nyílmódok

A bővítmény használatával a nyílbillentyűk viselkedése az alábbi módon változtatható:

* Normál: a nyílbillentyűk a kurzort mozgatják.
* Elemnavigáció: a nyílbillentyűkkel az előző vagy következő elemre, illetve a szülő- vagy gyermekelemre lehet lépni.
* Webmód: a nyílbillentyűkkel lehet váltogatni a webes elemtípusokat és az egyes elemek közt navigálni.
* áttekintőmód: a nyílbillentyűkkel lehet az egyes képernyőelemeken mozogni a köztük fennálló kapcsolattól függetlenül.

Elemnavigációs módban a következő parancsok érhetők el:

* Jobbnyíl: következő elem.
* Balnyíl: előző elem.
* Felnyíl: szülőelem.
* Lenyíl: az első gyermekelem.
* Szóköz vagy enter: elem aktiválása

Webmódban elérhető a normál és az elemenkénti navigáció. A választható elemek: hivatkozás, űrlapmező, címsor, keret, táblázat, lista, jelzőpont.

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

## ObjPad settings

In NVDA 2026.2, a dedicated setting is introduced to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
