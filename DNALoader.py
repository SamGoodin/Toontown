from DNAParser import *
from DNAStorage import *
from hood.folder import ZoneUtil
from direct.interval.IntervalGlobal import *

class DNALoader:

    def __init__(self, storage=None, pgStorage=None, townStorage=None, zoneStorage=None, DNA=1, zoneId=None):
        self.dnaStore = DNAStorage()
        if zoneId:
            self.setZoneId(zoneId)
        if storage:
            dnaBulk = DNABulkLoader(self.dnaStore, storage)
            dnaBulk.loadDNAFiles()
        if pgStorage:
            dnaBulkA = DNABulkLoader(self.dnaStore, pgStorage)
            dnaBulkA.loadDNAFiles()
        if townStorage:
            dnaBulkZ = DNABulkLoader(self.dnaStore, townStorage)
            dnaBulkZ.loadDNAFiles()
        if zoneStorage:
            dnaBulk1 = DNABulkLoader(self.dnaStore, zoneStorage)
            dnaBulk1.loadDNAFiles()
        node = loadDNAFile(self.dnaStore, DNA)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        if townStorage:
            self.townLoader()
        else:
            self.safeZoneLoader()

    def safeZoneLoader(self):
        self.makeDictionaries(self.dnaStore)
        self.createAnimatedProps(self.nodeList)
        self.holidayPropTransforms = {}
        npl = self.geom.findAllMatches('**/=DNARoot=holiday_prop')
        for i in xrange(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.flattenMedium()
        for i in self.nodeList:
            self.enterAnimatedProps(i)

    def townLoader(self):
        self.makeTownDictionaries(self.dnaStore)
        self.reparentLandmarkBlockNodes()
        self.renameFloorPolys(self.nodeList)
        self.createTownAnimatedProps(self.nodeList)
        self.holidayPropTransforms = {}
        npl = self.geom.findAllMatches('**/=DNARoot=holiday_prop')
        for i in xrange(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.flattenLight()
        self.geom.setName('town_top_level')

    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    def reparentLandmarkBlockNodes(self):
        bucket = self.landmarkBlocks = hidden.attachNewNode('landmarkBlocks')
        npc = self.geom.findAllMatches('**/sb*:*_landmark_*_DNARoot')
        for i in xrange(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

        npc = self.geom.findAllMatches('**/sb*:*animated_building*_DNARoot')
        for i in xrange(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

    def makeTownDictionaries(self, dnaStore):
        self.nodeDict = {}
        self.zoneDict = {}
        self.zoneVisDict = {}
        self.nodeList = []
        self.fadeInDict = {}
        self.fadeOutDict = {}
        a1 = Vec4(1, 1, 1, 1)
        a0 = Vec4(1, 1, 1, 0)
        numVisGroups = dnaStore.getNumDNAVisGroupsAI()
        for i in xrange(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            visGroup = dnaStore.getDNAVisGroupAI(i)
            groupName = groupFullName.split(':', 1)[0]
            zoneId = int(groupName)
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            else:
                if ':' in groupName:
                    groupName = '%s%s' % (zoneId, groupName[groupName.index(':'):])
                else:
                    groupName = '%s' % zoneId
                groupNode.setName(groupName)
            groupNode.flattenMedium()
            self.nodeDict[zoneId] = []
            self.nodeList.append(groupNode)
            self.zoneDict[zoneId] = groupNode
            visibles = []
            for i in xrange(visGroup.getNumVisibles()):
                visibles.append(int(visGroup.visibles[i]))
            visibles.append(ZoneUtil.getBranchZone(zoneId))
            self.zoneVisDict[zoneId] = visibles
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

        for i in xrange(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            zoneId = int(groupFullName.split(':', 1)[0])
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            for j in xrange(dnaStore.getNumVisiblesInDNAVisGroup(i)):
                visName = dnaStore.getVisibleName(i, j)
                groupName = groupFullName.split(':', 1)[0]
                nextZoneId = int(groupName)
                nextZoneId = ZoneUtil.getTrueZoneId(nextZoneId, self.zoneId)
                visNode = self.zoneDict[nextZoneId]
                self.nodeDict[zoneId].append(visNode)

        self.dnaStore.resetPlaceNodes()
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()

    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in xrange(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)

    def createTownAnimatedProps(self, nodeList):
        self.animPropDict = {}
        self.zoneIdToInteractivePropDict = {}
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in xrange(numAnimPropNodes):
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
                self.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                animPropObj = classObj(animPropNode)
                animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animPropObj)

            interactivePropNodes = i.findAllMatches('**/interactive_prop_*')
            numInteractivePropNodes = interactivePropNodes.getNumPaths()
            for j in xrange(numInteractivePropNodes):
                interactivePropNode = interactivePropNodes.getPath(j)
                className = 'InteractiveAnimatedProp'
                if 'hydrant' in interactivePropNode.getName():
                    className = 'HydrantInteractiveProp'
                elif 'trashcan' in interactivePropNode.getName():
                    className = 'TrashcanInteractiveProp'
                elif 'mailbox' in interactivePropNode.getName():
                    className = 'MailboxInteractiveProp'
                symbols = {}
                self.importModule(symbols, 'hood.folder', [className])
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
            for j in xrange(numAnimatedBuildingNodes):
                animatedBuildingNode = animatedBuildingNodes.getPath(j)
                className = 'GenericAnimatedBuilding'
                symbols = {}
                self.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                animatedBuildingObj = classObj(animatedBuildingNode)
                animPropList = self.animPropDict.get(i)
                if animPropList is None:
                    animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animatedBuildingObj)

        return

    def returnGeom(self):
        return self.geom

    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        for i in xrange(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = groupFullName.split(':', 1)[0]
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            groupNode.flattenMedium()
            self.nodeList.append(groupNode)

        self.removeLandmarkBlockNodes()
        self.dnaStore.resetPlaceNodes()
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()

    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in xrange(npc.getNumPaths()):
            npc.getPath(i).removeNode()

    def importModule(self, dcImports, moduleName, importSymbols):
        module = __import__(moduleName, globals(), locals(), importSymbols)

        if importSymbols:
            if importSymbols == ['*']:
                if hasattr(module, "__all__"):
                    importSymbols = module.__all__
                else:
                    importSymbols = module.__dict__.keys()
            for symbolName in importSymbols:
                if hasattr(module, symbolName):
                    dcImports[symbolName] = getattr(module, symbolName)
                else:
                    raise Exception('Symbol %s not defined in module %s.' % (symbolName, moduleName))
        else:
            components = moduleName.split('.')
            dcImports[components[0]] = module


    def createAnimatedProps(self, nodeList):
        self.animPropDict = {}
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in xrange(numAnimPropNodes):
                animPropNode = animPropNodes.getPath(j)
                if animPropNode.getName().startswith('animated_prop_generic'):
                    className = 'GenericAnimatedProp'
                else:
                    className = animPropNode.getName()[14:-8]
                symbols = {}
                self.importModule(symbols, 'hood.folder', [className])
                classObj = getattr(symbols[className], className)
                animPropObj = classObj(animPropNode)
                animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animPropObj)

            interactivePropNodes = i.findAllMatches('**/interactive_prop_*')
            numInteractivePropNodes = interactivePropNodes.getNumPaths()
            for j in xrange(numInteractivePropNodes):
                interactivePropNode = interactivePropNodes.getPath(j)
                className = 'GenericAnimatedProp'
                symbols = {}
                self.importModule(symbols, 'hood.folder', [className])
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

    def exitAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.exit()

    def enterAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.enter()

    def unload(self):
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        for i in self.nodeList:
            self.exitAnimatedProps(i)
        self.deleteAnimatedProps()
        self.geom.removeNode()
        del self.geom