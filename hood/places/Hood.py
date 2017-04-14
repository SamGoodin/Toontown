from direct.interval.IntervalGlobal import *
from direct.gui import OnscreenText
from panda3d.core import *
import Globals
from gui.LoadingScreen import LoadingScreen
from gui import Sky
from pandac.PandaModules import *


class Hood:

    def __init__(self):
        self.ls = LoadingScreen()
        self.titleColor = None
        self.titleText = None
        self.music = None
        self.skyFile = None
        self.playground = None
        self.dna = None
        self.fog = None
        self.storageFile = 'phase_4/dna/storage.xml'
        self.notify = directNotify.newCategory('HoodLoader')
        self.whiteFogColor = Vec4(0.8, 0.8, 0.8, 1)

    def loadHood(self):
        self.playground = self.dna.returnGeom()
        self.playground.reparentTo(base.render)

    def enterHood(self):
        base.lastPlayground = self.titleText
        base.localData.updateLastPlayground()
        self.titleText = OnscreenText.OnscreenText(self.titleText, fg=self.titleColor, font=Globals.getSignFont(),
                                                   pos=(0, -0.5), scale=0.16, drawOrder=0, mayChange=1)
        self.doSpawnTitleText()
        base.cTrav = CollisionTraverser()
        base.camera.hide()
        self.notify.warning("Hood load successful.")

    def unload(self):
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.playground.removeNode()
        del self.playground
        del self.titleColor
        del self.titleText
        self.notify.warning("Hood unload successful.")

    def startSky(self):
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)

    def startMusic(self, musicFile):
        self.music = base.loadMusic(musicFile)
        base.playMusic(self.music, looping=1, volume=0.8)

    def doSpawnTitleText(self):
        self.titleText.show()
        self.titleText.setColor(Vec4(*self.titleColor))
        self.titleText.clearColorScale()
        self.titleText.setFg(self.titleColor)
        seq = Sequence(Wait(0.1), Wait(6.0), self.titleText.colorScaleInterval(0.5, Vec4(1.0, 1.0, 1.0, 0.0)),
                       Func(self.titleText.hide))
        seq.start()
        seq.setAutoFinish(True)

    def tick(self):
        self.ls.tick()
