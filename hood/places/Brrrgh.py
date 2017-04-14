import random
from direct.showbase.DirectObject import DirectObject
import Globals
from hood.places.Hood import Hood
from battle import BattleParticles
from direct.task.Task import Task

SpawnPoints = [
    [35, -32, 6.2, 138, 0, 0],
    [26, -105, 6.2, -339, 0, 0],
    [-29, -139, 6.2, -385, 0, 0],
    [-79, -123, 6.2, -369, 0, 0],
    [-114, -86, 3, -54, 0, 0],
    [-136, 9, 6.2, -125, 0, 0],
    [-75, 92, 6.2, -187, 0, 0],
    [-7, 75, 6.2, -187, 0, 0],
    [-106, -42, 8.6, -111, 0, 0],
    [-116, -44, 8.3, -20, 0, 0]
]


class Brrrgh(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_8/audio/bgm/TB_nbrhood.ogg"
        self.sky = None
        self.skyFile = 'phase_3.5/models/props/BR_sky'
        self.dna = None
        self.pgStorageFile = 'phase_8/dna/storage_BR.pdna'
        self.szStorageFile = 'phase_8/dna/storage_BR_sz.pdna'
        self.szDNAFile = 'phase_8/dna/the_burrrgh_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (0.3, 0.6, 1.0, 1.0)
        self.titleText = "The Brrrgh"

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
        base.setCurrentZone(Globals.BRZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        self.windSound = map(base.loadSfx, ['phase_8/audio/sfx/SZ_TB_wind_1.ogg',
                                            'phase_8/audio/sfx/SZ_TB_wind_2.ogg',
                                            'phase_8/audio/sfx/SZ_TB_wind_3.ogg'])
        taskMgr.doMethodLater(1, self.__windTask, 'BR-wind')
        self.snow = BattleParticles.loadParticleFile('snowdisk.ptf')
        self.snow.setPos(0, 0, 5)
        self.snowRender = self.playground.attachNewNode('snowRender')
        self.snowRender.setDepthWrite(0)
        self.snowRender.setBin('fixed', 1)
        self.snow.start(camera, self.snowRender)

    def __windTask(self, task):
        base.playSfx(random.choice(self.windSound))
        time = random.random() * 8.0 + 1
        taskMgr.doMethodLater(time, self.__windTask, 'BR-wind')
        return Task.done

    def unload(self):
        Hood.unload(self)
        self.snow.cleanup()
        self.snowRender.removeNode()
        taskMgr.remove('BR-wind')
        del self.windSound
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')
