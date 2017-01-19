from panda3d.core import *
loadPrcFile("config/Config.prc")

from direct.showbase.ShowBase import ShowBase
from StartMenu import StartMenu
import Globals
from direct.gui import DirectGuiGlobals


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        Globals.setSignFont(loader.loadFont('phase_3/models/fonts/MickeyFont'))
        Globals.setRolloverSound(loader.loadSfx("phase_3/audio/sfx/GUI_rollover.ogg"))
        Globals.setClickSound(loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.ogg"))
        Globals.setInterfaceFont(loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'))
        DirectGuiGlobals.setDefaultFont(Globals.getInterfaceFont())
        DirectGuiGlobals.setDefaultClickSound(Globals.getClickSound())
        DirectGuiGlobals.setDefaultRolloverSound(Globals.getRolloverSound())
        Globals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
        self.loader.loadMusic("phase_3/audio/bgm/tti_theme.ogg").play()
        self.toon = None
        self.toonClass = None
        self.go()

    def go(self):
        import Messenger
        Messenger.Messenger().__init__()
        self.startMenuClass = StartMenu()
        self.setBackgroundColor(Globals.defaultBackgroundColor)
        self.startMenuClass.loadStartMenu()


game = MyApp()
game.run()

