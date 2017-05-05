from direct.interval.IntervalGlobal import *
from direct.gui import OnscreenText
from panda3d.core import *
import Globals
from gui.LoadingScreen import LoadingScreen
from gui import SkyUtil
from pandac.PandaModules import *
from hood.folder import ZoneUtil


class Hood:
    hoodName2Id = {
        'dd': Globals.DDZone,
        'tt': Globals.TTCZone,
        'br': Globals.BRZone,
        'mm': Globals.MMZone,
        'dg': Globals.DGZone,
        'oz': Globals.OZZone,
        'gs': Globals.GSZone,
        'dl': Globals.DLZone,
        'bosshq': Globals.BBHQ,
        'sellhq': Globals.SBHQ,
        'cashhq': Globals.CBHQ,
        'lawhq': Globals.LBHQ,
        'gz': Globals.GZone
    }

    def __init__(self):
        self.ls = LoadingScreen()
        self.titleColor = None
        self.titleText = None
        self.musicFile = None
        self.skyFile = None
        self.playground = None
        self.dna = None
        self.fog = None
        self.storageDNAFile = None
        self.safeZoneStorageDNAFile = None
        self.notify = directNotify.newCategory('HoodLoader')
        self.whiteFogColor = Vec4(0.8, 0.8, 0.8, 1)

    def loadHood(self):
        loader.beginBulkLoad('hood', 'Toontown', Globals.safeZoneCountMap[self.zoneId], 1, Globals.TIP_GENERAL)
        if self.storageDNAFile:
            loader.loadDNA(self.storageDNAFile).store(base.dnaStore)
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setTag('sky', 'Regular')
        self.sky.setScale(1.0)
        self.sky.setFogOff()
        self.music = base.loadMusic(self.musicFile)

    def createSafeZone(self, dnaFile):
        if self.safeZoneStorageDNAFile:
            loader.loadDNA(self.safeZoneStorageDNAFile).store(base.dnaStore)
        sceneTree = loader.loadDNA(dnaFile)
        node = sceneTree.generate(base.dnaStore)
        base.dnaData = sceneTree.generateData()
        if node.getNumParents() == 1:
            self.playground = NodePath(node.getParent(0))
            self.playground.reparentTo(hidden)
        else:
            self.playground = hidden.attachNewNode(node)
        self.makeDictionaries(sceneTree)
        self.createAnimatedProps(self.nodeList)
        self.holidayPropTransforms = {}
        npl = self.playground.findAllMatches('**/=DNARoot=holiday_prop')
        for i in range(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()

        self.playground.flattenMedium()
        gsg = base.win.getGsg()
        if gsg:
            self.playground.prepareScene(gsg)

    def makeDictionaries(self, sceneTree):
        self.nodeList = []
        for visgroup in base.dnaData.visgroups:
            groupNode = self.playground.find('**/' + visgroup.name)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            self.nodeList.append(groupNode)

        self.removeLandmarkBlockNodes()

    def removeLandmarkBlockNodes(self):
        npc = self.playground.findAllMatches('**/suit_building_origin')
        for i in range(npc.getNumPaths()):
            npc.getPath(i).removeNode()

    def createAnimatedProps(self, nodeList):
        self.animPropDict = {}
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in range(numAnimPropNodes):
                animPropNode = animPropNodes.getPath(j)
                if animPropNode.getName().startswith('animated_prop_generic'):
                    className = 'GenericAnimatedProp'
                else:
                    className = animPropNode.getName()[14:-8]
                symbols = {}
                Globals.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                animPropObj = classObj(animPropNode)
                animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animPropObj)

            interactivePropNodes = i.findAllMatches('**/interactive_prop_*')
            numInteractivePropNodes = interactivePropNodes.getNumPaths()
            for j in range(numInteractivePropNodes):
                interactivePropNode = interactivePropNodes.getPath(j)
                className = 'GenericAnimatedProp'
                symbols = {}
                Globals.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                interactivePropObj = classObj(interactivePropNode)
                animPropList = self.animPropDict.get(i)
                if animPropList is None:
                    animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(interactivePropObj)

        return

    def deleteAnimatedProps(self):
        for zoneNode, animPropList in self.animPropDict.items():
            for animProp in animPropList:
                animProp.delete()

        del self.animPropDict

    def enterAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.enter()

    def exitAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.exit()

    def enterHood(self):
        base.playMusic(self.music, looping=1, volume=0.8)
        self.playground.reparentTo(render)
        lightsOn = LerpColorScaleInterval(self.playground, 0.1, Vec4(1, 1, 1, 1))
        lightsOn.start()
        for i in self.nodeList:
            self.enterAnimatedProps(i)
        self.startSky()
        base.lastPlayground = self.titleText
        base.localData.updateLastPlayground()
        self.titleText = OnscreenText.OnscreenText(self.titleText, fg=self.titleColor, font=Globals.getSignFont(),
                                                   pos=(0, -0.5), scale=0.16, drawOrder=0, mayChange=1)
        self.doSpawnTitleText()
        base.cTrav = CollisionTraverser()
        base.camera.hide()
        self.notify.warning("Hood load successful.")
        base.toon.setGeom(self.playground)
        loader.endBulkLoad('hood')

    def addLinkTunnelHooks(self, hoodPart, nodeList, currentZoneId):
        tunnelOriginList = []
        for i in nodeList:
            linkTunnelNPC = i.findAllMatches('**/linktunnel*')
            for p in range(linkTunnelNPC.getNumPaths()):
                linkTunnel = linkTunnelNPC.getPath(p)
                name = linkTunnel.getName()
                nameParts = name.split('_')
                hoodStr = nameParts[1]
                zoneStr = nameParts[2]
                hoodId = self.getIdFromName(hoodStr)
                zoneId = int(zoneStr)
                hoodId = ZoneUtil.getTrueZoneId(hoodId, currentZoneId)
                zoneId = ZoneUtil.getTrueZoneId(zoneId, currentZoneId)
                linkSphere = linkTunnel.find('**/tunnel_trigger')
                if linkSphere.isEmpty():
                    linkSphere = linkTunnel.find('**/tunnel_sphere')
                if not linkSphere.isEmpty():
                    cnode = linkSphere.node()
                    cnode.setName('tunnel_trigger_' + hoodStr + '_' + zoneStr)
                    cnode.setCollideMask(Globals.WallBitmask | Globals.GhostBitmask)
                else:
                    linkSphere = linkTunnel.find('**/tunnel_trigger_' + hoodStr + '_' + zoneStr)
                    if linkSphere.isEmpty():
                        self.notify.error('tunnel_trigger not found')
                tunnelOrigin = linkTunnel.find('**/tunnel_origin')
                if tunnelOrigin.isEmpty():
                    self.notify.error('tunnel_origin not found')
                tunnelOriginPlaceHolder = render.attachNewNode('toph_' + hoodStr + '_' + zoneStr)
                tunnelOriginList.append(tunnelOriginPlaceHolder)
                tunnelOriginPlaceHolder.setPos(tunnelOrigin.getPos(render))
                tunnelOriginPlaceHolder.setHpr(tunnelOrigin.getHpr(render))
                #hood = base.localAvatar.cr.playGame.hood
                if ZoneUtil.tutorialDict:
                    how = 'teleportIn'
                    tutorialFlag = 1
                else:
                    how = 'tunnelIn'
                    tutorialFlag = 0
                hoodPart.accept('enter' + linkSphere.getName(), hoodPart.handleEnterTunnel,
                                [{'loader': ZoneUtil.getLoaderName(zoneId),
                                  'where': ZoneUtil.getToonWhereName(zoneId),
                                  'how': how,
                                  'hoodId': hoodId,
                                  'zoneId': zoneId,
                                  'shardId': None,
                                  'tunnelOrigin': tunnelOriginPlaceHolder,
                                  'tutorial': tutorialFlag}])

        return tunnelOriginList

    def getIdFromName(self, hoodName):
        id = self.hoodName2Id.get(hoodName)
        if id:
            return id
        else:
            self.notify.error('No such hood name as: %s' % hoodName)
            return None
        return None

    def handleEnterTunnel(self, requestStatus, collEntry):
        streetId = ZoneUtil.getCanonicalBranchZone(requestStatus['zoneId'])
        messenger.send('loadStreet', [streetId])

    def getPhaseFromHood(self, hoodId):
        hoodId = ZoneUtil.getStreetName(hoodId)
        return hoodId

    def unload(self):
        self.music.stop()
        del self.music
        self.stopSky()
        del self.sky
        self.playground.removeNode()
        del self.playground
        del self.titleColor
        del self.titleText
        self.notify.warning("Hood unload successful.")

    def startSky(self):
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setTag('sky', 'Regular')
        self.sky.setScale(1.0)
        self.sky.setFogOff()
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
        self.notify.warning('The sky is: %s' % self.sky)
        SkyUtil.startCloudSky(self)
        self.sky.reparentTo(base.cam)
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)

    def stopSky(self):
        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)

    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    def startMusic(self, musicFile):
        self.music = base.loadMusic(musicFile)
        base.playMusic(self.music, looping=1, volume=0.8)

    def doSpawnTitleText(self):
        self.titleText.show()
        self.titleText.setColor(Vec4(*self.titleColor))
        self.titleText.clearColorScale()
        self.titleText.setFg(self.titleColor)
        seq = Sequence(Wait(0.1), Wait(6.0), self.titleText.colorScaleInterval(0.5, Vec4(1.0, 1.0, 1.0, 0.0)),
                       Func(self.titleText.hide))
        seq.start()
        seq.setAutoFinish(True)
