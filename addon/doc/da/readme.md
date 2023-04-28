# ObjPad #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* Download [stabil version][1]
* NVDA compatibility: 2022.4 and later

Denne tilføjelse giver hurtige kommandoer til at styre objekter på skærmen,
herunder navigation og andre muligheder.

## Kommandoer

* Control+NVDA+TAB: Skifter gennem tilstanden der benyttes ved brug af
  piletasterne(se nedenfor for detaljer).

## Piletasttilstande

Tilføjelsen giver fire måder at bruge piletasterne på:

* Klassisk (eller normal tilstand): Brug piletasterne til at flytte
  markøren.
* Objektnavigation: Brug piletasterne til at gå til næste, forrige,
  underordnede og overordnede objekter.
* Web: Brug piletasterne til at gennemse elementer og flytte mellem dem.
* Scanningstilstand: Brug piletasterne til at flytte gennem objekter på
  skærmen uanset hierarki.

Følgende kommandoer er tilgængelige med piletasterne indstillet til
objektnavigation:

* Højre pil: Næste objekt.
* Venstre pil: Forrige objekt.
* Pil op: Overordnet objekt.
* Pil ned: Første underordnede objekt.
* Mellemrum eller ENTER: Aktivér.

Når webtilstand er aktiv, vil følgende kommandoer navigere mellem disse
elementer på en side, med mindre denne er indstillet til normal (objekt,
link, formularfelt, overskrift, ramme, tabel, liste, landmærke):

* Højre pil: Næste element.
* Venstre pil: Forrige element.
* Pil op: Forrige elementtype.
* Pil ned: Næste elementtype.
* Mellemrum eller ENTER: Aktivér.

Med scanningstilstand aktiv:

* Pil ned: Næste objekt eller næste linje.
* Pil op: Forrige objekt eller forrige linje.
* Højre pil: Næste tegn.
* Venstre pil: Forrige tegn.
* Control+højre pil: Næste ord.
* Control+venstre pil: Forrige ord.
* Mellemrum eller ENTER: Aktivér.

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

## Version 20.01

* Kræver NVDA 2019.3 eller nyere.

## Version 18.12

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Version 18.09

* Tilføjede oversættelser.
* Enter-tasten (talrækken på tastaturet og Numpad) kan bruges til at
  aktivere objekter.

## Version 18.03

* Bedre kompatibilitet med NVDA 2018.1.

## Version 16.12

* Tilføjet webtilstand.

## Version 16.10

* Første stabile version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
