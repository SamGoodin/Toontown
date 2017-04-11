import random
from direct.showbase.DirectObject import DirectObject
import Globals
from dna.DNALoader import *
from hood.places.Hood import Hood
from gui.Boat import Boat
from direct.task.Task import Task

SpawnPoints = [
    [-28, -2.5, 5.8, 120, 0, 0],
    [-22, 13, 5.8, 155.6, 0, 0],
    [67, 47, 5.7, 134.7, 0, 0],
    [62, 19, 5.7, 97, 0, 0],
    [66, -27, 5.7, 80.5, 0, 0],
    [-114, -7, 5.7, -97, 0, 0],
    [-108, 36, 5.7, -153.8, 0, 0],
    [-116, -46, 5.7, -70.1, 0, 0],
    [-63, -79, 5.7, -41.2, 0, 0],
    [-2, -79, 5.7, 57.4, 0, 0],
    [-38, -78, 5.7, 9.1, 0, 0]
]


class DDock(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/DD_nbrhood.ogg"
        self.sky = None
        self.skyFile = "phase_3.5/models/props/BR_sky"
        self.dna = None
        self.pgStorageFile = 'phase_6/dna/storage_DD.pdna'
        self.szStorageFile = 'phase_6/dna/storage_DD_sz.pdna'
        self.szDNAFile = 'phase_6/dna/donalds_dock_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (0.8, 0.6, 0.5, 1.0)
        self.titleText = "Donald's Dock"
        self.fog = Fog('DDFog')

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
        base.setCurrentZone(Globals.DDZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        self.fog.setColor(self.whiteFogColor)
        self.fog.setLinearRange(0, 400)
        render.clearFog()
        render.setFog(self.fog)
        self.sky.sky.clearFog()
        self.sky.sky.setFog(self.fog)
        self.seagullSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        water = self.playground.find('**/water')
        water.setTransparency(1)
        water.setColor(1, 1, 1, 0.8)
        self.boat = self.playground.find('**/donalds_boat')
        if self.boat.isEmpty():
            self.notify.error('Boat not found')
        else:
            wheel = self.boat.find('**/wheel')
            if wheel.isEmpty():
                self.notify.warning('Wheel not found')
            else:
                wheel.hide()
            self.boat.stash()
        self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')
        self.boatClass = Boat(self.boat, self.playground)
        self.boatClass.generateBoat()
        self.nextSeagullTime = 0
        taskMgr.add(self.__seagulls, 'dd-seagulls')

    def __seagulls(self, task):
        if task.time < self.nextSeagullTime:
            return Task.cont
        base.playSfx(self.seagullSound)
        self.nextSeagullTime = task.time + random.random() * 4.0 + 8.0
        return Task.cont

    def unload(self):
        Hood.unload(self)
        taskMgr.remove('dd-seagulls')
        render.clearFog()
        self.sky.sky.clearFog()
        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound
        del self.boat
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')


