import random
from direct.showbase.DirectObject import DirectObject
import Globals
from hood.places.Hood import Hood

SpawnPoints = [
    [86, 44, -13.5, 121.1, 0, 0],
    [88, -8, -13.5, 91, 0, 0],
    [92, -76, -13.5, 62.5, 0, 0],
    [53, -112, 6.5, 65.8, 0, 0],
    [-69, -71, 6.5, -67.2, 0, 0],
    [-75, 21, 6.5, -100.9, 0, 0],
    [-21, 72, 6.5, -129.5, 0, 0],
    [56, 72, 6.5, 138.2, 0, 0],
    [-41, 47, 6.5, -98.9, 0, 0]
]


class MM(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/MM_nbrhood.ogg"
        self.sky = None
        self.skyFile = "phase_6/models/props/MM_sky"
        self.dna = None
        self.pgStorageFile = 'phase_6/dna/storage_MM.pdna'
        self.szStorageFile = 'phase_6/dna/storage_MM_sz.pdna'
        self.szDNAFile = 'phase_6/dna/minnies_melody_land_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (1.0, 0.5, 0.5, 1.0)
        self.titleText = "Minnie's Melodyland"

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
        base.setCurrentZone(Globals.MMZone)
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
