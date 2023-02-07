# ObjPad
# A global plugin for NVDA
# Copyright 2016-2023 Joseph Lee and others, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table Navigator.
# Scan mode comes from ideas in Narrator in Windows 10 Version 1607 and later.
# Web mode comes from Enhanced Touch Gestures.
# Parts of source code are enhanced implementations of NVDA Core commands (copyright NV Access).

import globalPluginHandler
import ui
from globalCommands import commands, SCRCAT_OBJECTNAVIGATION
import browseMode
import api
import textInfos
import speech
import controlTypes
from scriptHandler import script
import addonHandler
addonHandler.initTranslation()

MODE_NORMAL = 0
MODE_OBJNAV = 1
MODE_WEB = 2
MODE_SCANMODE = 3


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	objArrowMode = 0

	@script(
		# Translators: input help mode message for ObjPad toggle command.
		description=_("Toggles ObjPad mode between normal, object nav and scan modes"),
		category=SCRCAT_OBJECTNAVIGATION,
		gesture="kb:control+NvDA+tab"
	)
	def script_toggleObjPad(self, gesture):
		if self.objArrowMode == MODE_NORMAL:
			self.objArrowMode = MODE_OBJNAV
			# Translators: one of the object arrow modes.
			ui.message(_("Object nav mode"))
		elif self.objArrowMode == MODE_OBJNAV:
			self.objArrowMode = MODE_WEB
			# Translators: one of the object arrow modes.
			ui.message(_("Web mode"))
		elif self.objArrowMode == MODE_WEB:
			self.objArrowMode = MODE_SCANMODE
			# Translators: one of the object arrow modes.
			ui.message(_("Scan mode"))
		else:
			self.objArrowMode = MODE_NORMAL
			# Translators: one of the object arrow modes.
			ui.message(_("Normal mode"))
		if MODE_NORMAL < self.objArrowMode <= MODE_SCANMODE:
			self.bindGesture("kb:rightarrow", "rightArrow")
			self.bindGesture("kb:leftarrow", "leftArrow")
			self.bindGesture("kb:downarrow", "downArrow")
			self.bindGesture("kb:uparrow", "upArrow")
			self.bindGesture("kb:space", "objActivate")
			self.bindGesture("kb:enter", "objActivate")
			self.bindGesture("kb:numpadEnter", "objActivate")
			if self.objArrowMode == MODE_SCANMODE:
				self.bindGesture("kb:control+rightArrow", "controlRightArrow")
				self.bindGesture("kb:control+leftArrow", "controlLeftArrow")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Web navigation:

	# Web elements list:
	webBrowseElements = (
		_("normal"), _("Link"), _("Form field"), _("Heading"), _("Frame"), _("Table"), _("List"), _("Landmark")
	)
	webBrowseMode = 0

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands = (
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLink,
			browseMode.BrowseModeTreeInterceptor.script_previousLink
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFormField,
			browseMode.BrowseModeTreeInterceptor.script_previousFormField
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextHeading,
			browseMode.BrowseModeTreeInterceptor.script_previousHeading
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFrame,
			browseMode.BrowseModeTreeInterceptor.script_previousFrame
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextTable,
			browseMode.BrowseModeTreeInterceptor.script_previousTable
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextList,
			browseMode.BrowseModeTreeInterceptor.script_previousList
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLandmark,
			browseMode.BrowseModeTreeInterceptor.script_previousLandmark
		),
	)

	def script_rightArrow(self, gesture):
		if self.objArrowMode == MODE_OBJNAV:
			commands.script_navigatorObject_next(gesture)
		elif self.objArrowMode == MODE_WEB:
			obj = api.getNavigatorObject().treeInterceptor
			if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
				if self.webBrowseMode == 0:
					commands.script_navigatorObject_nextInFlow(gesture)
				else:
					self.browseModeCommands[self.webBrowseMode - 1][0](obj, gesture)
			else:
				commands.script_navigatorObject_nextInFlow(gesture)
		elif self.objArrowMode == MODE_SCANMODE:
			commands.script_review_nextCharacter(gesture)

	def script_leftArrow(self, gesture):
		if self.objArrowMode == MODE_OBJNAV:
			commands.script_navigatorObject_previous(gesture)
		elif self.objArrowMode == MODE_WEB:
			obj = api.getNavigatorObject().treeInterceptor
			if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
				if self.webBrowseMode == 0:
					commands.script_navigatorObject_previousInFlow(gesture)
				else:
					self.browseModeCommands[self.webBrowseMode - 1][1](obj, gesture)
			else:
				commands.script_navigatorObject_previousInFlow(gesture)
		elif self.objArrowMode == MODE_SCANMODE:
			commands.script_review_previousCharacter(gesture)

	def script_controlRightArrow(self, gesture):
		commands.script_review_nextWord(gesture)

	def script_controlLeftArrow(self, gesture):
		commands.script_review_previousWord(gesture)

	# Modified global commands implementation to restrict movement to foreground elements.

	def script_downArrow(self, gesture):
		if self.objArrowMode == MODE_OBJNAV:
			commands.script_navigatorObject_firstChild(gesture)
		elif self.objArrowMode == MODE_WEB:
			self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
			ui.message(self.webBrowseElements[self.webBrowseMode])
		elif self.objArrowMode == MODE_SCANMODE:
			# Navigate to next line if possible.
			info = api.getReviewPosition().copy()
			info.expand(textInfos.UNIT_LINE)
			info.collapse()
			res = info.move(textInfos.UNIT_LINE, 1)
			if res != 0:
				api.setReviewPosition(info)
				info.expand(textInfos.UNIT_LINE)
				speech.speakTextInfo(info, unit=textInfos.UNIT_LINE, reason=controlTypes.OutputReason.CARET)
			else:
				curObject = api.getNavigatorObject()
				newObject = None
				if curObject.simpleFirstChild:
					newObject = curObject.simpleFirstChild
				elif curObject.simpleNext:
					newObject = curObject.simpleNext
				elif curObject.simpleParent:
					parent = curObject.simpleParent
					while parent and not parent.simpleNext:
						parent = parent.simpleParent
					# As long as one is on current foreground object...
					# Stay within the current top-level window.
					if parent and parent.simpleParent != api.getDesktopObject():
						newObject = parent.simpleNext
				if newObject:
					api.setNavigatorObject(newObject)
					speech.speakObject(newObject, reason=controlTypes.OutputReason.FOCUS)
				else:
					# Translators: a message when there is no next object when navigating
					ui.reviewMessage(_("No next"))

	def script_upArrow(self, gesture):
		if self.objArrowMode == MODE_OBJNAV:
			commands.script_navigatorObject_parent(gesture)
		elif self.objArrowMode == MODE_WEB:
			self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
			ui.message(self.webBrowseElements[self.webBrowseMode])
		elif self.objArrowMode == MODE_SCANMODE:
			# Move to previous line first so text can be reviewed before resorting to a new object.
			info = api.getReviewPosition().copy()
			info.expand(textInfos.UNIT_LINE)
			info.collapse()
			res = info.move(textInfos.UNIT_LINE, -1)
			if res != 0:
				api.setReviewPosition(info)
				info.expand(textInfos.UNIT_LINE)
				speech.speakTextInfo(info, unit=textInfos.UNIT_LINE, reason=controlTypes.OutputReason.CARET)
			else:
				# Do not move outside of the current window.
				curObject = api.getNavigatorObject()
				newObject = None
				if curObject.parent != api.getDesktopObject():
					newObject = curObject.simplePrevious
					if newObject:
						while newObject.simpleLastChild:
							newObject = newObject.simpleLastChild
					else:
						newObject = curObject.simpleParent
				if newObject:
					api.setNavigatorObject(newObject)
					speech.speakObject(newObject, reason=controlTypes.OutputReason.FOCUS)
				else:
					# Translators: a message when there is no previous object when navigating
					ui.reviewMessage(_("No previous"))

	def script_objActivate(self, gesture):
		commands.script_review_activate(gesture)
