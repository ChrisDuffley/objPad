# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

This add-on provides quick commands to manage objects on screen, including navigation and other possibilities.

## Commands

* Control+NVDA+TAB: Steps through arrow key modes (see below for details).

## Arrow key modes

The add-on provides four ways to use arrow keys:

* Classic (or normal mode): use arrow keys to move cursor.
* Object nav: use arrow keys to move to next/previous/parent/first child objects.
* Browse mode: use arrow keys to cycle through browse mode elements (web included) and move between them.
* Scan mode: use arrow keys to move through objects on screen regardless of hierarchy.

The following commands are available with arrow keys set to object nav:

* Right arrow: next object.
* Left arrow: previous object.
* Up arrow: parent object.
* Down arrow: first child object.
* SPACE or ENTER: activate.

With browse mode active (elements are default (moving by object/all elements), heading, table, link, form field, list):

* Right arrow: next element.
* Left arrow: previous element.
* Up arrow: previous element type.
* Down arrow: next element type.
* SPACE or ENTER: activate.

Notes:

* In NVDA 2025.3.3 and 2026.1, additional browse mode elements include frame, graphic, landmark, embedded object, and text paragraph.
* In NVDA 2026.2 running on a touchscreen computer, additional browse mode elements can be added via NVDA's browse mode settings.

With scan mode active:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Right arrow: review next character.
* Left arrow: previous character.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
