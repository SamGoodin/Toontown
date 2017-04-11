import random
from direct.showbase.DirectObject import DirectObject
import Globals
from dna.DNALoader import *
from hood.places.Hood import Hood
from direct.actor import Actor
from gui.effects import Bubbles
import copy

SpawnPoints = [
    [-165.8, 108, 0.025, 252, 0, 0],
    [21, 130, 0.16, 170, 0, 0],
    [93, 78.5, 0.23, 112, 0, 0],
    [79, -1.6, 0.75, 163, 0, 0],
    [10, 33, 5.32, 130.379, 0, 0],
    [-200, -42, 0.025, 317.543, 0, 0],
    [-21, -65, 0.335, -18, 0, 0],
    [23, 68.5, 4.51, -22.808, 0, 0]
]


class OutdoorZone(DirectObject, Hood):

    def __init__(self, toon, startPosHpr=1):
        DirectObject.__init__(self)
        Hood.__init__(self)
        self.accept('unloadZone', self.unload)
        self.toon = toon
        self.musicFile = "phase_6/audio/bgm/OZ_SZ.ogg"
        self.sky = None
        self.skyFile = "phase_3.5/models/props/TT_sky"
        self.dna = None
        self.pgStorageFile = 'phase_6/dna/storage_OZ.pdna'
        self.szStorageFile = 'phase_6/dna/storage_OZ_sz.pdna'
        self.szDNAFile = 'phase_6/dna/outdoor_zone_sz.pdna'
        if startPosHpr == 1:
            spawn = random.choice(SpawnPoints)
        else:
            spawn = startPosHpr
        self.toon.setPosHpr(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4], spawn[5])
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
        self.titleText = "Outdoor Zone"

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
        base.setCurrentZone(Globals.OZZone)
        self.enterHood()
        self.ls.end()

    def loadHoodSpecifics(self):
        self.done = 0
        self.geyserTrack = None
        self.__toonTracks = {}
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        geyserPlacer = self.playground.find('**/geyser*')
        waterfallPlacer = self.playground.find('**/waterfall*')
        binMgr = CullBinManager.getGlobalPtr()
        binMgr.addBin('water', CullBinManager.BTFixed, 29)
        binMgr = CullBinManager.getGlobalPtr()
        water = self.playground.find('**/water1*')
        water.setTransparency(1)
        water.setColorScale(1, 1, 1, 1)
        water.setBin('water', 51, 1)
        pool = self.playground.find('**/pPlane5*')
        pool.setTransparency(1)
        pool.setColorScale(1.0, 1.0, 1.0, 1.0)
        pool.setBin('water', 50, 1)
        self.geyserModel = loader.loadModel('phase_6/models/golf/golf_geyser_model')
        self.geyserSound = loader.loadSfx('phase_6/audio/sfx/OZ_Geyser.ogg')
        self.geyserSoundInterval = SoundInterval(self.geyserSound, node=geyserPlacer, listenerNode=base.camera,
                                                 seamlessLoop=False, volume=1.0, cutOff=120)
        self.geyserSoundNoToon = loader.loadSfx('phase_6/audio/sfx/OZ_Geyser_No_Toon.ogg')
        self.geyserSoundNoToonInterval = SoundInterval(self.geyserSoundNoToon, node=geyserPlacer,
                                                       listenerNode=base.camera, seamlessLoop=False, volume=1.0,
                                                       cutOff=120)
        if self.geyserModel:
            self.geyserActor = Actor.Actor(self.geyserModel)
            self.geyserActor.loadAnims({'idle': 'phase_6/models/golf/golf_geyser'})
            self.geyserActor.reparentTo(render)
            self.geyserActor.setPlayRate(8.6, 'idle')
            self.geyserActor.loop('idle')
            self.geyserActor.setDepthWrite(0)
            self.geyserActor.setTwoSided(True, 11)
            self.geyserActor.setColorScale(1.0, 1.0, 1.0, 1.0)
            self.geyserActor.setBin('fixed', 0)
            mesh = self.geyserActor.find('**/mesh_tide1')
            joint = self.geyserActor.find('**/uvj_WakeWhiteTide1')
            mesh.setTexProjector(mesh.findTextureStage('default'), joint, self.geyserActor)
            self.geyserActor.setPos(geyserPlacer.getPos())
            self.geyserActor.setZ(geyserPlacer.getZ() - 100.0)
            self.geyserPos = geyserPlacer.getPos()
            self.geyserPlacer = geyserPlacer
            self.startGeyser()
            base.sfxPlayer.setCutoffDistance(160)
            self.geyserPoolSfx = loader.loadSfx('phase_6/audio/sfx/OZ_Geyser_BuildUp_Loop.ogg')
            self.geyserPoolSoundInterval = SoundInterval(self.geyserPoolSfx, node=self.geyserPlacer,
                                                         listenerNode=base.camera, seamlessLoop=True, volume=1.0,
                                                         cutOff=120)
            self.geyserPoolSoundInterval.loop()
            self.bubbles = Bubbles.Bubbles(self.geyserPlacer, render)
            self.bubbles.renderParent.setDepthWrite(0)
            self.bubbles.start()
        self.collBase = render.attachNewNode('collisionBase')
        self.geyserCollSphere = CollisionSphere(0, 0, 0, 7.5)
        self.geyserCollSphere.setTangible(1)
        self.geyserCollNode = CollisionNode('barrelSphere')
        self.geyserCollNode.setIntoCollideMask(Globals.WallBitmask)
        self.geyserCollNode.addSolid(self.geyserCollSphere)
        self.geyserNodePath = self.collBase.attachNewNode(self.geyserCollNode)
        self.geyserNodePath.setPos(self.geyserPos[0], self.geyserPos[1], self.geyserPos[2] - 100.0)
        self.waterfallModel = loader.loadModel('phase_6/models/golf/golf_waterfall_model')
        if self.waterfallModel:
            self.waterfallActor = Actor.Actor(self.waterfallModel)
            self.waterfallActor.loadAnims({'idle': 'phase_6/models/golf/golf_waterfall'})
            self.waterfallActor.reparentTo(render)
            self.waterfallActor.setPlayRate(3.5, 'idle')
            self.waterfallActor.loop('idle')
            mesh = self.waterfallActor.find('**/mesh_tide1')
            joint = self.waterfallActor.find('**/uvj_WakeWhiteTide1')
            mesh.setTexProjector(mesh.findTextureStage('default'), joint, self.waterfallActor)
        self.waterfallActor.setPos(waterfallPlacer.getPos())

    def startGeyser(self, task=None):
        if hasattr(base, 'DTimer') and base.DTimer:
            self.geyserCycleTime = 20.0
            useTime = base.DTimer.getTime()
            timeToNextGeyser = 20.0 - useTime % 20.0
            taskMgr.doMethodLater(timeToNextGeyser, self.doGeyser, 'geyser Task')
        else:
            taskMgr.doMethodLater(5.0, self.startGeyser, 'start geyser Task')

    def doGeyser(self, task=None):
        if not self.done:
            self.setGeyserAnim()
            useTime = base.DTimer.getTime()
            timeToNextGeyser = 20.0 - useTime % 20.0
            taskMgr.doMethodLater(timeToNextGeyser, self.doGeyser, 'geyser Task')
        return task.done

    def setGeyserAnim(self, task=None):
        if self.done:
            return
        maxSize = 0.4 * random.random() + 0.75
        time = 1.0
        self.geyserTrack = Sequence()
        upPos = Vec3(self.geyserPos[0], self.geyserPos[1], self.geyserPos[2])
        downPos = Vec3(self.geyserPos[0], self.geyserPos[1], self.geyserPos[2] - 8.0)
        avList = []
        avList.append(base.localAvatar)
        self.avList = avList
        playSound = 0
        for av in avList:
            distance = self.geyserPlacer.getDistance(av)
            if distance < 7.0:
                place = base.currentZone
                local = 0
                avPos = av.getPos()
                upToon = Vec3(avPos[0], avPos[1], maxSize * self.geyserPos[2] + 40.0)
                midToon = Vec3(avPos[0], avPos[1], maxSize * self.geyserPos[2] + 30.0)
                downToon = Vec3(avPos[0], avPos[1], self.geyserPos[2])
                returnPoints = [(7, 7),
                                (8, 0),
                                (-8, 3),
                                (-7, 7),
                                (3, -7),
                                (0, 8),
                                (-10, 0),
                                (8, -3),
                                (5, 8),
                                (-8, 5),
                                (-1, 7)]
                pick = int((float(10) - 11.0) / 13.0 % len(returnPoints))
                returnChoice = returnPoints[pick]
                toonReturn = Vec3(self.geyserPos[0] + returnChoice[0], self.geyserPos[1] + returnChoice[1],
                                  self.geyserPos[2] - 1.5)
                topTrack = Sequence()
                av.dropShadow.hide()
                playSound = 1
                if av == base.localAvatar:
                    #base.cr.playGame.getPlace().setState('fishing')
                    #base.localAvatar.setTeleportAvailable(0)
                    #base.localAvatar.collisionsOff()
                    local = 1
                else:
                    #topTrack.delayDeletes = [DelayDelete.DelayDelete(av, 'OZSafeZoneLoader.setGeyserAnim')]
                    av.stopSmooth()
                animTrack = Parallel()
                toonTrack = Sequence()
                toonTrack.append(Wait(0.5))
                animTrack.append(ActorInterval(av, 'jump-idle', loop=1, endTime=11.5 * time))
                animTrack.append(ActorInterval(av, 'neutral', loop=0, endTime=0.25 * time))
                holder = render.attachNewNode('toon hold')
                base.holder = holder
                toonPos = av.getPos(render)
                toonHpr = av.getHpr(render)
                print 'av Pos %s' % av.getPos()
                base.toonPos = toonPos
                holder.setPos(toonPos)
                av.reparentTo(holder)
                av.setPos(0, 0, 0)
                lookAt = 180
                toonH = (lookAt + toonHpr[0]) % 360
                newHpr = Vec3(toonH, toonHpr[1], toonHpr[2])
                if toonH < 180:
                    lookIn = Vec3(0 + lookAt, -30, 0)
                else:
                    lookIn = Vec3(360 + lookAt, -30, 0)
                print 'Camera Hprs toon %s; lookIn %s; final %s' % (newHpr, lookIn, lookIn - newHpr)
                if local == 1:
                    camPosOriginal = camera.getPos()
                    camHprOriginal = camera.getHpr()
                    camParentOriginal = camera.getParent()
                    cameraPivot = holder.attachNewNode('camera pivot')
                    chooseHeading = random.choice([-10.0, 15.0, 40.0])
                    cameraPivot.setHpr(chooseHeading, -20.0, 0.0)
                    cameraArm = cameraPivot.attachNewNode('camera arm')
                    cameraArm.setPos(0.0, -23.0, 3.0)
                    camPosStart = Point3(0.0, 0.0, 0.0)
                    camHprStart = Vec3(0.0, 0.0, 0.0)
                    self.changeCamera(cameraArm, camPosStart, camHprStart)
                    cameraTrack = Sequence()
                    cameraTrack.append(Wait(11.0 * time))
                    cameraTrack.append(Func(self.changeCamera, camParentOriginal, camPosOriginal, camHprOriginal))
                    cameraTrack.start()
                moveTrack = Sequence()
                moveTrack.append(Wait(0.5))
                moveTrack.append(
                    LerpPosInterval(holder, 3.0 * time, pos=upToon, startPos=downToon, blendType='easeOut'))
                moveTrack.append(
                    LerpPosInterval(holder, 2.0 * time, pos=midToon, startPos=upToon, blendType='easeInOut'))
                moveTrack.append(
                    LerpPosInterval(holder, 1.0 * time, pos=upToon, startPos=midToon, blendType='easeInOut'))
                moveTrack.append(
                    LerpPosInterval(holder, 2.0 * time, pos=midToon, startPos=upToon, blendType='easeInOut'))
                moveTrack.append(
                    LerpPosInterval(holder, 1.0 * time, pos=upToon, startPos=midToon, blendType='easeInOut'))
                moveTrack.append(
                    LerpPosInterval(holder, 2.5 * time, pos=toonReturn, startPos=upToon, blendType='easeIn'))
                animTrack.append(moveTrack)
                animTrack.append(toonTrack)
                topTrack.append(animTrack)
                topTrack.append(Func(av.setPos, toonReturn))
                topTrack.append(Func(av.reparentTo, render))
                topTrack.append(Func(holder.removeNode))
                if local == 1:
                    topTrack.append(Func(self.restoreLocal))
                else:
                    topTrack.append(Func(self.restoreRemote, av))
                topTrack.append(Func(self.clearToonTrack, 10))
                self.storeToonTrack(10, topTrack)
                topTrack.start()

        self.geyserTrack.append(Func(self.doPrint, 'geyser start'))
        self.geyserTrack.append(
            Func(self.geyserNodePath.setPos, self.geyserPos[0], self.geyserPos[1], self.geyserPos[2]))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, 2.0 * time, 0.75, 0.01),
                                         LerpPosInterval(self.geyserActor, 2.0 * time, pos=downPos, startPos=downPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, time, maxSize, 0.75),
                                         LerpPosInterval(self.geyserActor, time, pos=upPos, startPos=downPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, 2.0 * time, 0.75, maxSize),
                                         LerpPosInterval(self.geyserActor, 2.0 * time, pos=downPos, startPos=upPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, time, maxSize, 0.75),
                                         LerpPosInterval(self.geyserActor, time, pos=upPos, startPos=downPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, 2.0 * time, 0.75, maxSize),
                                         LerpPosInterval(self.geyserActor, 2.0 * time, pos=downPos, startPos=upPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, time, maxSize, 0.75),
                                         LerpPosInterval(self.geyserActor, time, pos=upPos, startPos=downPos)))
        self.geyserTrack.append(Parallel(LerpScaleInterval(self.geyserActor, 4.0 * time, 0.01, maxSize),
                                         LerpPosInterval(self.geyserActor, 4.0 * time, pos=downPos, startPos=upPos)))
        self.geyserTrack.append(
            Func(self.geyserNodePath.setPos, self.geyserPos[0], self.geyserPos[1], self.geyserPos[2] - 100.0))
        self.geyserTrack.append(Func(self.doPrint, 'geyser end'))
        self.geyserTrack.start()
        if playSound:
            self.geyserSoundInterval.start()
        else:
            self.geyserSoundNoToonInterval.start()

        self.constructionSite = render.attachNewNode('constructionSite')

        self.constructionSiteBlocker = self.constructionSite.attachNewNode(CollisionNode('constructionSiteBlocker'))
        self.constructionSiteBlocker.setPos(-48, -154.5, 0)
        self.constructionSiteBlocker.node().addSolid(CollisionSphere(0, 0, 0, 35))

        self.coneModel = loader.loadModel('phase_3.5/models/props/unpainted_barrier_cone.bam')

        self.cone0 = Actor.Actor(self.coneModel)
        self.cone0.loadAnims({'jumptwist': 'phase_3.5/models/props/barrier_cone_chan_jumptwist.bam'})
        self.cone0.reparentTo(self.constructionSite)
        self.cone0.loop('jumptwist')
        self.cone0.setPos(-43, -142, 0.025)

        self.cone1 = Actor.Actor(self.coneModel)
        self.cone1.loadAnims({'walktrip': 'phase_3.5/models/props/barrier_cone_chan_walktrip.bam'})
        self.cone1.reparentTo(self.constructionSite)
        self.cone1.loop('walktrip')
        self.cone1.setPos(-52, -145, 0.025)

        self.ladder = loader.loadModel('phase_5/models/props/ladder2.bam')
        self.ladder.reparentTo(self.constructionSite)
        self.ladder.setPosHpr(-36.460, -130.828, 0.30, 61, -90, 0)
        self.ladder.find('**/shadow').removeNode()

        self.paintersWantedSign = loader.loadModel('phase_6/models/props/tti_painters_wanted_sign.bam')
        self.paintersWantedSign.reparentTo(self.constructionSite)
        self.paintersWantedSign.setPosHpr(-57, -129.613, 0.025, 160, 0, 0)

        self.constructionSign = loader.loadModel('phase_4/models/props/construction_sign.bam')
        self.constructionSign.reparentTo(self.constructionSite)
        self.constructionSign.setPosHpr(-47.941, -138.724, 0.122, 181, 0, 0)

    def changeCamera(self, newParent, newPos, newHpr):
        camera.reparentTo(newParent)
        camera.setPosHpr(newPos, newHpr)

    def restoreLocal(self, task=None):
        place = base.currentZone
        if place:
            #place.fsm.request('walk')
            pass
        #base.localAvatar.setTeleportAvailable(1)
        #base.localAvatar.collisionsOn()
        base.localAvatar.dropShadow.show()

    def restoreRemote(self, remoteAv, task=None):
        if remoteAv in self.avList:
            remoteAv.startSmooth()
            remoteAv.dropShadow.show()

    def storeToonTrack(self, avId=10, track=None):
        self.clearToonTrack(avId)
        self.__toonTracks[avId] = track

    def clearToonTrack(self, avId=10):
        oldTrack = self.__toonTracks.get(avId)
        if oldTrack:
            oldTrack.pause()
            #DelayDelete.cleanupDelayDeletes(oldTrack)
            del self.__toonTracks[avId]

    def clearToonTracks(self):
        keyList = []
        for key in self.__toonTracks:
            keyList.append(key)

        for key in keyList:
            if key in self.__toonTracks:
                self.clearToonTrack(key)

    def doPrint(self, thing):
        return 0
        print thing

    def unload(self):
        del self.birdSound
        self.done = 1
        self.collBase.removeNode()
        if self.geyserTrack:
            self.geyserTrack.finish()
        self.geyserTrack = None
        self.geyserActor.cleanup()
        self.geyserModel.removeNode()
        self.waterfallActor.cleanup()
        self.waterfallModel.removeNode()
        self.bubbles.destroy()
        del self.bubbles
        self.geyserPoolSoundInterval.finish()
        self.geyserPoolSfx.stop()
        self.geyserPoolSfx = None
        self.geyserPoolSoundInterval = None
        self.geyserSoundInterval.finish()
        self.geyserSound.stop()
        self.geyserSoundInterval = None
        self.geyserSound = None
        self.geyserSoundNoToonInterval.finish()
        self.geyserSoundNoToon.stop()
        self.geyserSoundNoToonInterval = None
        self.geyserSoundNoToon = None
        if hasattr(self, 'constructionSite'):
            self.paintersWantedSign.removeNode()
            self.ladder.removeNode()
            self.cone0.cleanup()
            self.cone1.cleanup()
            self.coneModel.removeNode()
            self.constructionSiteBlocker.removeNode()
            self.constructionSite.removeNode()
            del self.paintersWantedSign
            del self.ladder
            del self.cone0
            del self.cone1
            del self.coneModel
            del self.constructionSiteBlocker
            del self.constructionSite
        self.clearToonTracks()
        Hood.unload(self)
        self.ignoreAll()
        self.dna.unload()
        del self.dna
        self.ignore('unloadZone')
