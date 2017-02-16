from direct.showbase.DirectObject import DirectObject

import Sky
from LoadingScreen import LoadingScreen
from dna.DNALoader import *
from dna.DNADoor import DNADoor
from hood.places.estate import HouseGlobals
import Globals


class Estate(DirectObject):

    def __init__(self):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.namePlate = None
        self.floorMat = None
        self.dna = None
        self.storageFile = 'Resources/phase_4/dna/storage.pdna'
        self.pgStorageFile = 'Resources/phase_5.5/dna/storage_estate.pdna'
        self.szDNAFile = 'Resources/phase_5.5/dna/estate_1.pdna'
        self.houseNode = [None] * 6
        self.houseModels = [None] * HouseGlobals.NUM_HOUSE_TYPES
        self.housePosInd = 0
        self.name = ''
        self.accept('unloadZone', self.unload)

    def load(self, sky=1):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorageFile, None, None, self.szDNAFile)
        self.estate = self.dna.returnGeom()
        self.loadHouses()
        self.loadSunMoon()
        self.loadAirplane()
        self.estate.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = base.loadMusic("phase_4/audio/bgm/TC_nbrhood.ogg")
        path = self.estate.find('**/Path')
        path.setBin('ground', 10, 1)
        base.setCurrentZone(Globals.EstateZone)
        self.ls.end()

    def unload(self):
        if self.namePlate:
            self.namePlate.removeNode()
            del self.namePlate
            self.namePlate = None
        if self.floorMat:
            self.floorMat.removeNode()
            del self.floorMat
            self.floorMat = None
        if self.house:
            self.house.removeNode()
            del self.house
        del self.skyFile
        del self.music
        del self.dna
        del self.szDNAFile
        del self.pgStorageFile
        del self.storageFile
        for model in self.houseModels:
            model.removeNode()
        del self.houseModels
        for node in self.houseNode:
            node.removeNode()
        del self.houseNode
        self.sunMoonNode.removeNode()
        del self.sunMoonNode
        self.ignore('unloadZone')

    def loadHouses(self):
        for i in xrange(HouseGlobals.NUM_HOUSE_TYPES):
            self.houseModels[i] = loader.loadModel(HouseGlobals.houseModels[i])

        for i in xrange(6):
            posHpr = HouseGlobals.houseDrops[i]
            self.houseNode[i] = self.estate.attachNewNode('esHouse_' + str(i))
            self.houseNode[i].setPosHpr(*posHpr)
            self.houseNode[i].show()

        x = 0
        for house in self.houseModels:
            houseModel = self.houseModels[5]
            self.house = houseModel.copyTo(self.houseNode[x])
            self.__setupDoor()
            self.__setupFloorMat()
            x += 1

    def __setupDoor(self):
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dna.dnaStore.findNode(doorModelName)
        door_origin = self.house.find('**/door_origin')
        door_origin.setHpr(90, 0, 0)
        door_origin.setScale(0.6, 0.6, 0.8)
        door_origin.setPos(door_origin, 0.5, 0, 0.0)
        doorNP = door.copyTo(door_origin)
        self.door_origin = door_origin
        houseColor = HouseGlobals.stairWood
        color = Vec4(houseColor[0], houseColor[1], houseColor[2], 1)
        DNADoor.setupDoor(doorNP, door_origin, door_origin, self.dna.dnaStore, "String", color)

    def __setupFloorMat(self, changeColor=True):
        if self.floorMat:
            self.floorMat.removeNode()
            del self.floorMat
            self.floorMat = None
        mat = self.house.find('**/mat')
        if changeColor:
            mat.setColor(0.4, 0.357, 0.259, 1.0)
        color = HouseGlobals.houseColors[self.housePosInd]
        matText = TextNode('matText')
        matText.setTextColor(color[0], color[1], color[2], 1)
        matText.setAlign(matText.ACenter)
        matText.setFont(Globals.getSignFont())
        matText.setShadowColor(0, 0, 0, 1)
        matText.setBin('fixed')
        if Globals.BuildingNametagShadow:
            matText.setShadow(*Globals.BuildingNametagShadow)
        matText.setWordwrap(10.0)
        xScale = 1.0
        numLines = 0
        if self.name == '':
            return
        else:
            houseName = '%s\n House' % Globals.GetPossesive(self.name)
        matText.setText(houseName)
        self.matText = matText
        textHeight = matText.getHeight() - 2
        textWidth = matText.getWidth()
        xScale = 1.0
        if textWidth > 8:
            xScale = 8.0 / textWidth
        mat_origin = self.house.find('**/mat_origin')
        pos = mat_origin.getPos()
        mat_origin.setPosHpr(pos[0] - 0.15 * textHeight, pos[1], pos[2], 90, -90, 0)
        self.floorMat = mat_origin.attachNewNode(self.matText)
        self.floorMat.setDepthWrite(0)
        self.floorMat.setPos(0, -.025, 0)
        self.floorMat.setScale(0.45 * xScale)
        return

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

    def loadAirplane(self):
        self.airplane = loader.loadModel('phase_4/models/props/airplane')
        self.airplane.setScale(4)
        self.airplane.setPos(0, 0, 1)
        self.banner = self.airplane.find('**/*banner')
        bannerText = TextNode('bannerText')
        bannerText.setTextColor(1, 0, 0, 1)
        bannerText.setAlign(bannerText.ACenter)
        bannerText.setFont(Globals.getSignFont())
        bannerText.setText('Welcome')
        self.bn = self.banner.attachNewNode(bannerText.generate())
        self.bn.setHpr(180, 0, 0)
        self.bn.setPos(-1.8, 0.1, 0)
        self.bn.setScale(0.35)
        self.banner.hide()
