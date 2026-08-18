# Upravljaj objektima (ObjPad)

* Autori: Christopher Duffley <nvda@chrisduffley.com>, izvorno od Joseph Lee, Cleverson Uliana i drugih

Ovaj dodatak pruža brze naredbe za upravljanje objektima na ekranu, uključujući kretanje i druge mogućnosti.

## Naredbe

* Kontrol+NVDA+TAB: Prolazi kroz različite moduse za upotrebu tipki sa strelicama (vidi dolje za detalje).

## Modusi za upotrebu tipki sa strelicama

Dodatak nudi četiri modusa za upotrebu tipki sa strelicama:

* Klasični (ili uobičajeni modus): koristite tipke sa strelicama za premještanje kursora.
* Kretanje po objektima: koristite tipke sa strelicama za premještanje na prethodne, sljedeće, nadređene i podređene objekte.
* Web: Pomoću tipki sa strelicama kružite kroz elemente i krećite se između njih.
* Modus skeniranja: koristite tipke sa strelicama za kretanje između objekata na ekranu bez obzira na hijerarhiju.

Sljedeće naredbe su dostupne, ako su tipke sa strelicama postavljene na kretanje po objektima:

* Strelica desno: sljedeći objekt.
* Strelica lijevo: prethodni objekt.
* Strelica gore: nadređeni objekt.
* Strelica dolje: podređeni objekt.
* RAZMAKNICA ili ENTER: aktiviranje.

Kad je web modus aktivan (elementi su uobičajeni ili se kreću po objektu, poveznici, polju obrasca, naslovu, okviru, tablici, popisu, orijentiru):

* Strelica desno: sljedeći element.
* Strelica lijevo: prethodni element.
* Strelica gore: prethodna vrsta elementa.
* Strelica dolje: sljedeća vrsta elementa.
* RAZMAKNICA ili ENTER: aktiviranje.

Kad je modus skeniranja aktivan:

* Strelica dolje: sljedeći objekt ili sljedeći redak.
* Strelica gore: prethodni objekt ili prethodni redak.
* Strelica desno: pregled sljedećeg znaka.
* Strelica lijevo: prethodni znak.
* Kontrol+Strelica desno: sljedeća riječ.
* Kontrol+Strelica lijevo: prethodna riječ.
* RAZMAKNICA ili ENTER: aktiviranje.

## ObjPad settings

In NVDA 2026.2, a dedicated setting is introduced to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
