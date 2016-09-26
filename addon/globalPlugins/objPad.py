# Object Arrows
# A global plugin for NVDA
# Copyright 2016 Joseph Lee, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table aNavigator.

import globalPluginHandler
import ui
from globalCommands import commands

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	objArrowMode = False

	def script_toggleObjArrows(self, gesture):
		if not self.objArrowMode:
			self.objArrowMode = True
			self.bindGesture("kb:rightarrow", "objNext")
			self.bindGesture("kb:leftarrow", "objPrev")
			self.bindGesture("kb:downarrow", "objFirstChild")
			self.bindGesture("kb:uparrow", "objParent")
			self.bindGesture("kb:space", "objActivate")
			ui.message("Arrows will move between objects")
		else:
			self.objArrowMode = False
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)
			ui.message("Traditional object navigation mode")

	def script_objNext(self, gesture):
		commands.script_navigatorObject_next(gesture)

	def script_objPrev(self, gesture):
		commands.script_navigatorObject_previous(gesture)

	def script_objFirstChild(self, gesture):
		commands.script_navigatorObject_firstChild(gesture)

	def script_objParent(self, gesture):
		commands.script_navigatorObject_parent(gesture)

	def script_objActivate(self, gesture):
		commands.script_review_activate(gesture)

	__gestures={
		"kb:control+NvDA+tab":"toggleObjArrows",
	}
