from DNAParser import *
from DNAStorage import *

class DNALoader:

    def __init__(self, storage, pgStorage, szStorage, szDNA):
        self.dnaStore = DNAStorage()
        dnaBulk = DNABulkLoader(self.dnaStore, storage)
        dnaBulk.loadDNAFiles()
        dnaBulkA = DNABulkLoader(self.dnaStore, pgStorage)
        dnaBulkA.loadDNAFiles()
        dnaBulk1 = DNABulkLoader(self.dnaStore, szStorage)
        dnaBulk1.loadDNAFiles()
        node = loadDNAFile(self.dnaStore, szDNA)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
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