from pandac.PandaModules import *
from direct.task import Task
from DNALoader import *
import Sky

import random
from direct.showbase.DirectObject import DirectObject
from LoadingScreen import LoadingScreen

SpawnPoints = [
    (-60, -8, 1.3, -90, 0, 0),
    (-66, -9, 1.3, -274, 0, 0),
    (17, -28, 4.1, -44, 0, 0),
    (87.7, -22, 4, 66, 0, 0),
    (-9.6, 61.1, 0, 176.253, 0, 0),
    (-109.0, -2.5, -1.656, -90, 0, 0),
    (95.2458, -140.175, 2.5, -11.9715, 0, 0),
    (25, 123.4, 2.55, 272, 0, 0),
    (48, 39, 4, 201, 0, 0),
    (-80, -61, 0.1, -265, 0, 0),
    (-46.875, 43.68, -1.05, 124, 0, 0),
    (34, -105, 2.55, 45, 0, 0),
    (16, -75, 2.55, 56, 0, 0),
    (-27, -56, 0.1, 45, 0, 0),
    (-70, 4.6, -1.9, 90, 0, 0)
]

class TTC(DirectObject):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.accept('tick', self.tick)
        self.toon = toon
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.storageFile = 'phase_4/dna/storage.pdna'
        self.pgStorageFile = 'phase_4/dna/storage_TT.pdna'
        self.szStorageFile = 'phase_4/dna/storage_TT_sz.pdna'
        self.szDNAFile = 'phase_4/dna/toontown_central_sz.pdna'
        base.cTrav = CollisionTraverser()
        base.camera.hide()
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])

    def tick(self):
        self.ls.tick()

    def load(self, sky=1):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorageFile, None, self.szStorageFile, self.szDNAFile)
        self.ttc = self.dna.returnGeom()
        self.ttc.reparentTo(render)
        self.ls.tick()
        bank = self.ttc.find('**/*toon_landmark_TT_bank_DNARoot')
        doorTrigger = bank.find('**/door_trigger*')
        doorTrigger.setY(doorTrigger.getY() - 1.5)
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = base.loadMusic("phase_4/audio/bgm/TC_nbrhood.ogg")
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.sillyStreet, 'sillyStreet')
        base.taskMgr.add(self.punchlinePlace, 'punchlinePlace')
        base.taskMgr.add(self.loopyLane, 'loopyLane')
        base.taskMgr.add(self.goofySpeedway, 'goofySpeedway')
        self.ls.end()

    def unload(self):
        base.taskMgr.remove('sillyStreet')
        base.taskMgr.remove('punchlinePlace')
        base.taskMgr.remove('loopyLane')
        base.taskMgr.remove('goofySpeedway')
        self.ignoreAll()
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.ttc.removeNode()
        del self.ttc
        self.dna.unload()
        del self.dna
        self.ls.destroy()
        del self.ls

    def goofySpeedway(self, task):
        if self.toon.getX() <= 33.4 and self.toon.getX() >= 20.9:
            if self.toon.getY() <= 165.4 and self.toon.getY() >= 157.9:
                GoofySpeedway(self.toon).load()
                self.unload()
                self.toon.setPosHpr(0.353092, 79.5724, 0.0892678, 179.516, 0, 0)
                return task.done
        return task.cont

    def sillyStreet(self, task):
        if self.toon.getX() <= 35 and self.toon.getX() >= 21:
            if self.toon.getY() <= -155 and self.toon.getY() >= -164:
                SillyStreet(self.toon).load()
                self.unload()
                self.toon.setPosHpr(-91.9644, -100.045, -0.47204, 82.325, 0, 0)
                return task.done
        return task.cont

    def punchlinePlace(self, task):
        if self.toon.getX() <= -36 and self.toon.getX() >= -54:
            if self.toon.getY() <= 102 and self.toon.getY() >= 99:
                PunchlinePlace(self.toon).load()
                self.unload()
                self.toon.setPos(4.39313, 22.2804, -0.478364)
                self.toon.setHpr(269.45, 0, 0)
                return task.done
        return task.cont

    def loopyLane(self, task):
        if self.toon.getX() <= -152 and self.toon.getX() >= -154:
            if self.toon.getY() <= 12.5 and self.toon.getY() >= -4.3:
                LoopyLane(self.toon).load()
                self.unload()
                self.toon.setPos(-76.0011, 96.14, -0.47921)
                self.toon.setHpr(-271.592, 0, 0)
                return task.done
        return task.cont

class SillyStreet(DirectObject):

    def __init__(self, toon):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.storageFile = 'phase_4/dna/storage.pdna'
        self.pgStorage = 'phase_4/dna/storage_TT.pdna'
        self.townStorage = 'phase_5/dna/storage_town.pdna'
        self.streetStorage = 'phase_5/dna/storage_TT_town.pdna'
        self.streetDNAFile = 'phase_5/dna/toontown_central_2100.pdna'

    def tick(self):
        self.ls.tick()

    def load(self):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorage, self.townStorage, self.streetStorage, self.streetDNAFile, 2200)
        self.street = self.dna.returnGeom()
        self.street.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        self.ls.tick()
        base.taskMgr.add(self.ttc, 'ttcTunnel')
        self.ls.end()

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.ignoreAll()
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.street.removeNode()
        del self.street
        self.dna.unload()
        del self.dna
        self.ls.destroy()
        del self.ls

    def ttc(self, task):
        if self.toon.getX() <= -82 and self.toon.getX() >= -84:
            if self.toon.getY() <= -90 and self.toon.getY() >= -109:
                TTC(self.toon, (33.7737, -151.822, 3.02757, -24.1596, 0, 0)).load()
                self.unload()
                return task.done
        return task.cont

class PunchlinePlace(DirectObject):

    def __init__(self, toon):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.storageFile = 'phase_4/dna/storage.pdna'
        self.pgStorage = 'phase_4/dna/storage_TT.pdna'
        self.townStorage = 'phase_5/dna/storage_town.pdna'
        self.streetStorage = 'phase_5/dna/storage_TT_town.pdna'
        self.streetDNAFile = 'phase_5/dna/toontown_central_2300.pdna'

    def tick(self):
        self.ls.tick()

    def load(self):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorage, self.townStorage, self.streetStorage, self.streetDNAFile, 2200)
        self.street = self.dna.returnGeom()
        self.street.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        self.ls.tick()
        base.taskMgr.add(self.ttc, 'ttcTunnel')
        self.ls.end()

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.ignoreAll()
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.street.removeNode()
        del self.street
        self.dna.unload()
        del self.dna
        self.ls.destroy()
        del self.ls

    def ttc(self, task):
        if self.toon.getX() <= -5 and self.toon.getX() >= -6:
            if self.toon.getY() <= 28 and self.toon.getY() >= 12:
                TTC(self.toon, (-47.3624, 92.1697, 0.527566, 172.46, 0, 0)).load()
                self.unload()
                return task.done
        return task.cont

class LoopyLane(DirectObject):

    def __init__(self, toon):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.storageFile = 'phase_4/dna/storage.pdna'
        self.pgStorage = 'phase_4/dna/storage_TT.pdna'
        self.townStorage = 'phase_5/dna/storage_town.pdna'
        self.streetStorage = 'phase_5/dna/storage_TT_town.pdna'
        self.streetDNAFile = 'phase_5/dna/toontown_central_2200.pdna'

    def tick(self):
        self.ls.tick()

    def load(self):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorage, self.townStorage, self.streetStorage, self.streetDNAFile, 2200)
        self.street = self.dna.returnGeom()
        self.street.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        self.ls.tick()
        base.taskMgr.add(self.ttc, 'ttcTunnel')
        self.ls.end()

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.ignoreAll()
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.street.removeNode()
        del self.street
        self.dna.unload()
        del self.dna
        self.ls.destroy()
        del self.ls

    def ttc(self, task):
        if self.toon.getX() <= -69 and self.toon.getX() >= -70.1:
            if self.toon.getY() <= 103 and self.toon.getY() >= 87:
                TTC(self.toon, (-145.759, 4.73623, 0.527567, -86.817, 0, 0)).load()
                self.unload()
                return task.done
        return task.cont

class GoofySpeedway(DirectObject):

    def __init__(self, toon):
        DirectObject.__init__(self)
        self.ls = LoadingScreen()
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/GS_SZ.ogg"
        self.music = None
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.storageFile = 'phase_4/dna/storage.pdna'
        self.pgStorageFile = 'phase_6/dna/storage_GS.pdna'
        self.szStorageFile = 'phase_6/dna/storage_GS_sz.pdna'
        self.szDNAFile = 'phase_6/dna/goofy_speedway_sz.pdna'

    def tick(self):
        self.ls.tick()

    def load(self):
        self.ls.begin(100)
        self.dna = DNALoader(self.storageFile, self.pgStorageFile, None, self.szStorageFile, self.szDNAFile)
        self.street = self.dna.returnGeom()
        self.street.reparentTo(render)
        self.ls.tick()
        self.sky = Sky.Sky()
        self.sky.setupSky(self.skyFile)
        self.ls.tick()
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        self.ls.tick()
        base.taskMgr.add(self.ttc, 'ttcTunnel')
        blimp = self.street.find('**/GS_blimp')
        blimp.setPos(-70, 250, -70)
        blimpBase = NodePath('blimpBase')
        blimpBase.setPos(0, -200, 25)
        blimpBase.setH(-40)
        blimp.reparentTo(blimpBase)
        blimpRoot = NodePath('blimpRoot')
        blimpRoot.setPos(0, -70, 40)
        blimpRoot.reparentTo(self.street)
        blimpBase.reparentTo(blimpRoot)
        self.rotateBlimp = blimpRoot.hprInterval(360, Vec3(360, 0, 0))
        self.rotateBlimp.loop()
        self.ls.end()

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.ignoreAll()
        self.music.stop()
        del self.music
        self.sky.unload()
        del self.sky
        self.street.removeNode()
        del self.street
        self.rotateBlimp.finish()
        del self.rotateBlimp
        self.dna.unload()
        del self.dna
        self.ls.destroy()
        del self.ls

    def ttc(self, task):
        if self.toon.getX() <= 8.3 and self.toon.getX() >= -8.3:
            if self.toon.getY() <= 83.5 and self.toon.getY() >= 83.2:
                TTC(self.toon, (31.0937, 153.423, 3.02421, -149.957, 0, 0)).load()
                self.unload()
                return task.done
        return task.cont