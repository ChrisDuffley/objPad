# ObjPad #

* Tekijät: Christopher Duffley <nvda@chrisduffley.com> (alkuperäiset tekijät
  Joseph Lee, Cleverson Uliana sekä muut)
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2022.4 ja uudemmat

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

## Versio 23.05

* Ylläpitäjän vaihdos on huomioitu päivittämällä manifestitiedosto
  asianmukaisesti.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Windows 10 21H2 (marraskuun 2021 päivitys/koontiversio 19044) tai uudempi
  vaaditaan.

## Versio 23.01

* Vaatii NVDA 2022.3:n tai uudemman.
* Windows 10 tai uudempi vaaditaan, koska Microsoft ei enää tue Windows
  7:ää, 8:aa tai 8.1:tä tammikuusta 2023 alkaen.

## Versio 22.06

* Vaatii NVDA 2021.3:n tai uudemman.

## Versio 21.04

* Edellyttää NVDA 2020.1:tä tai uudempaa.

## Versio 20.01

* Vaatii NVDA 2019.3:n tai uudemman.

## Versio 18.12

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
