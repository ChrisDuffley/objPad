# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Perform various NVDA object commands by pressing a single key, including navigation and more.

## Commands

* Control+NVDA+TAB: cycles through the navigation modes selected in ObjPad settings (see below for details).

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

With browse mode active (elements are default (moving by object/all elements), heading, table, link, form field, list; additional browse mode elements can be added via NVDA's browse mode settings or from a dedicated ObjPad settings interface (see below)):

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

## ObjPad settings

ObjPad settings (part of NVDA settings screen) include the following settings:

* Navigation Modes to Cycle Through: choose which modes (object nav, browse mode, scan mode) Control+NVDA+TAB cycles through. Normal mode is always included. All modes are selected by default. At least one mode must stay selected; if you uncheck the last one, ObjPad warns you and keeps it checked.
* Browse mode navigation elements: choose which elements browse mode moves between. ObjPad shows this setting only on computers without a touchscreen and in portable copies of NVDA; otherwise, it's in NVDA's own browse mode settings.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
