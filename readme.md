# ObjPad #

* Author: Joseph Lee, Cleverson Uliana and others
* Download [stable version][1]
* Download [development version][2]

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

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev
