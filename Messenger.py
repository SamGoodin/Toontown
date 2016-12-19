import sys

from direct.gui.DirectGui import *
from direct.showbase import DirectObject

import Globals
from Toon import Toon
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
        self.ttc = ttc.load(0)
        geom = self.toon.getGeomNode()
        geom.getChild(0).setSx(0.730000019073)
        geom.getChild(0).setSz(0.730000019073)
        base.camera.reparentTo(self.toon)
        self.toonClass = Toon()
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
        mapModel = loader.loadModel('phase_3.5/models/gui/toontown_map')
        self.map = DirectFrame(relief=None, image=mapModel.find('**/toontown_map'),
                               image_scale=(1.8, 1, 1.35), scale=0.97, pos=(0, 0, 0.0775))
        mapModel.removeNode()
        self.cloudScaleList = (((0.55, 0, 0.4), (0.35, 0, 0.25)),
                               (),
                               ((0.45, 0, 0.45), (0.5, 0, 0.4)),
                               ((0.7, 0, 0.45),),
                               ((0.55, 0, 0.4),),
                               ((0.6, 0, 0.4), (0.5332, 0, 0.32)),
                               ((0.7, 0, 0.45), (0.7, 0, 0.45)),
                               ((0.7998, 0, 0.39),),
                               ((0.5, 0, 0.4),),
                               ((-0.45, 0, 0.4),),
                               ((-0.45, 0, 0.35),),
                               ((0.5, 0, 0.35),),
                               ((0.5, 0, 0.35),))
        self.cloudPosList = (((0.575, 0.0, -0.04), (0.45, 0.0, -0.25)),
                             (),
                             ((0.375, 0.0, 0.4), (0.5625, 0.0, 0.2)),
                             ((-0.02, 0.0, 0.23),),
                             ((-0.3, 0.0, -0.4),),
                             ((0.25, 0.0, -0.425), (0.125, 0.0, -0.36)),
                             ((-0.5625, 0.0, -0.07), (-0.45, 0.0, 0.2125)),
                             ((-0.125, 0.0, 0.5),),
                             ((0.66, 0.0, -0.4),),
                             ((-0.68, 0.0, -0.444),),
                             ((-0.6, 0.0, 0.45),),
                             ((0.66, 0.0, 0.5),),
                             ((0.4, 0.0, -0.35),))
        self.labelPosList = ((0.594, 0.0, -0.075),
                             (0.0, 0.0, -0.1),
                             (0.475, 0.0, 0.25),
                             (0.1, 0.0, 0.15),
                             (-0.3, 0.0, -0.375),
                             (0.2, 0.0, -0.45),
                             (-0.55, 0.0, 0.0),
                             (-0.088, 0.0, 0.47),
                             (0.7, 0.0, -0.5),
                             (-0.7, 0.0, -0.5),
                             (-0.7, 0.0, 0.5),
                             (0.7, 0.0, 0.5),
                             (0.45, 0.0, -0.45))
        self.labels = []
        self.clouds = []
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        buttonLoc = (0.45, 0, - 0.74)
        self.safeZoneButton = DirectButton(
            parent=self.map,
            relief=None,
            image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
            image_scale=(1.3, 1.1, 1.1),
            pos=buttonLoc,
            text='Back to Playground',
            text_scale=.055,
            text_pos=(0, -0.02),
            textMayChange=0)
        self.goHomeButton = DirectButton(
            parent=self.map,
            relief=None,
            image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
            image_scale=(0.66, 1.1, 1.1),
            pos=(0.15, 0, -.74),
            text='Go Home',
            text_scale=.055,
            text_pos=(0, -0.02),
            textMayChange=0,
            command=self.goHome)
        guiButton.removeNode()
        self.hoodLabel = DirectLabel(
            parent=self.map,
            relief=None,
            pos=(-0.43, 0, -0.726),
            text='',
            text_scale=.06,
            text_pos=(0, 0),
            text_wordwrap=14)
        self.hoodLabel.hide()
        self.map.resetFrameSize()
        self.map.hide()
        self.safeZoneButton.hide()
        self.book.hide()

    def openBook(self):
        base.playSfx(self.openSound)
        base.render.hide()
        base.setBackgroundColor(0.05, 0.15, 0.4)
        self.book.show()
        self.bookOpenButton.hide()
        self.bookCloseButton.show()
        self.map.show()

    def closeBook(self):
        base.playSfx(self.closeSound)
        base.render.show()
        base.setBackgroundColor(Globals.defaultBackgroundColor)
        self.book.hide()
        self.bookOpenButton.show()
        self.bookCloseButton.hide()
        self.map.hide()

    def goHome(self):
        messenger.send('unloadTTC')
        self.estate = Estate().load()
