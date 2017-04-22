import sys
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase import DirectObject
from panda3d.core import Vec4
import Globals
from gui.ShtikerBook import ShtikerBook
from StartMenu import StartMenu
from hood.places.estate.Estate import Estate
from hood.places.ToontownCentral import TTC
from hood.places.DonaldsDock import DDock
from hood.places.DaisyGardens import DG
from hood.places.MinniesMelodyland import MM
from hood.places.Brrrgh import Brrrgh
from hood.places.DonaldsDreamland import Dreamland
from hood.places.GoofySpeedway import GoofySpeedway
from hood.places.OutdoorZone import OutdoorZone
from makeatoon import MakeAToon
from gui import FriendsList


class Messenger(DirectObject.DirectObject):

    def __init__(self):
        DirectObject.DirectObject.__init__(self)
        self.MAT = None
        self.startMenu = None
        self.toon = None
        self.toonName = None
        self.playground = None
        self.accept('exit', self.exit)
        self.accept('enterMAT', self.enterMakeAToon)
        self.accept('StartMenu', self.enterStartMenu)
        self.accept('exitMakeAToon', self.unloadMakeAToon)
        self.accept('loadEstate', self.loadEstate)
        self.accept('enterGameFromStart', self.enterGameFromStart)
        self.accept('closeFriendsList', self.closeFriendsList)
        self.accept('hideAllGui', self.hideAllGui)
        self.accept('showAllGui', self.showAllGui)
        self.accept('enableGui', self.enableGui)
        self.accept('disableGui', self.disableGui)
        self.accept('backToPlayground', self.backToPlayground)
        self.accept('showFriendsListButton', self.showFriendsListButton)
        self.accept('hideFriendsListButton', self.hideFriendsListButton)
        self.accept('teleportIn', self.teleportInSequence)
        self.accept('loadTTC', self.loadTTC)
        self.accept('loadDock', self.loadDock)
        self.accept('loadGardens', self.loadGardens)
        self.accept('loadMelody', self.loadMelody)
        self.accept('loadBrrrgh', self.loadBrrrgh)
        self.accept('loadDreamland', self.loadDreamland)
        self.accept('loadSpeedway', self.loadSpeedway)
        self.accept('loadOutdoorZone', self.loadOutdoorZone)

    @staticmethod
    def exit():
        sys.exit()

    def loadTTC(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        ttc = TTC(self.toon, startPosHpr)
        self.playground = ttc.load()

    def loadDock(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        dock = DDock(self.toon, startPosHpr)
        self.playground = dock.load()

    def loadGardens(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        gardens = DG(self.toon, startPosHpr)
        self.playground = gardens.load()

    def loadMelody(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        melody = MM(self.toon, startPosHpr)
        self.playground = melody.load()

    def loadBrrrgh(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        brrrgh = Brrrgh(self.toon, startPosHpr)
        self.playground = brrrgh.load()

    def loadDreamland(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        dream = Dreamland(self.toon, startPosHpr)
        self.playground = dream.load()

    def loadSpeedway(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        speedway = GoofySpeedway(self.toon, startPosHpr)
        self.playground = speedway.load()

    def loadOutdoorZone(self, startPosHpr=None):
        if not startPosHpr:
            startPosHpr = 1
        outdoorzone = OutdoorZone(self.toon, startPosHpr)
        self.playground = outdoorzone.load()

    def backToPlayground(self):
        if base.lastPlayground == Globals.TTCZone:
            self.loadTTC()
        elif base.lastPlayground == Globals.DDZone:
            self.loadDock()
        elif base.lastPlayground == Globals.DGZone:
            self.loadGardens()
        elif base.lastPlayground == Globals.MMZone:
            self.loadMelody()
        elif base.lastPlayground == Globals.BRZone:
            self.loadBrrrgh()
        elif base.lastPlayground == Globals.DLZone:
            self.loadDreamland()
        elif base.lastPlayground == Globals.GSZone:
            self.loadSpeedway()
        elif base.lastPlayground == Globals.OZZone:
            self.loadOutdoorZone()

    def enterMakeAToon(self):
        self.MAT = MakeAToon.MakeAToon()
        self.MAT.enterMakeAToon()

    def enterStartMenu(self):
        self.startMenu = StartMenu()
        self.startMenu.loadStartMenu()

    def unloadMakeAToon(self):
        self.toon = self.MAT.getToon()
        self.toon.setData()
        base.toon = self.toon
        self.MAT.exit()
        self.MAT.unload()
        base.marginManager.clearMargins()
        del self.MAT
        self.enterGameTrack()

    def enterGameFromStart(self):
        self.toon = base.toon.getToon()
        self.enterGameTrack()

    def enterGameTrack(self):
        self.enterGame()
        #self.teleportInSequence()

    def teleportInSequence(self):
        self.teleportInTrack = Sequence(Func(self.toon.enterTeleportIn), Wait(2), Func(self.toon.exitTeleportIn),
                 Func(self.toon.enterNeutral))
        self.teleportInTrack.start()
        self.teleportInTrack.setAutoFinish(True)

    def enterGame(self):
        base.lastPlayground = base.localData.getLastPlayground()
        self.backToPlayground()
        base.camera.reparentTo(self.toon)
        self.toon.reparentTo(render)
        self.toon.initializeBodyCollisions()
        self.toon.initializeDropShadow()
        self.toon.initializeNametag3d()
        self.toon.rescaleToon()
        self.toon.setActiveShadow(1)
        self.toon.rescaleToon()
        self.toon.initializeSmartCamera()
        self.toon.setupControls()
        base.localAvatar = self.toon
        self.shtikerBook = ShtikerBook()
        self.laffMeter = self.toon.setupLaffMeter()
        friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
        friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
        friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
        newScale = 0.8
        self.bFriendsList = DirectButton(image=(friendsButtonNormal, friendsButtonPressed, friendsButtonRollover),
                                         relief=None, pos=(-0.141, 0, -0.125), parent=base.a2dTopRight, scale=newScale,
                                         text=('', 'Friends', 'Friends'),
                                         text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1),
                                         text_pos=(0, -0.18), text_font=Globals.getInterfaceFont(),
                                         command=self.openFriendsList)
        self.friendsListButtonActive = 0
        self.friendsListButtonObscured = 0
        friendsGui.removeNode()

    def loadEstate(self):
        self.estate = Estate().load()

    def hideFriendsListButton(self):
        self.bFriendsList.hide()

    def showFriendsListButton(self):
        self.bFriendsList.show()

    def openFriendsList(self):
        self.friendsList = FriendsList.showFriendsList()
        self.bFriendsList.hide()

    def closeFriendsList(self):
        self.friendsList = FriendsList.hideFriendsList()
        self.bFriendsList.show()

    def hideAllGui(self):
        self.friendsList = FriendsList.hideFriendsList()
        self.bFriendsList.hide()
        self.shtikerBook.hideOpenClose()

    def showAllGui(self):
        self.closeFriendsList()
        self.shtikerBook.showOpenClose()

    def disableGui(self):
        self.shtikerBook.disable()
        self.bFriendsList['state'] = DGG.DISABLED

    def enableGui(self):
        self.shtikerBook.enable()
        self.bFriendsList['state'] = DGG.NORMAL

