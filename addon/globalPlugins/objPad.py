# ObjPad
# A global plugin for NVDA
# Copyright 2016-2026 Joseph Lee and others, released under GPL

# Allows obj nav commands via arrow keys.
# Arrow key handling comes from Easy Table Navigator.
# Scan mode comes from ideas in Narrator in Windows 10 Version 1607 and later.
# Browse mode comes from Enhanced Touch Gestures.
# Parts of source code are enhanced implementations of NVDA Core commands (copyright NV Access).

import builtins
import globalPluginHandler
import ui
from globalCommands import commands, SCRCAT_OBJECTNAVIGATION
import browseMode
import touchHandler
import api
import textInfos
import speech
import controlTypes
import enum
import gui
import wx
from scriptHandler import script
import config
import inputCore
import addonHandler

# Some add-on messages are exact copies of NVDA Core (call the built-in gettext function).
# Pyright: ignore attribute access issue (builtins._ points to Gettext function in NVDA Core).
nvdaMessage = builtins._  # type: ignore
addonHandler.initTranslation()

# Object navigation modes enumeration
class ObjPadMode(enum.IntEnum):
	NORMAL = 0  # Arrow keys are passed through the aplication
	OBJNAV = 1  # Arrow keys perform object navigation commands
	WEBBROWSE = 2  # Arrow keys move by web (browse mode ) elements
	SCANMODE = 3  # Arrow keys move through text across objects


# Mode labels, used for mode change announcements and for the modes list in ObjPad settings.
OBJPAD_MODE_LABELS: dict[ObjPadMode, str] = {
	# Translators: one of the object arrow modes.
	ObjPadMode.NORMAL: _("Normal mode"),
	# Translators: one of the object arrow modes.
	ObjPadMode.OBJNAV: _("Object nav mode"),
	# Translators: one of the object arrow modes.
	ObjPadMode.WEBBROWSE: _("Browse mode"),
	# Translators: one of the object arrow modes.
	ObjPadMode.SCANMODE: _("Scan mode"),
}

# Modes which can be enabled or disabled (normal mode is always available).
# Modes are stored in config by enumeration member name so additional modes can be added later.
CONFIGURABLE_OBJPAD_MODES: list[ObjPadMode] = [mode for mode in ObjPadMode if mode != ObjPadMode.NORMAL]

config.conf.spec["objPad"] = {
	"modes": "string_list(default=list({}))".format(
		", ".join(f'"{mode.name}"' for mode in CONFIGURABLE_OBJPAD_MODES)
	),
}


def getEnabledObjPadModes() -> set[ObjPadMode]:
	enabledModeNames = set(config.conf["objPad"]["modes"])
	return {mode for mode in CONFIGURABLE_OBJPAD_MODES if mode.name in enabledModeNames}


class ObjPadPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: This is the label for the ObjPad settings panel.
	title = _("ObjPad")

	def makeSettings(self, settingsSizer: wx.BoxSizer):
		objPadHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		self._modesCheckListBox: gui.nvdaControls.CustomCheckListBox = objPadHelper.addLabeledControl(
			# Translators: label for the list of ObjPad modes to switch between in ObjPad settings.
			_("Select &navigation modes to cycle through:"),
			gui.nvdaControls.CustomCheckListBox,
			choices=[OBJPAD_MODE_LABELS[mode] for mode in CONFIGURABLE_OBJPAD_MODES],
		)
		enabledModes = getEnabledObjPadModes()
		for i, mode in enumerate(CONFIGURABLE_OBJPAD_MODES):
			self._modesCheckListBox.Check(i, mode in enabledModes)
		self._modesCheckListBox.Bind(wx.EVT_CHECKLISTBOX, self._onModesListChange)
		self._modesCheckListBox.SetSelection(0)

		# On touch capable computers, NVDA offers browse mode navigation elements setting
		# in browse mode settings.
		self._showBrowseModeElements = not touchHandler.touchSupported()
		if self._showBrowseModeElements:
			# Source: NVDA Core (2026.2)
			# Store element types for use in onSave (excludes the always-active "default" entry).
			self._browseModeElements = list(browseMode.BrowseModeTreeInterceptor._browseTouchNavRegistry)
			self._browseModeCheckListBox: gui.nvdaControls.CustomCheckListBox
			self._browseModeCheckListBox = objPadHelper.addLabeledControl(
				nvdaMessage("&Browse mode navigation elements:"),
				gui.nvdaControls.CustomCheckListBox,
				choices=[label for _itemType, label in self._browseModeElements],
			)
			enabledTypes = set(config.conf["virtualBuffers"]["browseModeTouchNavigationElements"])
			for i, (itemType, _label) in enumerate(self._browseModeElements):
				self._browseModeCheckListBox.Check(i, itemType in enabledTypes)

	def _noModesSelectedMessage(self) -> str:
		# Translators: message shown when no ObjPad mode is selected in ObjPad settings.
		return _(
			"At least one ObjPad mode must be selected in order to switch from normal mode to another mode."
		)

	def _onModesListChange(self, evt: wx.CommandEvent):
		# Source: NVDA Core (speech modes list in voice settings)
		# Continue event propagation so the user is notified about the item being checked or unchecked.
		evt.Skip()
		if not self._modesCheckListBox.CheckedItems:
			gui.messageBox(
				self._noModesSelectedMessage(),
				# Translators: title of the warning shown when all ObjPad modes are unchecked
				# in ObjPad settings.
				_("Warning"),
				wx.OK | wx.ICON_WARNING,
				self,
			)
			# Check the mode again so ObjPad can still switch from normal mode to another mode.
			self._modesCheckListBox.Check(evt.GetInt(), True)

	def isValid(self) -> bool:
		if not self._modesCheckListBox.CheckedItems:
			self._validationErrorMessageBox(
				message=self._noModesSelectedMessage(),
				# Translators: Same as the label for the list of ObjPad modes in ObjPad settings,
				# but without keyboard accelerator (& character) nor final colon.
				option=_("Select navigation modes to cycle through"),
			)
			self._modesCheckListBox.SetFocus()
			return False
		return super().isValid()

	def onSave(self):
		config.conf["objPad"]["modes"] = [
			mode.name
			for i, mode in enumerate(CONFIGURABLE_OBJPAD_MODES)
			if self._modesCheckListBox.IsChecked(i)
		]
		if self._showBrowseModeElements:
			config.conf["virtualBuffers"]["browseModeTouchNavigationElements"] = [
				itemType
				for i, (itemType, _label) in enumerate(self._browseModeElements)
				if self._browseModeCheckListBox.IsChecked(i)
			]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Object navigation arrow key mode (normal mode/object nav by default)
	objArrowMode: ObjPadMode = ObjPadMode.NORMAL

	def __init__(self):
		super().__init__()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(ObjPadPanel)

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(ObjPadPanel)

	@script(
		# Translators: input help mode message for ObjPad toggle command.
		description=_("Switches between normal mode and ObjPad modes selected in ObjPad settings"),
		category=SCRCAT_OBJECTNAVIGATION,
		gesture="kb:control+NvDA+tab"
	)
	def script_toggleObjPad(self, gesture: inputCore.InputGesture):
		self.objArrowMode = self._nextObjPadMode()
		ui.message(OBJPAD_MODE_LABELS[self.objArrowMode])
		self._bindObjPadModeGestures()

	def _nextObjPadMode(self) -> ObjPadMode:
		# Move to the next enabled mode, wrapping around to normal mode (which is always available).
		modes = list(ObjPadMode)
		enabledModes = getEnabledObjPadModes()
		modeIndex = modes.index(ObjPadMode(self.objArrowMode))
		for offset in range(1, len(modes) + 1):
			mode = modes[(modeIndex + offset) % len(modes)]
			if mode == ObjPadMode.NORMAL or mode in enabledModes:
				return mode
		return ObjPadMode.NORMAL

	def _bindObjPadModeGestures(self):
		# Start from static gestures so mode-specific gestures (such as scan mode ones) do not linger.
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		if self.objArrowMode == ObjPadMode.NORMAL:
			return
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

	def script_rightArrow(self, gesture: inputCore.InputGesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_next(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if api.getNavigatorObject().treeInterceptor:
				api.getNavigatorObject().treeInterceptor.script_nextSelectedElement(gesture)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
			commands.script_review_nextCharacter(gesture)

	def script_leftArrow(self, gesture: inputCore.InputGesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_previous(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if api.getNavigatorObject().treeInterceptor:
				api.getNavigatorObject().treeInterceptor.script_prevSelectedElement(gesture)
		elif self.objArrowMode == ObjPadMode.SCANMODE:
			commands.script_review_previousCharacter(gesture)

	def script_controlRightArrow(self, gesture: inputCore.InputGesture):
		commands.script_review_nextWord(gesture)

	def script_controlLeftArrow(self, gesture: inputCore.InputGesture):
		commands.script_review_previousWord(gesture)

	# Modified global commands implementation to restrict movement to foreground elements.

	def script_downArrow(self, gesture: inputCore.InputGesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_firstChild(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if api.getNavigatorObject().treeInterceptor:
				api.getNavigatorObject().treeInterceptor.script_nextBrowseElement(gesture)
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
					ui.reviewMessage(nvdaMessage("No next"))

	def script_upArrow(self, gesture: inputCore.InputGesture):
		if self.objArrowMode == ObjPadMode.OBJNAV:
			commands.script_navigatorObject_parent(gesture)
		elif self.objArrowMode == ObjPadMode.WEBBROWSE:
			if api.getNavigatorObject().treeInterceptor:
				api.getNavigatorObject().treeInterceptor.script_prevBrowseElement(gesture)
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
					ui.reviewMessage(nvdaMessage("No previous"))

	def script_objActivate(self, gesture: inputCore.InputGesture):
		commands.script_review_activate(gesture)
