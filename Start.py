from panda3d.core import *
loadPrcFile("config/Config.prc")

from data.LocalData import LocalData
from direct.showbase.ShowBase import ShowBase
from StartMenu import StartMenu
import Globals
from direct.gui import DirectGuiGlobals
from gui.MarginManager import MarginManager
from gui.nametag.ChatBalloon import ChatBalloon
from gui.nametag import NametagGlobals
from panda3d.physics import PhysicsManager, ParticleSystemManager
from gui.DTimer import DTimer
import os
from direct.showbase.Transitions import Transitions
import ToontownLoader
from dna.DNAStorage import DNAStorage
from panda3d.core import *


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.enviroDR = None
        self.enviroCam = None
        self.stereoEnabled = True
        self.setupEnviroCamera()
        self.setupVfs()
        Globals.setInterfaceFont(loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'))
        Globals.setSignFont(loader.loadFont('phase_3/models/fonts/MickeyFont'))
        Globals.setRolloverSound(loader.loadSfx("phase_3/audio/sfx/GUI_rollover.ogg"))
        Globals.setClickSound(loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.ogg"))
        DirectGuiGlobals.setDefaultFont(Globals.getInterfaceFont())
        DirectGuiGlobals.setDefaultClickSound(Globals.getClickSound())
        DirectGuiGlobals.setDefaultRolloverSound(Globals.getRolloverSound())
        DirectGuiGlobals.setDefaultFontFunc('phase_3/models/fonts/ImpressBT.ttf')
        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__.loader = self.loader
        oldLoader.destroy()
        self.physicsMgr = PhysicsManager()
        self.particleMgr = ParticleSystemManager()
        self.DTimer = DTimer()
        self.localData = LocalData()
        self.setCursorAndIcon()
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setMinFov(Globals.DefaultCameraFov / (4. / 3.))
        self.camLens.setNearFar(Globals.DefaultCameraNear, Globals.DefaultCameraFar)
        self.cam2d.node().setCameraMask(BitMask32.bit(1))
        self.cam.node().setCameraMask(Globals.MainCameraBitmask | Globals.EnviroCameraBitmask)
        self.transitions = Transitions(self.loader)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.initNametagGlobals()
        Globals.setDefaultDialogGeom(self.loader.loadModel('phase_3/models/gui/dialog_box_gui'))
        self.currentZone = None
        self.lastPlayground = None
        self.loader.loadMusic("phase_3/audio/bgm/ttr_theme.ogg").play()
        self.toon = None
        self.toonClass = None
        self.loadDnaStore()
        self.go()

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
            self.vfs.mount("multifiles/" + mount, "/", 0)

    def setCursorAndIcon(self):
        import tempfile, atexit, shutil
        tempdir = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, tempdir)
        searchPath = DSearchPath()
        if __debug__:
            searchPath.appendDirectory(Filename('/phase_3/etc'))
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
            #self.dnaStore.storeFont(ToontownGlobals.getSuitFont(), 'suit')

            self.loader.loadDNA('phase_3.5/dna/storage_interior.xml').store(self.dnaStore)

    def initNametagGlobals(self):
        arrow = loader.loadModel('phase_3/models/props/arrow')
        card = loader.loadModel('phase_3/models/props/panel')
        speech3d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox'))
        thought3d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox_thought_cutout'))
        speech2d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox_noarrow'))
        chatButtonGui = loader.loadModel('phase_3/models/gui/chat_button_gui')
        NametagGlobals.setCamera(self.cam)
        NametagGlobals.setArrowModel(arrow)
        NametagGlobals.setNametagCard(card, VBase4(-0.5, 0.5, -0.5, 0.5))
        if self.mouseWatcherNode:
            NametagGlobals.setMouseWatcher(self.mouseWatcherNode)
        NametagGlobals.setSpeechBalloon3d(speech3d)
        NametagGlobals.setThoughtBalloon3d(thought3d)
        NametagGlobals.setSpeechBalloon2d(speech2d)
        NametagGlobals.setThoughtBalloon2d(thought3d)
        NametagGlobals.setPageButton(PGButton.SReady, chatButtonGui.find('**/Horiz_Arrow_UP'))
        NametagGlobals.setPageButton(PGButton.SDepressed, chatButtonGui.find('**/Horiz_Arrow_DN'))
        NametagGlobals.setPageButton(PGButton.SRollover, chatButtonGui.find('**/Horiz_Arrow_Rllvr'))
        NametagGlobals.setQuitButton(PGButton.SReady, chatButtonGui.find('**/CloseBtn_UP'))
        NametagGlobals.setQuitButton(PGButton.SDepressed, chatButtonGui.find('**/CloseBtn_DN'))
        NametagGlobals.setQuitButton(PGButton.SRollover, chatButtonGui.find('**/CloseBtn_Rllvr'))
        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound:
            NametagGlobals.setRolloverSound(rolloverSound)
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound:
            NametagGlobals.setClickSound(clickSound)
        NametagGlobals.setToon(self.cam)

        self.marginManager = MarginManager()
        '''self.margins = self.aspect2d.attachNewNode(self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
        mm = self.marginManager

        # TODO: Dynamicaly add more and reposition cells
        padding = 0.0225

        # Order: Top to bottom
        self.leftCells = [
            mm.addGridCell(0.2 + padding, -0.45, base.a2dTopLeft),  # Above boarding groups
            mm.addGridCell(0.2 + padding, -0.9, base.a2dTopLeft),  # 1
            mm.addGridCell(0.2 + padding, -1.35, base.a2dTopLeft)  # Below Boarding Groups
        ]

        # Order: Left to right
        self.bottomCells = [
            mm.addGridCell(-0.87, 0.2 + padding, base.a2dBottomCenter),  # To the right of the laff meter
            mm.addGridCell(-0.43, 0.2 + padding, base.a2dBottomCenter),  # 1
            mm.addGridCell(0.01, 0.2 + padding, base.a2dBottomCenter),  # 2
            mm.addGridCell(0.45, 0.2 + padding, base.a2dBottomCenter),  # 3
            mm.addGridCell(0.89, 0.2 + padding, base.a2dBottomCenter)  # To the left of the shtiker book
        ]

        # Order: Bottom to top
        self.rightCells = [
            mm.addGridCell(-0.2 - padding, -1.35, base.a2dTopRight),  # Above the street map
            mm.addGridCell(-0.2 - padding, -0.9, base.a2dTopRight),  # Below the friends list
            mm.addGridCell(-0.2 - padding, -0.45, base.a2dTopRight)  # Behind the friends list
        ]'''

    def setupEnviroCamera(self):
        clearColor = VBase4(0, 0, 0, 1)
        if self.enviroDR:
            clearColor = self.enviroDR.getClearColor()
            self.win.removeDisplayRegion(self.enviroDR)
        if not self.enviroCam:
            self.enviroCam = self.cam.attachNewNode(Camera('enviroCam'))
        mainDR = self.camNode.getDisplayRegion(0)
        if self.stereoEnabled == False:
            self.enviroDR = self.win.makeStereoDisplayRegion()
            if not mainDR.isStereo():
                self.win.removeDisplayRegion(mainDR)
                mainDR = self.win.makeStereoDisplayRegion()
                mainDR.setCamera(self.cam)
            ml = mainDR.getLeftEye()
            mr = mainDR.getRightEye()
            el = self.enviroDR.getLeftEye()
            er = self.enviroDR.getRightEye()
            el.setSort(-8)
            ml.setSort(-6)
            er.setSort(-4)
            er.setClearDepthActive(True)
            mr.setSort(-2)
            mr.setClearDepthActive(False)
        else:
            self.enviroDR = self.win.makeMonoDisplayRegion()
            if mainDR.isStereo():
                self.win.removeDisplayRegion(mainDR)
                mainDR = self.win.makeMonoDisplayRegion()
                mainDR.setCamera(self.cam)
            self.enviroDR.setSort(-10)
        self.enviroDR.setClearColor(clearColor)
        self.win.setClearColor(clearColor)
        self.enviroDR.setCamera(self.enviroCam)
        self.enviroCamNode = self.enviroCam.node()
        self.enviroCamNode.setLens(self.cam.node().getLens())
        self.enviroCamNode.setCameraMask(Globals.EnviroCameraBitmask)
        render.hide(Globals.EnviroCameraBitmask)
        self.camList.append(self.enviroCam)
        self.backgroundDrawable = self.enviroDR
        self.enviroDR.setTextureReloadPriority(-10)


game = MyApp()
game.run()

