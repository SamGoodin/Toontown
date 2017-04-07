import random
from direct.showbase.DirectObject import DirectObject
import Globals
from dna.DNALoader import *
from hood.places.Hood import Hood

SpawnPoints = [
    [-0.7, 62, 0.08, 182, 0, 0],
    [-1, -30, 0.06, 183, 0, 0],
    [-13, -120, 0, 307, 0, 0],
    [16.4, -120, 0, 65, 0, 0],
    [-0.5, -90, 0, 182, 0, 0],
    [-30, -25, -0.373, 326, 0, 0],
    [29, -17, -0.373, 32, 0, 0]
]

class GoofySpeedway(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/GS_SZ.ogg"
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.storageFile = 'Resources/phase_4/dna/storage.pdna'
        self.pgStorageFile = 'Resources/phase_6/dna/storage_GS.pdna'
        self.szStorageFile = 'Resources/phase_6/dna/storage_GS_sz.pdna'
        self.szDNAFile = 'Resources/phase_6/dna/goofy_speedway_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
        self.titleText = "Goofy Speedway"

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
        base.setCurrentZone(Globals.GSZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        base.taskMgr.add(self.ttc, 'ttcTunnel')
        blimp = self.playground.find('**/GS_blimp')
        blimp.setPos(-70, 250, -70)
        blimpBase = NodePath('blimpBase')
        blimpBase.setPos(0, -200, 25)
        blimpBase.setH(-40)
        blimp.reparentTo(blimpBase)
        blimpRoot = NodePath('blimpRoot')
        blimpRoot.setPos(0, -70, 40)
        blimpRoot.reparentTo(self.playground)
        blimpBase.reparentTo(blimpRoot)
        self.rotateBlimp = blimpRoot.hprInterval(360, Vec3(360, 0, 0))
        self.rotateBlimp.loop()

    def unload(self):
        Hood.unload(self)
        base.taskMgr.remove('ttcTunnel')
        self.rotateBlimp.finish()
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')

    def ttc(self, task):
        if self.toon.getX() <= 8.3 and self.toon.getX() >= -8.3:
            if self.toon.getY() <= 83.5 and self.toon.getY() >= 83.2:
                messenger.send('unloadZone')
                messenger.send('loadTTC', [(31.0937, 153.423, 3.02421, -149.957, 0, 0)])
                return task.done
        return task.cont