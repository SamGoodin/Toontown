from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.dnaStorage = None
        self.prop = None

    def loadDNAFile(self, dnaStorage, file):
        #self.loadDNAFileBase(dnaStorage, file)
        nodePath = NodePath(PandaNode('dna'))
        self.prop.traverse(nodePath, self.dnaStorage)
        return nodePath

Game().run()