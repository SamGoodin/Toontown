import sys

from direct.gui.DirectGui import *
from direct.showbase import DirectObject

import Globals
from gui.ShtikerBook import ShtikerBook
from StartMenu import StartMenu
from hood.places.estate.Estate import Estate
from hood.places.TTC import TTC
from makeatoon import MakeAToon


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

    @staticmethod
    def exit():
        sys.exit()

    def enterMakeAToon(self):
        self.MAT = MakeAToon.MakeAToon()
        self.MAT.enterMakeAToon()

    def enterStartMenu(self):
        self.startMenu = StartMenu()
        self.startMenu.loadStartMenu()

    def unloadMakeAToon(self):
        self.toon = self.MAT.getToon()
        base.toon = self.toon
        self.MAT.exit()
        self.MAT.unload()
        base.marginManager.clearMargins()
        del self.MAT
        ttc = TTC(self.toon)
        self.ttc = ttc.load(0)
        geom = self.toon.getGeomNode()
        geom.getChild(0).setSx(0.730000019073)
        geom.getChild(0).setSz(0.730000019073)
        base.camera.reparentTo(self.toon)
        base.toon.setupCameraPositions()
        base.toon.setupControls()
        self.shtikerBook = ShtikerBook()

    def loadEstate(self):
        self.estate = Estate().load()


