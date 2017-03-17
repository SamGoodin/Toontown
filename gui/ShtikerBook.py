from direct.gui.DirectGui import *
import Globals
from direct.interval.IntervalGlobal import *
from panda3d.core import Vec4

class ShtikerBook(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=DGG.BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerBook)
        model = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        self['image'] = model.find('**/big_book')
        self['image_scale'] = (2, 1, 1.5)
        self.resetFrameSize()
        self.OpenButton = DirectButton(image=(
            model.find('**/BookIcon_CLSD'), model.find('**/BookIcon_OPEN'), model.find('**/BookIcon_RLVR')),
            relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305,
            command=self.startOpenBook)
        self.CloseButton = DirectButton(image=(
            model.find('**/BookIcon_OPEN'), model.find('**/BookIcon_CLSD'), model.find('**/BookIcon_RLVR2')),
            relief=None, pos=(-0.158, 0, 0.17), parent=base.a2dBottomRight, scale=0.305,
            command=self.closeBook)
        self.OpenButton.show()
        self.CloseButton.hide()
        self.nextArrow = DirectButton(parent=self, relief=None, image=(
            model.find('**/arrow_button'), model.find('**/arrow_down'), model.find('**/arrow_rollover')),
                                      scale=(0.1, 0.1, 0.1), pos=(0.838, 0, -0.661))
        self.prevArrow = DirectButton(parent=self, relief=None, image=(
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
            textMayChange=0,
            command=self.backToPlayground)
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
        cloudModel = loader.loadModel('phase_3.5/models/gui/cloud')
        cloudImage = cloudModel.find('**/cloud')
        for hood in Globals.HoodsForTeleportAll:
            fullname = hood
            hoodIndex = Globals.HoodsForTeleportAll.index(hood)
            label = DirectButton(
                parent=self.map,
                relief=None,
                pos=self.labelPosList[hoodIndex],
                pad=(0.2, 0.16),
                text=('', fullname, fullname),
                text_bg=Vec4(1, 1, 1, 0.4),
                text_scale=0.055,
                text_wordwrap=8,
                rolloverSound=None,
                clickSound=None,
                pressEffect=0,
                sortOrder=1,
                command=self.teleportToZone,
                extraArgs=fullname)
            label.resetFrameSize()
            self.labels.append(label)
            hoodClouds = []
            for cloudScale, cloudPos in zip(self.cloudScaleList[hoodIndex], self.cloudPosList[hoodIndex]):
                cloud = DirectFrame(
                    parent=self.map,
                    relief=None,
                    state=DGG.DISABLED,
                    image=cloudImage,
                    scale=(cloudScale[0], cloudScale[1], cloudScale[2]),
                    pos=(cloudPos[0], cloudPos[1], cloudPos[2]))
                cloud.hide()
                hoodClouds.append(cloud)

            self.clouds.append(hoodClouds)

        self.resetFrameSize()
        self.hoodLabel.hide()
        self.map.resetFrameSize()
        self.map.hide()
        self.safeZoneButton.hide()
        self.hide()
        self.estate = None

    def teleportToZone(self, *args):
        self.zone = ""
        for arg in args:
            self.zone += arg
        track = Sequence(Func(self.closeBook), Wait(2), Func(base.toon.enterTeleportOut), Wait(4),
                         Func(self.loadNewZone))
        track.start()

    def loadNewZone(self):
        self.unloadCurrentPlayground()
        def ttc():
            messenger.send('loadTTC')

        def dock():
            messenger.send('loadDock')

        options = {Globals.TTCZone: ttc,
                   Globals.DDZone: dock}
        options[self.zone]()
        messenger.send('teleportIn')

    def startOpenBook(self):
        self.track = Sequence(Func(base.toon.enterBook), Wait(.6), Func(self.openBook), Func(base.toon.enterReadBook),
                              Func(self.finishOpenBook))
        self.track.start()
        base.toon.disableAvatarControls()

    def openBook(self):
        base.playSfx(self.openSound)
        base.render.hide()
        base.setBackgroundColor(0.05, 0.15, 0.4)
        self.show()
        self.OpenButton.hide()
        self.CloseButton.show()
        self.map.show()
        if base.currentZone == Globals.EstateZone:
            self.safeZoneButton.show()
            self.goHomeButton.hide()
        elif "-" in base.currentZone:
            self.safeZoneButton.show()
            self.goHomeButton.show()
        else:
            self.safeZoneButton.hide()
            self.goHomeButton.show()
        messenger.send('hideFriendsListButton')

    def finishOpenBook(self):
        self.track.finish()

    def closeBook(self):
        self.track = Sequence(Func(base.toon.enterCloseBook), Wait(2), Func(base.toon.exitCloseBook), Wait(0),
                              Func(self.finishCloseBook))
        self.track.start()
        messenger.send('showFriendsListButton')
        base.playSfx(self.closeSound)
        base.render.show()
        base.setBackgroundColor(Globals.defaultBackgroundColor)
        self.hide()
        self.OpenButton.show()
        self.CloseButton.hide()
        self.map.hide()

    def finishCloseBook(self):
        self.track.finish()
        base.toon.enableAvatarControls()

    def goHome(self):
        track = Sequence(Func(self.closeBook), Wait(2), Func(base.toon.enterTeleportOut), Wait(4),
                         Func(self.loadEstate))
        track.start()

    def loadEstate(self):
        base.setLastPlayground(base.currentZone.rsplit('-', 1)[0])
        self.unloadCurrentPlayground()
        messenger.send('loadEstate')

    def unloadCurrentPlayground(self):
        messenger.send('unloadZone')

    def backToPlayground(self):
        self.btpgTrack = Sequence(Func(self.closeBook), Wait(2), Func(base.toon.enterTeleportOut), Wait(4),
                                  Func(self.goBackToPlayground), Func(self.finishBackToPlayground))
        self.btpgTrack.start()

    def goBackToPlayground(self):
        self.unloadCurrentPlayground()

        def ttc():
            messenger.send('backToPlayground')

        options = {Globals.TTCZone: ttc}
        options[base.lastPlayground]()

    def finishBackToPlayground(self):
        self.finishCloseBook()
        self.btpgTrack.finish()

    def hideOpenClose(self):
        self.OpenButton.hide()
        self.CloseButton.hide()

    def showOpenClose(self):
        if self.isHidden():
            self.OpenButton.show()
            self.CloseButton.hide()
        else:
            self.OpenButton.hide()
            self.CloseButton.show()

    def disable(self):
        self.OpenButton['state'] = DGG.DISABLED
        self.CloseButton['state'] = DGG.DISABLED

    def enable(self):
        self.OpenButton['state'] = DGG.NORMAL
        self.CloseButton['state'] = DGG.NORMAL