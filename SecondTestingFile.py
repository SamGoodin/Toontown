from pandac.PandaModules import *
loadPrcFile('config/Config.prc')

from direct.showbase.ShowBase import ShowBase
import Globals
import ToontownLoader
from dna.DNAStorage import DNAStorage


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        cbm = CullBinManager.getGlobalPtr()
        cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
        cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)
        cbm.addBin('gui-popup', CullBinManager.BTFixed, 60)

        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setMinFov(Globals.DefaultCameraFov / (4. / 3.))
        self.camLens.setNearFar(Globals.DefaultCameraNear, Globals.DefaultCameraFar)
        self.cam2d.node().setCameraMask(BitMask32.bit(1))

        # Keep VFS here to use files
        self.vfs = VirtualFileSystem.getGlobalPtr()
        for mount in Globals.mounts:
            self.vfs.mount("multifiles/" + mount, "/", 0)

        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__.loader = self.loader
        oldLoader.destroy()

        self.loadDnaStore()

        from hood.places.ToontownCentral import TTC
        self.ttc = TTC(None)
        self.ttc.load()
        self.ttc.startSky()

    def loadDnaStore(self):
        if not hasattr(self, 'dnaStore'):
            self.dnaStore = DNAStorage()

            self.loader.loadDNA('phase_4/dna/storage.xml').store(self.dnaStore)

            '''self.dnaStore.storeFont(Globals.getInterfaceFont(), 'humanist')
            self.dnaStore.storeFont(Globals.getSignFont(), 'mickey')
            self.dnaStore.storeFont(ToontownGlobals.getSuitFont(), 'suit')'''

            self.loader.loadDNA('phase_3.5/dna/storage_interior.xml').store(self.dnaStore)

    def setCurrentZone(self, zone):
        self.currentZone = zone

    def setLastPlayground(self, zone):
        self.lastPlayground = zone

T = Window()
T.run()