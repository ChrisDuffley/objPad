# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others
* Download [stable version][1]
* NVDA compatibility: 2022.4 and later

This add-on provides quick commands to manage objects on screen, including navigation and other possibilities.

## Commands

* Control+NVDA+TAB: Steps through arrow key modes (see below for details).

## Arrow key modes

The add-on provides four ways to use arrow keys:

* Classic (or normal mode): use arrow keys to move cursor.
* Object nav: use arrow keys to move to next/previous/parent/first child objects.
* Web: use arrow keys to cycle through elements and move between them.
* Scan mode: use arrow keys to move through objects on screen regardless of hierarchy.

The following commands are available with arrow keys set to object nav:

* Right arrow: next object.
* Left arrow: previous object.
* Up arrow: parent object.
* Down arrow: first child object.
* SPACE or ENTER: activate.

With web mode active (elements are normal or moving by object, link, form field, heading, frame, table, list, landmark):

* Right arrow: next element.
* Left arrow: previous element.
* Up arrow: previous element type.
* Down arrow: next element type.
* SPACE or ENTER: activate.

With scan mode active:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Right arrow: review next character.
* Left arrow: previous character.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.

## Version 22.06

* Requires NVDA 2021.3 or later.

## Version 21.04

* Requires NVDA 2020.1 or later.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.09

* Added localizations.
* Enter key (regular and Numpad) can be used to activate objects.

## Version 18.03

* Better compatibility with NVDA 2018.1.

## Version 16.12

* Added web mode.

## Version 16.10

* Initial stable version.

[1]: https://addons.nvda-project.org/files/get.php?file=objPad
