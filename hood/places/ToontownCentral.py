import random
from direct.showbase.DirectObject import DirectObject
from hood.places.Hood import Hood
import Globals
from gui import SkyUtil
from gui.LoadingScreen import LoadingScreen
from direct.task.Task import Task
from hood.places.Town import Town

SpawnPoints = [
    [-60, -8, 1.3, -90, 0, 0],
    [-66, -9, 1.3, -274, 0, 0],
    [17, -28, 4.1, -44, 0, 0],
    [87.7, -22, 4, 66, 0, 0],
    [-9.6, 61.1, 0, 132, 0, 0],
    [-109.0, -2.5, -1.656, -90, 0, 0],
    [-35.4, -81.3, 0.5, -4, 0, 0],
    [-103, 72, 0, -141, 0, 0],
    [93.5, -148.4, 2.5, 43, 0, 0],
    [25, 123.4, 2.55, 272, 0, 0],
    [48, 39, 4, 201, 0, 0],
    [-80, -61, 0.1, -265, 0, 0],
    [-46.875, 43.68, -1.05, 124, 0, 0],
    [34, -105, 2.55, 45, 0, 0],
    [16, -75, 2.55, 56, 0, 0],
    [-27, -56, 0.1, 45, 0, 0],
    [100, 27, 4.1, 150, 0, 0],
    [-70, 4.6, -1.9, 90, 0, 0],
    [-130.7, 50, 0.55, -111, 0, 0]
]

class TTC(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_4/audio/bgm/TC_nbrhood.ogg"
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.zoneId = Globals.ToontownCentralId
        self.storageDNAFile = 'phase_4/dna/storage_TT.xml'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.xml'
        self.szDNAFile = 'phase_4/dna/toontown_central_sz.xml'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
        self.titleText = "Toontown Central"
        self.accept('loadStreet', self.loadStreet)

    def load(self):
        self.loadHood()
        self.createSafeZone(self.szDNAFile)
        self.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        self.loadHoodSpecifics()
        base.setCurrentZone(Globals.TTCZone)
        self.enterHood()

    def loadHoodSpecifics(self):
        bank = self.playground.find('**/*toon_landmark_TT_bank_DNARoot')
        doorTrigger = bank.find('**/door_trigger*')
        doorTrigger.setY(doorTrigger.getY() - 1.5)
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        taskMgr.doMethodLater(1, self.__birds, 'TT-birds')

    def __birds(self, task):
        base.playSfx(random.choice(self.birdSound))
        time = random.random() * 20.0 + 1
        taskMgr.doMethodLater(time, self.__birds, 'TT-birds')
        return Task.done

    def unload(self):
        Hood.unload(self)
        taskMgr.remove('TT-birds')
        del self.birdSound
        self.ignoreAll()

    def loadStreet(self, streetId):
        if streetId == 2100:
            self.street = SillyStreet(self.toon)
            self.street.load()
            self.unload()
            self.toon.setPosHpr(-91.9644, -100.045, -0.47204, 82.325, 0, 0)
        elif streetId == 2200:
            self.street = LoopyLane(self.toon)
            self.street.load()
            self.unload()
            self.toon.setPosHpr(-76.0011, 96.14, -0.47921, -271.592, 0, 0)
        elif streetId == 2300:
            self.street = PunchlinePlace(self.toon)
            self.street.load()
            self.unload()
            self.toon.setPosHpr(4.39313, 22.2804, -0.478364, 269.45, 0, 0)
        else:
            print streetId

    def goofySpeedway(self, task):
        if self.toon.getX() <= 33.4 and self.toon.getX() >= 20.9:
            if self.toon.getY() <= 165.4 and self.toon.getY() >= 157.9:
                messenger.send('unloadZone')
                messenger.send('loadSpeedway', [(0.353092, 79.5724, 0.0892678, 179.516, 0, 0)])
                return task.done
        return task.cont


class SillyStreet(DirectObject, Town):

    def __init__(self, toon):
        DirectObject.__init__(self)
        Town.__init__(self)
        self.zoneId = Globals.SillyStreetId
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.townStorageDNAFile = 'phase_5/dna/storage_TT_town.xml'
        self.streetDnaFile = 'phase_5/dna/toontown_central_2100.xml'
        self.accept('unloadZone', self.unload)
        self.accept('loadHood', self.loadPlayground)

    def load(self):
        self.loadHood()
        self.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        self.enter()
        base.setCurrentZone(Globals.TTCZone + Globals.StreetZone)

    def unload(self):
        Town.unload(self)
        self.ignoreAll()
        del self.zoneId
        del self.musicFile
        del self.activityMusicFile
        del self.skyFile
        del self.townStorageDNAFile
        del self.streetDnaFile

    def loadPlayground(self, id):
        if id == Globals.ToontownCentralId:
            self.playground = TTC(self.toon)
            self.playground.load()
            self.unload()


class PunchlinePlace(DirectObject, Town):

    def __init__(self, toon):
        DirectObject.__init__(self)
        Town.__init__(self)
        self.zoneId = Globals.PunchlinePlaceId
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.townStorageDNAFile = 'phase_5/dna/storage_TT_town.xml'
        self.streetDnaFile = 'phase_5/dna/toontown_central_2300.xml'
        self.accept('unloadZone', self.unload)
        self.accept('loadHood', self.loadPlayground)

    def load(self):
        self.loadHood()
        self.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        self.enter()
        base.setCurrentZone(Globals.TTCZone + Globals.StreetZone)

    def unload(self):
        Town.unload(self)
        self.ignoreAll()
        del self.zoneId
        del self.musicFile
        del self.activityMusicFile
        del self.skyFile
        del self.townStorageDNAFile
        del self.streetDnaFile

    def loadPlayground(self, id):
        if id == Globals.ToontownCentralId:
            self.playground = TTC(self.toon)
            self.playground.load()
            self.unload()


class LoopyLane(DirectObject, Town):

    def __init__(self, toon):
        DirectObject.__init__(self)
        Town.__init__(self)
        self.zoneId = Globals.LoopyLaneId
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.townStorageDNAFile = 'phase_5/dna/storage_TT_town.xml'
        self.streetDnaFile = 'phase_5/dna/toontown_central_2200.xml'
        self.accept('unloadZone', self.unload)
        self.accept('loadHood', self.loadPlayground)

    def load(self):
        self.loadHood()
        self.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        self.enter()
        base.setCurrentZone(Globals.TTCZone + Globals.StreetZone)

    def unload(self):
        Town.unload(self)
        self.ignoreAll()
        del self.zoneId
        del self.musicFile
        del self.activityMusicFile
        del self.skyFile
        del self.townStorageDNAFile
        del self.streetDnaFile

    def loadPlayground(self, id):
        if id == Globals.ToontownCentralId:
            self.playground = TTC(self.toon)
            self.playground.load()
            self.unload()
