# ObjPad
# A global plugin for NVDA
# Copyright 2016-2026 Joseph Lee and others, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table Navigator.
# Scan mode comes from ideas in Narrator in Windows 10 Version 1607 and later.
# Web mode comes from Enhanced Touch Gestures.
# Parts of source code are enhanced implementations of NVDA Core commands (copyright NV Access).

from typing import NamedTuple
import globalPluginHandler
import ui
from globalCommands import commands, SCRCAT_OBJECTNAVIGATION
import browseMode
import api
import textInfos
import speech
import controlTypes
import enum
from scriptHandler import script
import addonHandler
addonHandler.initTranslation()

# Object navigation modes enumeration
class ObjPadMode(enum.IntEnum):
	NORMAL = 0  # Arrow keys are passed through the aplication
	OBJNAV = 1  # Arrow keys perform object navigation commands
	WEBBROWSE = 2  # Arrow keys move by web (browse mode ) elements
	SCANMODE = 3  # Arrow keys move through text across objects


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Object navigation arrow key mode (normal mode/object nav by default)
	objArrowMode = 0

	@script(
		# Translators: input help mode message for ObjPad toggle command.
		description=_("Toggles ObjPad mode between normal, object nav and scan modes"),
		category=SCRCAT_OBJECTNAVIGATION,
		gesture="kb:control+NvDA+tab"
	)
	def script_toggleObjPad(self, gesture):
		if self.objArrowMode == ObjPadMode.NORMAL:
			self.objArrowMode = ObjPadMode.OBJNAV
			# Translators: one of the object arrow modes.
			ui.message(_("Object nav mode"))
		elif self.objArrowMode == ObjPadMode.OBJNAV:
			self.objArrowMode = ObjPadMode.WEBBROWSE
			# Translators: one of the object arrow modes.
			ui.message(_("Browse mode"))
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			self.objArrowMode = ObjPadMode.SCANMODE
			# Translators: one of the object arrow modes.
			ui.message(_("Scan mode"))
		else:
			self.objArrowMode = ObjPadMode.NORMAL
			# Translators: one of the object arrow modes.
			ui.message(_("Normal mode"))
		if ObjPadMode.NORMAL < self.objArrowMode <= ObjPadMode.SCANMODE:
			self.bindGesture("kb:rightarrow", "rightArrow")
			self.bindGesture("kb:leftarrow", "leftArrow")
			self.bindGesture("kb:downarrow", "downArrow")
			self.bindGesture("kb:uparrow", "upArrow")
			self.bindGesture("kb:space", "objActivate")
			self.bindGesture("kb:enter", "objActivate")
			self.bindGesture("kb:numpadEnter", "objActivate")
			if self.objArrowMode == ObjPadMode.SCANMODE:
				self.bindGesture("kb:control+rightArrow", "controlRightArrow")
				self.bindGesture("kb:control+leftArrow", "controlLeftArrow")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Web navigation:

	# Web elements and associated scripts list:
	WebBrowseElement = NamedTuple(
		"WebBrowseElement", [
			("script", str),
			("element", str)
		]
	)
	webBrowseElements = (
		WebBrowseElement("", _("Default (all elements)")),
		WebBrowseElement("Link", _("Links")),
		WebBrowseElement("FormField", _("Form fields")),
		WebBrowseElement("Heading", _("Headings")),
		WebBrowseElement("Frame", _("Frames")),
		WebBrowseElement("Table", _("Tables")),
		WebBrowseElement("List", _("Lists")),
		WebBrowseElement("Landmark", _("Landmarks")),
		WebBrowseElement("EmbeddedObject", _("Embedded objects")),
		WebBrowseElement("TextParagraph", _("Text paragraphs")),
	)
	webBrowseMode = 0

	def script_rightArrow(self, gesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_next(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if (
				isinstance(
					(obj := api.getNavigatorObject().treeInterceptor),
					browseMode.BrowseModeTreeInterceptor
				) and self.webBrowseMode > 0  # An actual browse mode element
			):
				getattr(
					obj,
					f"script_next{self.webBrowseElements[self.webBrowseMode].script}"
				)(gesture)
			else:
				commands.script_navigatorObject_nextInFlow(gesture)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
			commands.script_review_nextCharacter(gesture)

	def script_leftArrow(self, gesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_previous(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if (
				isinstance(
					(obj := api.getNavigatorObject().treeInterceptor),
					browseMode.BrowseModeTreeInterceptor
			) and self.webBrowseMode > 0  # An actual browse mode element
			):
				getattr(
					obj,
					f"script_previous{self.webBrowseElements[self.webBrowseMode].script}"
				)(gesture)
			else:
				commands.script_navigatorObject_previousInFlow(gesture)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
			commands.script_review_previousCharacter(gesture)

	def script_controlRightArrow(self, gesture):
		commands.script_review_nextWord(gesture)

	def script_controlLeftArrow(self, gesture):
		commands.script_review_previousWord(gesture)

	# Modified global commands implementation to restrict movement to foreground elements.

	def script_downArrow(self, gesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_firstChild(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
			ui.message(self.webBrowseElements[self.webBrowseMode].element)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
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
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_parent(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
			ui.message(self.webBrowseElements[self.webBrowseMode].element)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
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
