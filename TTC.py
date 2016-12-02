from pandac.PandaModules import *
from direct.task import Task
from DNALoader import *

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
        dna = DNALoader(self.storageFile, self.pgStorageFile, self.szStorageFile, self.szDNAFile)
        self.ttc = dna.returnGeom()
        self.ttc.reparentTo(render)
        self.ls.tick()
        bank = self.ttc.find('**/*toon_landmark_TT_bank_DNARoot')
        doorTrigger = bank.find('**/door_trigger*')
        doorTrigger.setY(doorTrigger.getY() - 1.5)
        if sky == 1:
            pass
        else:
            self.setupSky()
        self.ls.tick()
        self.music = base.loadMusic("phase_4/audio/bgm/TC_nbrhood.ogg")
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.sillyStreet, 'sillyStreet')
        base.taskMgr.add(self.punchlinePlace, 'punchlinePlace')
        base.taskMgr.add(self.loopyLane, 'loopyLane')
        base.taskMgr.add(self.goofySpeedway, 'goofySpeedway')
        self.ls.end()

    def setupSky(self):
        self.sky = loader.loadModel("phase_3.5/models/props/TT_sky.bam")
        self.sky.reparentTo(render)
        self.sky.setScale(5, 5, 5)
        Clouds1 = self.sky.find("**/cloud1")
        Clouds2 = self.sky.find("**/cloud2")
        Clouds1.setScale(0.6, 0.6, 0.6)
        Clouds2.setScale(0.9, 0.9, 0.9)
        Clouds1Spin = Clouds1.hprInterval(360, Vec3(60, 0, 0))
        Clouds1Spin.loop()
        Clouds2Spin = Clouds2.hprInterval(360, Vec3(-60, 0, 0))
        Clouds2Spin.loop()
        Clouds1.setTransparency(TransparencyAttrib.MBinary, 1)
        Clouds2.setTransparency(TransparencyAttrib.MBinary, 1)

    def unload(self):
        base.taskMgr.remove('sillyStreet')
        base.taskMgr.remove('punchlinePlace')
        base.taskMgr.remove('loopyLane')
        base.taskMgr.remove('goofySpeedway')
        self.music.stop()
        del self.music
        self.ttc.removeNode()
        del self.ttc

    def goofySpeedway(self, task):
        if self.toon.getX() <= 166.5 and self.toon.getX() >= 156:
            if self.toon.getY() <= -19.5 and self.toon.getY() >= -35.5:
                loadingScreen = LoadingScreen()
                loadingScreen.begin(100)
                self.unload()
                loadingScreen.tick()
                self.toon.setPosHpr(0.353092, 79.5724, 0.0892678, 179.516, 0, 0)
                GoofySpeedway(self.toon).load()
                loadingScreen.end()
                return task.done
        return task.cont

    def sillyStreet(self, task):
        if self.toon.getX() <= -155 and self.toon.getX() >= -164:
            loadingScreen = LoadingScreen()
            loadingScreen.begin(100)
            self.unload()
            loadingScreen.tick()
            self.toon.setPos(-90.8546, -100.658, -0.475494)
            self.toon.setHpr(92.6896, 0, 0)
            SillyStreet(self.toon).load()
            loadingScreen.end()
            return task.done
        else:
            return task.cont

    def punchlinePlace(self, task):
        if self.toon.getX() <= 102 and self.toon.getX() >= 100:
            if self.toon.getY() <= 54 and self.toon.getY() >= 37:
                loadingScreen = LoadingScreen()
                loadingScreen.begin(100)
                self.unload()
                loadingScreen.tick()
                self.toon.setPos(4.39313, 22.2804, -0.478364)
                self.toon.setHpr(269.45, 0, 0)
                PunchlinePlace(self.toon).load()
                loadingScreen.end()
                return task.done
        return task.cont

    def loopyLane(self, task):
        if self.toon.getX() <= 12 and self.toon.getX() >= -4:
            if self.toon.getY() <= 154 and self.toon.getY() >= 153:
                loadingScreen = LoadingScreen()
                loadingScreen.begin(100)
                self.unload()
                loadingScreen.tick()
                self.toon.setPos(-76.0011, 96.14, -0.47921)
                self.toon.setHpr(-271.592, 0, 0)
                LoopyLane(self.toon).load()
                loadingScreen.end()
                return task.done
        return task.cont

