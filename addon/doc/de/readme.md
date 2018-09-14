# ObjPad #

* Autoren: Joseph Lee, Cleverson Uliana und andere
* [stabile version][1] herunterladen
* [Testversion herunterladen][2]

Dieses Add-on bietet schnelle Befehle zur Verwaltung von Objekten auf dem
Bildschirm, einschließlich Navigation und anderer Möglichkeiten.

## Befehle

* STRG+NVDA+TAB: wechselt zwischen den Navigationsarten auf dem Bildschirm
  (Details siehe unten).

## Navigationsarten

Die Erweiterung bietet vier Möglichkeiten der Navigation mit Pfeiltasten:

* Klassisch (oder Normalmodus): Verwenden Sie die Pfeiltasten, um den Cursor
  zu steuern.
* Objektnavigation: Benutzen Sie die Pfeiltasten, um zu den
  nächsten/vorherigen Hauptobjekten bzw. ersten/vorherigen/nächsten
  Unterobjekten zu gelangen.
* Web: Benutzen Sie die Pfeiltasten, um durch die Elementtypen zu blättern
  und sich zwischen elementen zu bewegen.
* Scan-Modus: Benutzen Sie die Pfeiltasten, um unabhängig von der Hierarchie
  durch die Objekte auf dem Bildschirm zu navigieren.

Die folgenden Befehle sind verfügbar, wenn die Pfeiltasten auf
Objektnavigation eingestellt sind:

* Rechtspfeil: nächstes Objekt.
* Linkspfeil: vorheriges Objekt.
* Pfeil nach oben: Hauptobjekt für die aktuelle Region.
* Pfeil nach unten: erstes Unterobjekt des Hauptobjektes.
* SPACE or ENTER: activate.

Elemente können im Webmodus normal eingestellt werden. Sie können aber auch
zwischen den Elementtypen Objekte, Links, Formularfelder, Überschriften,
Rahmen, Tabellen, Listen, Sprungmarken navigieren:

* Rechtspfeil: nächstes Element.
* Linkspfeil: vorheriges Element
* Pfeil nach oben: vorheriges Elementtyp.
* Pfeil nach unten: nächstes Elementtyp.
* SPACE or ENTER: activate.

Bei aktiviertem Scan-Modus:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Rechtspfeil: nächster Buchstabe.
* Linkspfeil: vorheriger Buchstabe.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

## Version 18.09

* Added localizations.
* Enter key (regular and Numpad) can be used to activate objects.

## Version 18.03

* Bessere Kompatibilität mit NVDA 2018.1.

## Version 16.12

* Web-Modus wurde hinzugefügt.

## Version 16.10

* Ehrstveröffentlichung der stabilen Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev
