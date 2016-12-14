from direct.showbase.DirectObject import DirectObject

import Sky
from LoadingScreen import LoadingScreen
from dna.DNALoader import *
from hood.places.estate import HouseGlobals


class Estate(DirectObject):

    def __init__(self):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.storageFile = 'Resources/phase_4/dna/storage.pdna'
        self.pgStorageFile = 'Resources/phase_5.5/dna/storage_estate.pdna'
        self.szDNAFile = 'Resources/phase_5.5/dna/estate_1.pdna'
        self.houseNode = [None] * 6
        self.houseModels = [None] * HouseGlobals.NUM_HOUSE_TYPES

    def load(self, sky=1):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorageFile, None, None, self.szDNAFile)
        self.estate = self.dna.returnGeom()
        self.loadHouses()
        self.loadSunMoon()
        self.estate.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = base.loadMusic("phase_4/audio/bgm/TC_nbrhood.ogg")
        path = self.estate.find('**/Path')
        path.setBin('ground', 10, 1)
        self.ls.end()

    def loadHouses(self):
        for i in xrange(HouseGlobals.NUM_HOUSE_TYPES):
            self.houseModels[i] = loader.loadModel(HouseGlobals.houseModels[i])

        for i in xrange(6):
            posHpr = HouseGlobals.houseDrops[i]
            self.houseNode[i] = self.estate.attachNewNode('esHouse_' + str(i))
            self.houseNode[i].setPosHpr(*posHpr)
            print 'idk'

    def loadSunMoon(self):
        self.sun = loader.loadModel('phase_4/models/props/sun.bam')
        self.moon = loader.loadModel('phase_5.5/models/props/moon.bam')
        self.sunMoonNode = self.estate.attachNewNode('sunMoon')
        self.sunMoonNode.setPosHpr(0, 0, 0, 0, 0, 0)
        if self.sun:
            self.sun.reparentTo(self.sunMoonNode)
            self.sun.setY(270)
            self.sun.setScale(2)
            self.sun.setBillboardPointEye()
        if self.moon:
            self.moon.setP(180)
            self.moon.reparentTo(self.sunMoonNode)
            self.moon.setY(-270)
            self.moon.setScale(15)
            self.moon.setBillboardPointEye()
        self.sunMoonNode.setP(30)