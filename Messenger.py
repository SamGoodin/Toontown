import sys
from direct.showbase import DirectObject
import MakeAToon
from StartMenu import StartMenu
from TTC import TTC
import Toon
from LoadingScreen import LoadingScreen
from direct.gui.DirectGui import *
import Globals


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
        self.MAT.exit()
        self.MAT.unload()
        del self.MAT
        ttc = TTC(self.toon)
        ttc.load(0)
        geom = self.toon.getGeomNode()
        geom.getChild(0).setSx(0.730000019073)
        geom.getChild(0).setSz(0.730000019073)
        base.camera.reparentTo(self.toon)
        self.toonClass = Toon.Toon()
        self.toonClass.setupCameraPositions()
        self.toon = self.toonClass.setupControls(self.toon)
        self.shtikerBook()

    def shtikerBook(self):
        self.book = DirectFrame()
        model = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        self.book['image'] = model.find('**/big_book')
        self.book['image_scale'] = (2, 1, 1.5)
        self.book.resetFrameSize()
        self.bookOpenButton = DirectButton(image=(
        model.find('**/BookIcon_CLSD'), model.find('**/BookIcon_OPEN'), model.find('**/BookIcon_RLVR')),
                                           relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305,
                                           command=self.openBook)
        self.bookCloseButton = DirectButton(image=(
        model.find('**/BookIcon_OPEN'), model.find('**/BookIcon_CLSD'), model.find('**/BookIcon_RLVR2')),
                                            relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305,
                                            command=self.closeBook)
        self.bookOpenButton.show()
        self.bookCloseButton.hide()
        self.nextArrow = DirectButton(parent=self.book, relief=None, image=(
        model.find('**/arrow_button'), model.find('**/arrow_down'), model.find('**/arrow_rollover')),
                                      scale=(0.1, 0.1, 0.1), pos=(0.838, 0, -0.661))
        self.prevArrow = DirectButton(parent=self.book, relief=None, image=(
        model.find('**/arrow_button'), model.find('**/arrow_down'), model.find('**/arrow_rollover')),
                                      scale=(-0.1, 0.1, 0.1), pos=(-0.838, 0, -0.661))
        model.removeNode()
        self.openSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.ogg')
        self.closeSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.ogg')
        self.pageSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.ogg')
        self.book.hide()

    def openBook(self):
        base.playSfx(self.openSound)
        base.render.hide()
        base.setBackgroundColor(0.05, 0.15, 0.4)
        self.book.show()
        self.bookOpenButton.hide()
        self.bookCloseButton.show()

    def closeBook(self):
        base.playSfx(self.closeSound)
        base.render.show()
        base.setBackgroundColor(Globals.defaultBackgroundColor)
        self.book.hide()
        self.bookOpenButton.show()
        self.bookCloseButton.hide()