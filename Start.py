from panda3d.core import *
loadPrcFile("config/Config.prc")

from data.LocalData import LocalData
from direct.showbase.ShowBase import ShowBase
from StartMenu import StartMenu
import Globals
from direct.gui import DirectGuiGlobals
from gui.MarginManager import MarginManager
from gui.margins.MarginManager import MarginManager as OtherMarginManager
from gui.nametag import NametagGlobals
from panda3d.physics import PhysicsManager, ParticleSystemManager


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.physicsMgr = PhysicsManager()
        self.particleMgr = ParticleSystemManager()
        self.localData = LocalData()
        Globals.setSignFont(loader.loadFont('phase_3/models/fonts/MickeyFont'))
        Globals.setRolloverSound(loader.loadSfx("phase_3/audio/sfx/GUI_rollover.ogg"))
        Globals.setClickSound(loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.ogg"))
        Globals.setInterfaceFont(loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'))
        DirectGuiGlobals.setDefaultFont(Globals.getInterfaceFont())
        DirectGuiGlobals.setDefaultClickSound(Globals.getClickSound())
        DirectGuiGlobals.setDefaultRolloverSound(Globals.getRolloverSound())
        NametagGlobals.setCardModel('phase_3/models/props/panel.bam')
        NametagGlobals.setArrowModel('phase_3/models/props/arrow.bam')
        NametagGlobals.setChatBalloon3dModel('phase_3/models/props/chatbox.bam')
        NametagGlobals.setChatBalloon2dModel('phase_3/models/props/chatbox_noarrow.bam')
        NametagGlobals.setThoughtBalloonModel('phase_3/models/props/chatbox_thought_cutout.bam')
        Globals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
        self.setupMargins()
        self.currentZone = None
        self.lastPlayground = None
        self.loader.loadMusic("phase_3/audio/bgm/tti_theme.ogg").play()
        self.toon = None
        self.toonClass = None
        self.go()

    def setupMargins(self):
        self.marginManager = MarginManager()
        self.otherMarginManager = OtherMarginManager()

    def setCurrentZone(self, zone):
        self.currentZone = zone

    def setLastPlayground(self, zone):
        self.lastPlayground = zone

    def go(self):
        import Messenger
        Messenger.Messenger().__init__()
        self.startMenuClass = StartMenu()
        self.setBackgroundColor(Globals.defaultBackgroundColor)
        self.startMenuClass.loadStartMenu()


game = MyApp()
game.run()

