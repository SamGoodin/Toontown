from direct.showbase.ShowBase import ShowBase
from DNAParser import *
from DNAStorage import *

class Test(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.dnaStore = DNAStorage("phase_4/dna/storage_TT.pdna")
        dnaBulk = DNABulkLoader("phase_4/dna/storage_TT.pdna", "phase_4/dna/storage_TT_sz.pdna")
        dnaBulk.loadDNAFiles()
        node = loadDNAFile("phase_4/dna/storage_TT.pdna", 'phase_4/dna/toontown_central_sz.pdna')
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries("phase_4/dna/storage_TT.pdna")
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

    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        for i in xrange(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = base.cr.hoodMgr.extractGroupName(groupFullName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            groupNode.flattenMedium()
            self.nodeList.append(groupNode)

        self.removeLandmarkBlockNodes()

    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in xrange(npc.getNumPaths()):
            npc.getPath(i).removeNode()

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
                base.cr.importModule(symbols, 'toontown.hood', [className])
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
                base.cr.importModule(symbols, 'toontown.hood', [className])
                classObj = getattr(symbols[className], className)
                interactivePropObj = classObj(interactivePropNode)
                animPropList = self.animPropDict.get(i)
                if animPropList is None:
                    animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(interactivePropObj)

        return