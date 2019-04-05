# ObjPad #

* Autori: Joseph Lee, Cleverson Uliana i drugi
* Preuzmi [stable version][1]
* Preuzmi [development version][2]
* NVDA compatibility: 2017.3 to 2019.1

Ovaj dodatak pruža brze naredbe za upravljanje objektima na zaslonu,
uključujući navigaciju i druge mogućnosti. 

## Naredbe 

* Control+NVDA+TAB: Izgovara različite načine korištenja tipki sa strelicama
  (vidi dolje za detalje).

## Načini korištenja tipki sa strelicama 

Dodatak nudi četiri načina korištenja tipki sa strelicama: 

* Klasični (ili uobičajeni način) koristite tipke sa strelicama za pomicanje
  kursora.
* Način objektne navigacije: koristite tipke sa strelicama za pomak na
  prethodni/sljedeći objekt.
* Web: Pomoću tipki sa strelicama kružite kroz elemente i krećite se između
  njih.
* Način skeniranja: koristite tipke sa strelicama za kretanje između
  objekata na zaslonu bez obzira na hijerarhiju.

Sljedeće naredbe su dostupne ako su tipke sa strelicama postavljene na način
objektne navigacije:

* Strelica desno: sljedeći objekt.
* Strelica lijevo: prethodni objekt.
* Strelica gore: objekt više razine.
* Strelica dolje: prvi objekt niže razine.
* SPACE or ENTER: activate.

Ako je aktivan način rada u web okruženju (elementi su uobičajeni ili se
kreću prema objektu, linku, polju obrasca, naslovu, okviru, tablici, popisu,
orijentiru): 

* Strelica desno: sljedeći element.
* Strelica lijevo: prethodni element.
* Strelica gore: tip prethodnog elementa.
* Strelica dolje: tip sljedećeg elementa.
* SPACE or ENTER: activate.

Ako je aktivan način skeniranja:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Strelica desno: pregled sljedećeg znaka.
* Strelica lijevo: prethodni znak.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

## Version 18.09

* Added localizations.
* Enter key (regular and Numpad) can be used to activate objects.

## Inačica 18.03

* Bolja kompatibilnost s NVDA inačicom 2018.1.

## Inačica 16.12

* Dodan način rada u web okruženju.

## Inačica 16.10

* Inicijalna stabilna inačica.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev