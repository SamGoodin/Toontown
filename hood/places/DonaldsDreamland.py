import random
from direct.showbase.DirectObject import DirectObject
import Globals
from dna.DNALoader import *
from hood.places.Hood import Hood

SpawnPoints = [
    [77, 91, 0, 124.4, 0, 0],
    [29, 92, 0, -154.5, 0, 0],
    [-28, 49, -16.4, -142, 0, 0],
    [21, 40, -16, -65.1, 0, 0],
    [48, 27, -15.4, -161, 0, 0],
    [-2, -22, -15.2, -132.1, 0, 0],
    [-92, -88, 0, -116.3, 0, 0],
    [-56, -93, 0, -21.5, 0, 0],
    [20, -88, 0, -123.4, 0, 0],
    [76, -90, 0, 11, 0, 0]
]


class Dreamland(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_8/audio/bgm/DL_nbrhood.ogg"
        self.sky = None
        self.skyFile = "phase_8/models/props/DL_sky"
        self.dna = None
        self.storageFile = 'Resources/phase_4/dna/storage.pdna'
        self.pgStorageFile = 'Resources/phase_8/dna/storage_DL.pdna'
        self.szStorageFile = 'Resources/phase_8/dna/storage_DL_sz.pdna'
        self.szDNAFile = 'Resources/phase_8/dna/donalds_dreamland_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (1.0, 0.9, 0.5, 1.0)
        self.titleText = "Donald's Dreamland"

    def load(self):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorageFile, None, self.szStorageFile, self.szDNAFile)
        self.loadHood()
        self.tick()
        self.startSky()
        self.tick()
        self.startMusic(self.musicFile)
        self.loadHoodSpecifics()
        self.tick()
        base.setCurrentZone(Globals.DLZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        pass

    def unload(self):
        Hood.unload(self)
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')