class SillyStreet:

    def __init__(self, toon):
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.streetFile = "phase_15/street/TTC_silly_street"
        self.street = None

    def load(self):
        self.street = loader.loadModel(self.streetFile)
        self.street.reparentTo(render)
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.ttc, 'ttcTunnel')

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.music.stop()
        del self.music
        self.street.removeNode()
        del self.street

    def ttc(self, task):
        if self.toon.getX() <= -83 and self.toon.getX() >= -85:
            if self.toon.getY() <= -91 and self.toon.getY() >= -108:
                ls = LoadingScreen()
                ls.begin(100)
                self.unload()
                ls.tick()
                TTC(self.toon, (-151.514, -32.8979, 3.02421, 247.186, 0, 0)).load()
                ls.end()
                return task.done
        return task.cont

class PunchlinePlace:

    def __init__(self, toon):
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.streetFile = "phase_15/street/TTC_punchline_place"
        self.street = None

    def load(self):
        self.street = loader.loadModel(self.streetFile)
        self.street.reparentTo(render)
        self.music = base.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.ttc, 'ttcTunnel')

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.music.stop()
        del self.music
        self.street.removeNode()
        del self.street

    def ttc(self, task):
        if self.toon.getX() <= -4.5 and self.toon.getX() >= -5:
            if self.toon.getY() <= 29 and self.toon.getY() >= 12:
                ls = LoadingScreen()
                ls.begin(100)
                self.unload()
                ls.tick()
                TTC(self.toon, (91.4972, 43.8591, 0.522909, 440.311, 0, 0)).load()
                ls.end()
                return task.done
        return task.cont

class LoopyLane:

    def __init__(self, toon):
        self.toon = toon
        self.musicFile = "phase_3.5/audio/bgm/TC_SZ.ogg"
        self.music = None
        self.streetFile = "phase_15/street/TTC_loopy_lane"
        self.street = None

    def load(self):
        self.street = loader.loadModel(self.streetFile)
        self.street.reparentTo(render)
        self.music = base.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.ttc, 'ttcTunnel')

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.music.stop()
        del self.music
        self.street.removeNode()
        del self.street

    def ttc(self, task):
        if self.toon.getX() <= -72 and self.toon.getX() >= -73:
            if self.toon.getY() <= 103 and self.toon.getY() >= 87.5:
                ls = LoadingScreen()
                ls.begin(100)
                self.unload()
                ls.tick()
                TTC(self.toon, (6.59755, 144.358, 0.519495, -183.679, 0, 0)).load()
                ls.end()
                return task.done
        return task.cont

class GoofySpeedway:

    def __init__(self, toon):
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/GS_SZ.ogg"
        self.music = None
        self.streetFile = "phase_6/models/karting/GasolineAlley_TT"
        self.street = None

    def load(self):
        self.street = loader.loadModel(self.streetFile)
        self.street.reparentTo(render)
        self.street.setPosHpr(0, 0, 0, 0, 0, 0)
        self.tunnel = loader.loadModel('phase_3.5/models/modules/safe_zone_entrance_tunnel_TT')
        self.tunnel.setPosHpr(-20, 78.1, 0.56, 0, 0, 0)
        self.tunnel.reparentTo(self.street)
        self.music = loader.loadMusic(self.musicFile)
        base.playMusic(self.music, looping=1)
        base.taskMgr.add(self.ttc, 'ttcTunnel')

    def unload(self):
        base.taskMgr.remove('ttcTunnel')
        self.music.stop()
        del self.music
        self.street.removeNode()
        del self.street

    def ttc(self, task):
        if self.toon.getX() <= 8.5 and self.toon.getX() >= -8.5:
            if self.toon.getY() <= 85.2 and self.toon.getY() >= 85.1:
                ls = LoadingScreen()
                ls.begin(100)
                self.unload()
                ls.tick()
                TTC(self.toon, (153.96, -33.3484, 3.0229, 118.076, 0, 0)).load()
                ls.end()
                return task.done
        return task.cont