from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.toon = Toon()

class Toon(Actor):

    def __init__(self):
        Actor.__init__(self, None, None, other=None, flattenable=0, setFinal=1)
        self.createActor()

    def createActor(self):
        print 'dad'
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 20)
        levelOneOut = base.config.GetInt('lod1-out', 0)
        levelTwoIn = base.config.GetInt('lod2-in', 80)
        levelTwoOut = base.config.GetInt('lod2-out', 20)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 80)
        self.addLOD(1000, levelOneIn, levelOneOut)
        # self.addLOD(500, levelTwoIn, levelTwoOut)
        # self.addLOD(250, levelThreeIn, levelThreeOut)
        self.loadModel(head, 'head', '1000', True)
        self.loadModel(torso, 'torso', '1000', True)
        self.loadModel(legs, 'legs', '1000', True)
        self.showPart('head', '1000')
        self.showPart('torso', '1000')
        self.showPart('legs', '1000')
        self.loadAnims(LegsAnimDict[legsName], 'legs', '1000')
        self.loadAnims(TorsoAnimDict[torsoName], 'torso', '1000')
        if headName:
            self.loadAnims(HeadAnimDict[headName], 'head', '1000')
        self.findAllMatches('**/boots_short').stash()
        self.findAllMatches('**/boots_long').stash()
        self.findAllMatches('**/shoes').stash()

game = Window()
game.run()