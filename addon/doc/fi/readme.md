# ObjPad #

* Tekijät: Joseph Lee, Cleverson Uliana sekä muut
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* NVDA compatibility: 2017.3 to 2019.2

Tämä lisäosa tarjoaa pikakomentoja ruudulla olevien objektien hallintaan,
navigointi ja muut mahdollisuudet mukaan lukien.

## Komennot

* Control+NVDA+Sarkain: Vaihtaa nuolinäppäintilaa (katso lisätietoja alta).

## Nuolinäppäintilat

Lisäosa tarjoaa neljä tapaa nuolinäppäinten käyttämiseen:

* Perinteinen (tai normaali tila): käytä nuolinäppäimiä kohdistimen
  siirtämiseen.
* Objektinavigointi: käytä nuolinäppäimiä seuraavaan/edelliseen/ylemmän
  tason/ensimmäiseen alemman tason objektiin siirtymiseen.
* Verkko: käytä nuolinäppäimiä elementtityypin vaihtamiseen ja niiden
  välillä liikkumiseen.
* Skannaustila: käytä nuolinäppäimiä ruudulla olevien objektien välillä
  liikkumiseen niiden hierarkiasta riippumatta.

Seuraavat komennot ovat käytettävissä, kun nuolinäppäinten tilana on
objektinavigointi:

* Nuoli oikealle: seuraava objekti.
* Nuoli vasemmalle: edellinen objekti.
* Nuoli ylös: ylemmän tason objekti.
* Nuoli alas: ensimmäinen alemman tason objekti.
* Väli tai Enter: aktivoi.

Kun verkkotila on aktiivisena (elementit ovat normaaleja tai niiden välillä
liikutaan objekti, linkki, lomakekenttä, otsikko, kehys, taulukko, luettelo
ja kiintopiste kerrallaan):

* Nuoli oikealle: seuraava elementti.
* Nuoli vasemmalle: edellinen elementti.
* Nuoli ylös: edellinen elementtityyppi.
* Nuoli alas: seuraava elementtityyppi.
* Väli tai Enter: aktivoi.

Skannaustilan ollessa aktiivisena:

* Nuoli alas: seuraava objekti tai rivi.
* Nuoli ylös: edellinen objekti tai rivi.
* Nuoli oikealle: seuraava merkki.
* Nuoli vasemmalle: edellinen merkki.
* Ctrl+Nuoli oikealle: seuraava sana.
* Ctrl+Nuoli vasemmalle: edellinen sana.
* Väli tai Enter: aktivoi.

## Versio 18.09

* Lokalisointeja lisätty.
* Tavallista ja laskinnäppäimistön Enter-näppäintä voi käyttää objektien
  aktivoimiseen.

## Versio 18.03

* Parempi yhteensopivuus NVDA 2018.1:n kanssa.

## Versio 16.12

* Lisätty verkkotila.

## Versio 16.10

* Ensimmäinen vakaa versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev
