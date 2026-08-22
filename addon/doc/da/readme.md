# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Denne tilføjelse giver hurtige kommandoer til at styre objekter på skærmen, herunder navigation og andre muligheder.

## Kommandoer

* Control+NVDA+TAB: Skifter gennem tilstanden der benyttes ved brug af piletasterne(se nedenfor for detaljer).

## Piletasttilstande

Tilføjelsen giver fire måder at bruge piletasterne på:

* Klassisk (eller normal tilstand): Brug piletasterne til at flytte markøren.
* Objektnavigation: Brug piletasterne til at gå til næste, forrige, underordnede og overordnede objekter.
* Web: Brug piletasterne til at gennemse elementer og flytte mellem dem.
* Scanningstilstand: Brug piletasterne til at flytte gennem objekter på skærmen uanset hierarki.

Følgende kommandoer er tilgængelige med piletasterne indstillet til objektnavigation:

* Højre pil: Næste objekt.
* Venstre pil: Forrige objekt.
* Pil op: Overordnet objekt.
* Pil ned: Første underordnede objekt.
* Mellemrum eller ENTER: Aktivér.

Når webtilstand er aktiv, vil følgende kommandoer navigere mellem disse elementer på en side, med mindre denne er indstillet til normal (objekt, link, formularfelt, overskrift, ramme, tabel, liste, landmærke):

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

## ObjPad settings

In NVDA 2026.2, a dedicated setting is introduced to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
