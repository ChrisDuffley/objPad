# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Perform various NVDA object commands by pressing a single key, including navigation and more.

## Commands

* Control+NVDA+TAB: Steps through arrow key modes selected in ObjPad settings (see below for details).

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

* Navigation Modes to Cycle Through: choose which arrow key modes (object nav, browse mode, scan mode) Control+NVDA+TAB switches between. Normal mode is always available. By default, all modes are selected. At least one mode must be selected.
* Browse mode navigation elements (non-touch devices and portable NVDA versions only): see below.

NVDA includes a dedicated setting to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
