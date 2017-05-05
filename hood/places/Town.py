import Globals
from gui import SkyUtil
from pandac.PandaModules import *
from hood.folder import ZoneUtil
from direct.interval.IntervalGlobal import *


class Town:
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
        self.skyFile = None
        self.musicFile = None
        self.activityMusicFile = None
        self.battleMusicFile = 'phase_3.5/audio/bgm/encntr_general_bg.ogg'
        self.townStorageDNAFile = None
        self.streetDnaFile = None

    def enter(self):
        base.playMusic(self.music, looping=1, volume=0.8)
        self.geom.reparentTo(render)
        base.toon.setGeom(self.geom)
        base.toon.setOnLevelGround(1)
        self.startSky()
        loader.endBulkLoad('town')
        #TODO: idk

    def finishLoad(self):
        self.music = base.loadMusic(self.musicFile)
        self.activityMusic = base.loadMusic(self.activityMusicFile)
        self.battleMusic = base.loadMusic(self.battleMusicFile)
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setTag('sky', 'Regular')
        self.sky.setScale(1.0)
        self.sky.setFogOff()

    def startSky(self):
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
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
        messenger.send('loadHood', [streetId])

    def getPhaseFromHood(self, hoodId):
        hoodId = ZoneUtil.getStreetName(hoodId)
        return hoodId

    def unload(self):
        self.music.stop()
        del self.battleMusic
        del self.music
        del self.activityMusic
        del self.holidayPropTransforms
        self.deleteAnimatedProps()
        self.stopSky()
        del self.sky
        self.geom.removeNode()
        del self.geom

    def loadHood(self):
        title = Globals.GlobalStreetNames.get(self.zoneId)
        loader.beginBulkLoad('town', "Heading to " + title[2], 6, 1, Globals.TIP_GENERAL)
        loader.loadDNA('phase_5/dna/storage_town.xml').store(base.dnaStore)
        loader.loadDNA(self.townStorageDNAFile).store(base.dnaStore)
        sceneTree = loader.loadDNA(self.streetDnaFile)
        node = sceneTree.generate(base.dnaStore)
        base.dnaData = sceneTree.generateData()
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(sceneTree)
        self.reparentLandmarkBlockNodes()
        self.renameFloorPolys(self.nodeList)
        self.createAnimatedProps(self.nodeList)
        self.holidayPropTransforms = {}
        npl = self.geom.findAllMatches('**/=DNARoot=holiday_prop')
        for i in range(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()

        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.setName('town_top_level')
        self.finishLoad()

    def reparentLandmarkBlockNodes(self):
        bucket = self.landmarkBlocks = hidden.attachNewNode('landmarkBlocks')
        npc = self.geom.findAllMatches('**/sb*:*_landmark_*_DNARoot')
        for i in range(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

        npc = self.geom.findAllMatches('**/sb*:*animated_building*_DNARoot')
        for i in range(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]

    def makeDictionaries(self, sceneTree):
        self.nodeDict = {}
        self.zoneDict = {}
        self.nodeToZone = {}
        self.nodeList = []
        self.fadeInDict = {}
        self.fadeOutDict = {}
        a1 = Vec4(1, 1, 1, 1)
        a0 = Vec4(1, 1, 1, 0)
        for visgroup in base.dnaData.visgroups:
            groupName = self.extractGroupName(visgroup.name)
            zoneId = int(groupName)
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            groupNode = self.geom.find('**/' + visgroup.name)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            else:
                if ':' in groupName:
                    groupName = '%s%s' % (zoneId, groupName[groupName.index(':'):])
                else:
                    groupName = '%s' % zoneId
                groupNode.setName(groupName)
            self.nodeDict[zoneId] = []
            self.nodeList.append(groupNode)
            self.zoneDict[zoneId] = groupNode
            self.nodeToZone[groupNode] = zoneId
            fadeDuration = 0.5
            self.fadeOutDict[groupNode] = Sequence(Func(groupNode.setTransparency, 1),
                                                   LerpColorScaleInterval(groupNode, fadeDuration, a0,
                                                                          startColorScale=a1),
                                                   Func(groupNode.clearColorScale), Func(groupNode.clearTransparency),
                                                   Func(groupNode.stash), name='fadeZone-' + str(zoneId), autoPause=1)
            self.fadeInDict[groupNode] = Sequence(Func(groupNode.unstash), Func(groupNode.setTransparency, 1),
                                                  LerpColorScaleInterval(groupNode, fadeDuration, a1,
                                                                         startColorScale=a0),
                                                  Func(groupNode.clearColorScale), Func(groupNode.clearTransparency),
                                                  name='fadeZone-' + str(zoneId), autoPause=1)

        for visgroup in base.dnaData.visgroups:
            zoneId = int(self.extractGroupName(visgroup.name))
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            for visName in visgroup.vis:
                groupName = self.extractGroupName(visName)
                nextZoneId = int(groupName)
                nextZoneId = ZoneUtil.getTrueZoneId(nextZoneId, self.zoneId)
                visNode = self.zoneDict[nextZoneId]
                self.nodeDict[zoneId].append(visNode)

    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in range(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)

    def createAnimatedProps(self, nodeList):
        self.animPropDict = {}
        self.zoneIdToInteractivePropDict = {}
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in range(numAnimPropNodes):
                animPropNode = animPropNodes.getPath(j)
                if animPropNode.getName().startswith('animated_prop_generic'):
                    className = 'GenericAnimatedProp'
                elif animPropNode.getName().startswith('animated_prop_'):
                    name = animPropNode.getName()[len('animated_prop_'):]
                    splits = name.split('_')
                    className = splits[0]
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
                className = 'InteractiveAnimatedProp'
                if 'hydrant' in interactivePropNode.getName():
                    className = 'HydrantInteractiveProp'
                elif 'trashcan' in interactivePropNode.getName():
                    className = 'TrashcanInteractiveProp'
                elif 'mailbox' in interactivePropNode.getName():
                    className = 'MailboxInteractiveProp'
                symbols = {}
                Globals.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                interactivePropObj = classObj(interactivePropNode)
                animPropList = self.animPropDict.get(i)
                if animPropList is None:
                    animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(interactivePropObj)
                if interactivePropObj.getCellIndex() == 0:
                    zoneId = int(i.getName())
                    if zoneId not in self.zoneIdToInteractivePropDict:
                        self.zoneIdToInteractivePropDict[zoneId] = interactivePropObj
                    else:
                        self.notify.error(
                            'already have interactive prop %s in zone %s' % (self.zoneIdToInteractivePropDict, zoneId))

            animatedBuildingNodes = i.findAllMatches('**/*:animated_building_*;-h')
            for np in animatedBuildingNodes:
                if np.getName().startswith('sb'):
                    animatedBuildingNodes.removePath(np)

            numAnimatedBuildingNodes = animatedBuildingNodes.getNumPaths()
            for j in range(numAnimatedBuildingNodes):
                animatedBuildingNode = animatedBuildingNodes.getPath(j)
                className = 'GenericAnimatedBuilding'
                symbols = {}
                Globals.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                animatedBuildingObj = classObj(animatedBuildingNode)
                animPropList = self.animPropDict.get(i)
                if animPropList is None:
                    animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animatedBuildingObj)

        return

    def deleteAnimatedProps(self):
        for zoneNode, animPropList in self.animPropDict.items():
            for animProp in animPropList:
                animProp.delete()

        del self.animPropDict