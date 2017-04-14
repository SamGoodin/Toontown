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
from gui.DTimer import DTimer
import os
from direct.showbase.Transitions import Transitions
import ToontownLoader
from dna.DNAStorage import DNAStorage


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.setupVfs()
        Globals.setInterfaceFont(self.loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'))
        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        self.physicsMgr = PhysicsManager()
        self.particleMgr = ParticleSystemManager()
        self.DTimer = DTimer()
        self.localData = LocalData()
        self.setCursorAndIcon()
        self.transitions = Transitions(self.loader)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        Globals.setSignFont(self.loader.loadFont('phase_3/models/fonts/MickeyFont'))
        Globals.setRolloverSound(self.loader.loadSfx("phase_3/audio/sfx/GUI_rollover.ogg"))
        Globals.setClickSound(self.loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.ogg"))
        DirectGuiGlobals.setDefaultFont(Globals.getInterfaceFont())
        DirectGuiGlobals.setDefaultClickSound(Globals.getClickSound())
        DirectGuiGlobals.setDefaultRolloverSound(Globals.getRolloverSound())
        NametagGlobals.setCardModel('phase_3/models/props/panel.bam')
        NametagGlobals.setArrowModel('phase_3/models/props/arrow.bam')
        NametagGlobals.setChatBalloon3dModel('phase_3/models/props/chatbox.bam')
        NametagGlobals.setChatBalloon2dModel('phase_3/models/props/chatbox_noarrow.bam')
        NametagGlobals.setThoughtBalloonModel('phase_3/models/props/chatbox_thought_cutout.bam')
        Globals.setDefaultDialogGeom(self.loader.loadModel('phase_3/models/gui/dialog_box_gui'))
        self.setupMargins()
        self.currentZone = None
        self.lastPlayground = None
        self.loader.loadMusic("phase_3/audio/bgm/ttr_theme.ogg").play()
        self.toon = None
        self.toonClass = None
        self.loadDnaStore()
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

    def setupVfs(self):
        self.vfs = VirtualFileSystem.getGlobalPtr()
        for mount in Globals.mounts:
            self.vfs.mount("multifiles/" + mount, "resources", 0)

    def setCursorAndIcon(self):
        import tempfile, atexit, shutil
        tempdir = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, tempdir)
        searchPath = DSearchPath()
        if __debug__:
            searchPath.appendDirectory(Filename('resources/phase_3/etc'))
        searchPath.appendDirectory(Filename('phase_3/etc'))
        for filename in ['toonmono.cur', 'icon.ico']:
            p3filename = Filename(filename)
            found = self.vfs.resolveFilename(p3filename, searchPath)
            if not found:
                return
            with open(os.path.join(tempdir, filename), 'wb') as f:
                f.write(self.vfs.readFile(p3filename, False))
        wp = WindowProperties()
        wp.setCursorFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'toonmono.cur')))
        wp.setIconFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'icon.ico')))
        self.win.requestProperties(wp)

    def loadDnaStore(self):
        if not hasattr(self, 'dnaStore'):
            self.dnaStore = DNAStorage()

            self.loader.loadDNA('phase_4/dna/storage.xml').store(self.dnaStore)

            self.dnaStore.storeFont(Globals.getInterfaceFont(), 'humanist')
            self.dnaStore.storeFont(Globals.getSignFont(), 'mickey')
            #self.dnaStore.storeFont(Globals.getSuitFont(), 'suit')

            self.loader.loadDNA('phase_3.5/dna/storage_interior.xml').store(self.dnaStore)


game = MyApp()
game.run()

