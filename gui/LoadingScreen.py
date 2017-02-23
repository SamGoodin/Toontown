from pandac.PandaModules import *
from direct.gui.DirectGui import *
import random
import Globals

class LoadingScreen:

    def __init__(self):
        self.defaultTex = 'phase_3.5/maps/loading/default.jpg'
        self.__expectedCount = 0
        self.__count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background')
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None,
                                 pos=(base.a2dRight / 100, 0, 0.535), text='', textMayChange=1, text_scale=0.06,
                                 text_fg=(0, 0, 0, 1), text_align=TextNode.ALeft,
                                 text_font=Globals.getInterfaceFont())
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(
        base.a2dLeft + (base.a2dRight / 4.95), base.a2dRight - (base.a2dRight / 4.95), -0.03, 0.03), pos=(0, 0, 0.15),
                                     text='')
        logoScale = 0.5625  # Scale for our locked aspect ratio (2:1).
        self.logo = OnscreenImage(
            image='phase_3/maps/toontown-logo.png',
            scale=(logoScale * 2.0, 1, logoScale))
        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        # self.logo.setPos(scale[0], 0, -scale[2])
        self.logo.setPos(0, 0, -scale[2])

    def getTip(self):
        return random.choice(Globals.TipDict.get("TIP_GENERAL"))

    def destroy(self):
        self.title.destroy()
        self.gui.removeNode()
        self.logo.removeNode()

    def begin(self, range, gui=1):
        self.waitBar['range'] = range
        self.title['text'] = self.getTip()
        loadingScreenTex = self.defaultTex
        self.background = loader.loadTexture(loadingScreenTex)
        self.__count = 0
        self.__expectedCount = range
        if gui:
            self.title.reparentTo(base.a2dpBottomLeft, 4000)
            self.title.setPos(0.35, 0, 0.23)
            self.gui.setPos(0, -0.1, 0)
            self.gui.reparentTo(aspect2d, 4000)
            self.gui.setTexture(self.background, 1)
            if loadingScreenTex == self.defaultTex:
                self.logo.reparentTo(base.a2dpTopCenter, 4000)
        else:
            self.title.reparentTo(base.a2dpBottomLeft, 4000)
            self.gui.reparentTo(hidden)
            self.logo.reparentTo(hidden)
        self.waitBar.reparentTo(base.a2dpBottomCenter, 4000)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.logo.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)