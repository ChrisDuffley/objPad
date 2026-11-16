# objPad/installTasks.py
# Copyright 2026 Joseph Lee, released under GPL.

# Registers add-on config spec/settings blueprint.

import config

def onInstall() -> None:
	# Register this add-on's settings with NVDA's configuration system.
	# The global plugin main module version serves as a fallback in case custom sections data is gone.
	# Spell out the default modes list.
	confspec = {
		"modes": "string_list(default=list('OBJNAV', 'WEBBROWSE', 'SCANMODE'))"
	}
	config.configSections.registerSection("objPad", confspec, isBaseOnly=True)
