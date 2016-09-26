# Object Arrows
# A global plugin for NVDA
# Copyright 2016 Joseph Lee, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table aNavigator.

import globalPluginHandler
import ui
from globalCommands import commands

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	objArrowMode = 0

	def script_toggleObjArrows(self, gesture):
		if self.objArrowMode == 0:
			self.objArrowMode = 1
			ui.message("Arrows will move between objects")
		elif self.objArrowMode == 1:
			self.objArrowMode = 2
			ui.message("Scan mode")
		else:
			self.objArrowMode = 0
			ui.message("Traditional object navigation mode")
		if 0 < self.objArrowMode <= 2:
			self.bindGesture("kb:rightarrow", "rightArrow")
			self.bindGesture("kb:leftarrow", "leftArrow")
			self.bindGesture("kb:downarrow", "downArrow")
			self.bindGesture("kb:uparrow", "upArrow")
			self.bindGesture("kb:space", "objActivate")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	def script_rightArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_next(gesture)
		elif self.objArrowMode == 2:
			commands.script_review_nextCharacter(gesture)

	def script_leftArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_previous(gesture)
		elif self.objArrowMode == 2:
			commands.script_review_previousCharacter(gesture)

	def script_downArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_firstChild(gesture)
		elif self.objArrowMode == 2:
			commands.script_navigatorObject_nextInFlow(gesture)

	def script_upArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_parent(gesture)
		elif self.objArrowMode == 2:
			commands.script_navigatorObject_previousInFlow(gesture)

	def script_objActivate(self, gesture):
		commands.script_review_activate(gesture)

	__gestures={
		"kb:control+NvDA+tab":"toggleObjArrows",
	}
