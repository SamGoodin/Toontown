import sys

from direct.gui.DirectGui import *
from direct.showbase import DirectObject
from panda3d.core import Vec4
import Globals
from gui.ShtikerBook import ShtikerBook
from StartMenu import StartMenu
from hood.places.estate.Estate import Estate
from hood.places.TTC import TTC
from makeatoon import MakeAToon
from gui import FriendsList


class Messenger(DirectObject.DirectObject):

    def __init__(self):
        DirectObject.DirectObject.__init__(self)
        self.MAT = None
        self.startMenu = None
        self.toon = None
        self.toonName = None
        self.ttc = None
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

    @staticmethod
    def exit():
        sys.exit()

    def backToPlayground(self):
        if base.lastPlayground == Globals.TTCZone:
            ttc = TTC(self.toon)
            self.ttc = ttc.load(0)
            geom = self.toon.getGeomNode()
            geom.getChild(0).setSx(0.730000019073)
            geom.getChild(0).setSz(0.730000019073)

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
        self.enterGame()

    def enterGameFromStart(self):
        self.toon = base.toon.getToon()
        self.enterGame()

    def enterGame(self):
        base.camera.reparentTo(self.toon)
        self.toon.reparentTo(render)
        ttc = TTC(self.toon)
        self.ttc = ttc.load(0)
        geom = self.toon.getGeomNode()
        geom.getChild(0).setSx(0.730000019073)
        geom.getChild(0).setSz(0.730000019073)
        self.toon.setupCameraPositions()
        self.toon.setupControls()
        self.shtikerBook = ShtikerBook()
        self.laffMeter = self.toon.setupLaffMeter()
        friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
        friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
        friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
        newScale = oldScale = 0.8
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

