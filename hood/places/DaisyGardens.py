import random
from direct.showbase.DirectObject import DirectObject
import Globals
from dna.DNALoader import *
from hood.places.Hood import Hood
from direct.task.Task import Task

SpawnPoints = [
    [0, 0, 0, -10.5, 0, 0],
    [76, 35, 1.1, -30.2, 0, 0],
    [97, 106, 0, 51.4, 0, 0],
    [51, 180, 10, 22.6, 0, 0],
    [-14, 203, 10, 85.6, 0, 0],
    [-58, 158, 10, -146.9, 0, 0],
    [-86, 128, 0, -178.9, 0, 0],
    [-64, 65, 0, 17.7, 0, 0],
    [-13, 39, 0, -15.7, 0, 0],
    [-12, 193, 0, -112.4, 0, 0],
    [87, 128, 0, 45.4, 0, 0]
]


class DG(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_8/audio/bgm/DG_nbrhood.ogg"
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.storageFile = 'Resources/phase_4/dna/storage.pdna'
        self.pgStorageFile = 'Resources/phase_8/dna/storage_DG.pdna'
        self.szStorageFile = 'Resources/phase_8/dna/storage_DG_sz.pdna'
        self.szDNAFile = 'Resources/phase_8/dna/daisys_garden_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (0.8, 0.6, 1.0, 1.0)
        self.titleText = "Daisy Gardens"

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
        base.setCurrentZone(Globals.DGZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        self.birdSound = map(base.loadSfx, ['phase_8/audio/sfx/SZ_DG_bird_01.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_02.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_03.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_04.ogg'])
        taskMgr.doMethodLater(1, self.__birds, 'DG-birds')

    def __birds(self, task):
        base.playSfx(random.choice(self.birdSound))
        time = random.random() * 20.0 + 1
        taskMgr.doMethodLater(time, self.__birds, 'DG-birds')
        return Task.done

    def unload(self):
        taskMgr.remove('DG-birds')
        del self.birdSound
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')
