# ObjPad
# A global plugin for NVDA
# Copyright 2016 Joseph Lee, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table Navigator.
# Scan mode comes from ideas in Narrator in Windows 10 Version 1607.

import globalPluginHandler
import ui
from globalCommands import commands
import api
import textInfos
import speech
import controlTypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	objArrowMode = 0

	def script_toggleObjArrows(self, gesture):
		if self.objArrowMode == 0:
			self.objArrowMode = 1
			ui.message("Object nav mode")
		elif self.objArrowMode == 1:
			self.objArrowMode = 2
			ui.message("Scan mode")
		else:
			self.objArrowMode = 0
			ui.message("Normal mode")
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

	# Modified global commands implementation to restrict movement to foreground elements.

	def script_downArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_firstChild(gesture)
		elif self.objArrowMode == 2:
			curObject=api.getNavigatorObject()
			newObject=None
			if curObject.simpleFirstChild:
				newObject=curObject.simpleFirstChild
			elif curObject.simpleNext:
				newObject=curObject.simpleNext
			elif curObject.simpleParent:
				parent=curObject.simpleParent
				while parent and not parent.simpleNext:
					parent=parent.simpleParent
				# As long as one is on current foreground object...
				if parent and parent.simpleParent != api.getDesktopObject():
					newObject=parent.simpleNext
			if newObject:
				api.setNavigatorObject(newObject)
				speech.speakObject(newObject,reason=controlTypes.REASON_FOCUS)
			else:
				# Translators: a message when there is no next object when navigating
				ui.reviewMessage(_("No next"))

	def script_upArrow(self, gesture):
		if self.objArrowMode == 1:
			commands.script_navigatorObject_parent(gesture)
		elif self.objArrowMode == 2:
			# Do not move outside of the current window.
			curObject=api.getNavigatorObject()
			newObject=None
			if curObject.parent != api.getDesktopObject():
				newObject=curObject.simplePrevious
				if newObject:
					while newObject.simpleLastChild:
						newObject=newObject.simpleLastChild
				else:
					newObject=curObject.simpleParent
			if newObject:
				api.setNavigatorObject(newObject)
				speech.speakObject(newObject,reason=controlTypes.REASON_FOCUS)
			else:
				# Translators: a message when there is no previous object when navigating
				ui.reviewMessage(_("No previous"))

	def script_objActivate(self, gesture):
		commands.script_review_activate(gesture)

	__gestures={
		"kb:control+NvDA+tab":"toggleObjArrows",
	}
