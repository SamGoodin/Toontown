import Globals
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from toon import Toon
from GenderShop import GenderShop
from ColorShop import ColorShop
from BodyShop import BodyShop
from ClothingShop import ClothingShop
from NameShop import NameShop

class MakeAToon:

    def __init__(self):
        self.gs = GenderShop(self)
        self.bs = None
        self.cos = None
        self.cls = None
        self.ns = None
        self.shop = None
        self.toonPosition = None
        self.toonScale = None
        self.toonHpr = None
        self.toonName = None

    def enterMakeAToon(self):
        self.load()
        base.camLens.setMinFov(48.0/(4./3.))
        self.music = base.loadMusic("phase_3/audio/bgm/create_a_toon.ogg")
        base.playMusic(self.music, looping=1)
        camera.setPosHpr(-5.7, -12.3501, 2.15, -24.8499, 2.73, 0)
        self.guiTopBar.show()
        self.guiBottomBar.show()
        self.guiCancelButton.show()
        self.enterGenderShop()

    def enterGenderShop(self):
        self.shop = "gs"
        self.genderWalls.reparentTo(self.squishJoint)
        self.genderProps.reparentTo(self.propJoint)
        self.roomSquishActor.pose('squish', 0)
        self.guiNextButton['state'] = DGG.DISABLED
        self.guiTopBar['text'] = 'Choose  Boy  or  Girl'
        self.guiTopBar['text_fg'] = (1, 0.92, 0.2, 1)
        self.guiTopBar['text_scale'] = 0.18
        base.transitions.fadeIn()
        self.guiNextButton.show()
        self.gs.showButtons()
        self.rotateLeftButton.hide()
        self.rotateRightButton.hide()
        self.guiLastButton.hide()

    def exitGenderShop(self):
        self.gs.exit()
        self.toon = self.gs.getToon()
        self.toonPosition = self.toon.getPos()
        self.toonScale = self.toon.getScale()
        self.toonHpr = self.toon.getHpr()
        self.toonType = self.gs.getAnimalType()
        self.bodyType = self.gs.getBodyType()
        self.legsType = self.gs.getLegsType()

    def enterBodyShop(self):
        self.shop = "bs"
        self.guiTopBar['text'] = "Choose Your Type"
        self.guiTopBar['text_fg'] = (0.0, 0.98, 0.5, 1)
        self.guiTopBar['text_scale'] = 0.18
        self.bs = BodyShop(self, self.toon, self.toonType, self.bodyType, self.legsType)
        self.bs.load()
        self.bs.enter()
        self.guiNextButton.show()
        self.guiLastButton.show()
        self.rotateLeftButton.show()
        self.rotateRightButton.show()
        self.setBackButtonState(DGG.NORMAL)
        self.setNextButtonState(DGG.NORMAL)

    def exitBodyShop(self):
        self.toon = self.bs.exit()

    def enterColorShop(self):
        self.shop = "cos"
        self.guiTopBar['text'] = "Choose Your Color"
        self.guiTopBar['text_fg'] = (0, 1, 1, 1)
        self.guiTopBar['text_scale'] = .18
        self.setBackButtonState(DGG.NORMAL)
        self.setNextButtonState(DGG.NORMAL)
        self.cos = ColorShop(self, self.toonType)
        self.cos.load()
        self.cos.enter(self.toon)

    def exitColorShop(self):
        self.toon = self.cos.exit()

    def enterClothingShop(self):
        self.shop = "cls"
        self.guiTopBar['text'] = "Choose Your Clothes"
        self.guiTopBar['text_fg'] = (1, 0.92, 0.2, 1)
        self.guiTopBar['text_scale'] = 0.16
        self.cls = ClothingShop(self.toon)
        self.cls.load()
        self.cls.enter()
        self.guiNextButton.show()
        self.toon.setScale(self.toonScale)
        self.toon.setPos(self.toonPosition)
        self.toon.setHpr(self.toonHpr)

    def exitClothingShop(self):
        self.toon = self.cls.exit()
        self.cls.unload()

    def enterNameShop(self):
        self.shop = "ns"
        self.guiTopBar['text'] = 'Choose Your Name'
        self.guiTopBar['text_fg'] = (0.0, 0.98, 0.5, 1)
        self.guiTopBar['text_scale'] = 0.15
        self.spotlight.setPos(2, -1.95, 0.41)
        self.toon.setPos(Point3(1.5, -4, 0))
        self.toon.setH(120)
        self.rotateLeftButton.hide()
        self.rotateRightButton.hide()
        self.ns = NameShop()
        self.ns.load()
        self.ns.enter(self.toon, [], 0)
        base.toon = self.toon
        self.guiNextButton.hide()

    def exitNameShop(self):
        self.toonName = self.ns.getToonName()
        self.spotlight.setPos(1.18, -1.27, 0.41)
        self.ns.exit()
        self.ns.unload()

    def load(self):
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        gui.flattenMedium()
        guiAcceptUp = gui.find('**/tt_t_gui_mat_okUp')
        guiAcceptUp.flattenStrong()
        guiAcceptDown = gui.find('**/tt_t_gui_mat_okDown')
        guiAcceptDown.flattenStrong()
        guiCancelUp = gui.find('**/tt_t_gui_mat_closeUp')
        guiCancelUp.flattenStrong()
        guiCancelDown = gui.find('**/tt_t_gui_mat_closeDown')
        guiCancelDown.flattenStrong()
        guiNextUp = gui.find('**/tt_t_gui_mat_nextUp')
        guiNextUp.flattenStrong()
        guiNextDown = gui.find('**/tt_t_gui_mat_nextDown')
        guiNextDown.flattenStrong()
        guiNextDisabled = gui.find('**/tt_t_gui_mat_nextDisabled')
        guiNextDisabled.flattenStrong()
        skipTutorialUp = gui.find('**/tt_t_gui_mat_skipUp')
        skipTutorialUp.flattenStrong()
        skipTutorialDown = gui.find('**/tt_t_gui_mat_skipDown')
        skipTutorialDown.flattenStrong()
        rotateUp = gui.find('**/tt_t_gui_mat_arrowRotateUp')
        rotateUp.flattenStrong()
        rotateDown = gui.find('**/tt_t_gui_mat_arrowRotateDown')
        rotateDown.flattenStrong()
        self.guiTopBar = DirectFrame(relief=None, text='Click the arrows to create your toon.',
                                     text_font=Globals.getSignFont(), text_fg=(0.0, 0.65, 0.35, 1),
                                     text_scale=0.18, text_pos=(0, -0.03), pos=(0, 0, 0.86))
        self.guiTopBar.hide()
        self.guiBottomBar = DirectFrame(relief=None, image_scale=(1.25, 1, 1), pos=(0.01, 0, -0.86))
        self.guiBottomBar.hide()
        self.guiCheckButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiAcceptUp,
                                                                                         guiAcceptDown,
                                                                                         guiAcceptUp,
                                                                                         guiAcceptDown),
                                           image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                           image2_scale=(0.7, 0.7, 0.7), pos=(1.165, 0, -0.018),
                                           text=('', 'Done', 'Done'),
                                           text_font=Globals.getInterfaceFont(), text_scale=0.08,
                                           text_align=TextNode.ARight, text_pos=(0.075, 0.13), text_fg=(1, 1, 1, 1),
                                           text_shadow=(0, 0, 0, 1))
        self.guiCheckButton.setPos(-0.13, 0, 0.13)
        self.guiCheckButton.reparentTo(base.a2dBottomRight)
        self.guiCheckButton.hide()
        self.guiCancelButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiCancelUp,
                                                                                          guiCancelDown,
                                                                                          guiCancelUp,
                                                                                          guiCancelDown),
                                            image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                            image2_scale=(0.7, 0.7, 0.7), pos=(-1.179, 0, -0.011),
                                            text=('', 'Cancel', 'Cancel'),
                                            text_font=Globals.getInterfaceFont(),
                                            text_scale=0.08, text_pos=(0, 0.115),
                                            text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.backToStartMenu)
        self.guiCancelButton.setPos(0.13, 0, 0.13)
        self.guiCancelButton.reparentTo(base.a2dBottomLeft)
        self.guiCancelButton.hide()
        self.guiNextButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiNextUp,
                                                                                        guiNextDown,
                                                                                        guiNextUp,
                                                                                        guiNextDisabled),
                                          image_scale=(0.3, 0.3, 0.3), image1_scale=(0.35, 0.35, 0.35),
                                          image2_scale=(0.35, 0.35, 0.35), pos=(1.165, 0, -0.018),text=('',
                                                                           'Next',
                                                                           'Next',
                                                                           ''),
                                          text_font=Globals.getInterfaceFont(), command=self.goToNextShop,
                                          text_scale=0.08, text_pos=(0, 0.115),
                                          text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
        self.guiNextButton.setPos(-0.13, 0, 0.13)
        self.guiNextButton.reparentTo(base.a2dBottomRight)
        self.guiNextButton.hide()
        self.guiLastButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiNextUp,
                                                                                        guiNextDown,
                                                                                        guiNextUp,
                                                                                        guiNextDown),
                                          image3_color=Vec4(0.5, 0.5, 0.5, 0.75), image_scale=(-0.3, 0.3, 0.3),
                                          image1_scale=(-0.35, 0.35, 0.35), image2_scale=(-0.35, 0.35, 0.35),
                                          pos=(0.825, 0, -0.018), text=('',
                                                                        'Back',
                                                                        'Back',
                                                                        ''),
                                          text_font=Globals.getInterfaceFont(), text_scale=0.08,
                                          text_pos=(0, 0.115), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.goBack)
        self.guiLastButton.setPos(-0.37, 0, 0.13)
        self.guiLastButton.reparentTo(base.a2dBottomRight)
        self.guiLastButton.hide()
        self.rotateLeftButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(rotateUp,
                                                                                           rotateDown,
                                                                                           rotateUp,
                                                                                           rotateDown),
                                             image_scale=(-0.4, 0.4, 0.4), image1_scale=(-0.5, 0.5, 0.5),
                                             image2_scale=(-0.5, 0.5, 0.5), pos=(-0.355, 0, 0.36),)
        self.rotateLeftButton.flattenMedium()
        self.rotateLeftButton.reparentTo(base.a2dBottomCenter)
        self.rotateLeftButton.hide()
        self.rotateLeftButton.bind(DGG.B1PRESS, self.rotateToonLeft)
        self.rotateLeftButton.bind(DGG.B1RELEASE, self.stopToonRotateLeftTask)
        self.rotateRightButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(rotateUp,
                                                                                            rotateDown,
                                                                                            rotateUp,
                                                                                            rotateDown),
                                              image_scale=(0.4, 0.4, 0.4), image1_scale=(0.5, 0.5, 0.5),
                                              image2_scale=(0.5, 0.5, 0.5), pos=(0.355, 0, 0.36))
        self.rotateRightButton.flattenStrong()
        self.rotateRightButton.reparentTo(base.a2dBottomCenter)
        self.rotateRightButton.hide()
        self.rotateRightButton.bind(DGG.B1PRESS, self.rotateToonRight)
        self.rotateRightButton.bind(DGG.B1RELEASE, self.stopToonRotateRightTask)
        gui.removeNode()
        self.roomDropActor = Actor()
        self.roomDropActor.loadModel('phase_3/models/makeatoon/roomAnim_model')
        self.roomDropActor.loadAnims({'drop': 'phase_3/models/makeatoon/roomAnim_roomDrop'})
        self.roomDropActor.reparentTo(render)
        self.dropJoint = self.roomDropActor.find('**/droppingJoint')
        self.roomSquishActor = Actor()
        self.roomSquishActor.loadModel('phase_3/models/makeatoon/roomAnim_model')
        self.roomSquishActor.loadAnims({'squish': 'phase_3/models/makeatoon/roomAnim_roomSquish'})
        self.roomSquishActor.reparentTo(render)
        self.squishJoint = self.roomSquishActor.find('**/scalingJoint')
        self.propSquishActor = Actor()
        self.propSquishActor.loadModel('phase_3/models/makeatoon/roomAnim_model')
        self.propSquishActor.loadAnims({'propSquish': 'phase_3/models/makeatoon/roomAnim_propSquish'})
        self.propSquishActor.reparentTo(render)
        self.propSquishActor.pose('propSquish', 0)
        self.propJoint = self.propSquishActor.find('**/propJoint')
        self.spotlightActor = Actor()
        self.spotlightActor.loadModel('phase_3/models/makeatoon/roomAnim_model')
        self.spotlightActor.loadAnims({'spotlightShake': 'phase_3/models/makeatoon/roomAnim_spotlightShake'})
        self.spotlightActor.reparentTo(render)
        self.spotlightJoint = self.spotlightActor.find('**/spotlightJoint')
        ee = DirectFrame(pos=(-1, 1, 1), frameSize=(-.01, 0.01, -.01, 0.01), frameColor=(0, 0, 0, 0.05), state='normal')
        #ee.bind(DGG.B1PRESS, lambda x, ee=ee: self.toggleSlide())
        self.eee = ee
        self.room = loader.loadModel('phase_3/models/makeatoon/tt_m_ara_mat_room')
        self.room.flattenMedium()
        self.genderWalls = self.room.find('**/genderWalls')
        self.genderWalls.flattenStrong()
        self.genderProps = self.room.find('**/genderProps')
        self.genderProps.flattenStrong()
        self.bodyWalls = self.room.find('**/bodyWalls')
        self.bodyWalls.flattenStrong()
        self.bodyProps = self.room.find('**/bodyProps')
        self.bodyProps.flattenStrong()
        self.colorWalls = self.room.find('**/colorWalls')
        self.colorWalls.flattenStrong()
        self.colorProps = self.room.find('**/colorProps')
        self.colorProps.flattenStrong()
        self.clothesWalls = self.room.find('**/clothWalls')
        self.clothesWalls.flattenMedium()
        self.clothesProps = self.room.find('**/clothProps')
        self.clothesProps.flattenMedium()
        self.nameWalls = self.room.find('**/nameWalls')
        self.nameWalls.flattenStrong()
        self.nameProps = self.room.find('**/nameProps')
        self.nameProps.flattenStrong()
        self.background = self.room.find('**/background')
        self.background.flattenStrong()
        self.background.reparentTo(render)
        self.floor = self.room.find('**/floor')
        self.floor.flattenStrong()
        self.floor.reparentTo(render)
        self.spotlight = self.room.find('**/spotlight')
        self.spotlight.reparentTo(self.spotlightJoint)
        self.spotlight.setColor(1, 1, 1, 0.3)
        self.spotlight.setPos(1.18, -1.27, 0.41)
        self.spotlight.setScale(2.6)
        self.spotlight.setHpr(0, 0, 0)
        smokeSeqNode = SequenceNode('smoke')
        smokeModel = loader.loadModel('phase_3/models/makeatoon/tt_m_ara_mat_smoke')
        smokeFrameList = list(smokeModel.findAllMatches('**/smoke_*'))
        smokeFrameList.reverse()
        for smokeFrame in smokeFrameList:
            smokeSeqNode.addChild(smokeFrame.node())
        smokeSeqNode.setFrameRate(12)
        self.smoke = render.attachNewNode(smokeSeqNode)
        self.smoke.setScale(1, 1, 0.75)
        self.smoke.hide()
        self.gs.load()

    def exit(self):
        base.camLens.setMinFov(52.0 / (4. / 3.))
        self.guiTopBar.hide()
        self.guiBottomBar.hide()
        self.room.reparentTo(hidden)
        self.music.stop()

    def getToon(self):
        return self.toon

    def unload(self):
        self.exit()
        if self.shop == "gs":
            self.gs.unload()
        elif self.shop == "bs":
            self.bs.unload()
        elif self.shop == "cos":
            self.cos.unload()
        elif self.shop == "cls":
            self.exitClothingShop()
        elif self.shop == "ns":
            self.exitNameShop()
        del self.cos
        del self.gs
        del self.bs
        del self.cls
        del self.ns
        del self.toon
        self.guiTopBar.destroy()
        self.guiBottomBar.destroy()
        self.guiCancelButton.destroy()
        self.guiCheckButton.destroy()
        self.eee.destroy()
        self.guiNextButton.destroy()
        self.guiLastButton.destroy()
        self.rotateLeftButton.destroy()
        self.rotateRightButton.destroy()
        del self.guiTopBar
        del self.guiBottomBar
        del self.guiCancelButton
        del self.guiCheckButton
        del self.eee
        del self.guiNextButton
        del self.guiLastButton
        del self.rotateLeftButton
        del self.rotateRightButton
        self.room.removeNode()
        del self.room
        self.genderWalls.removeNode()
        self.genderProps.removeNode()
        del self.genderWalls
        del self.genderProps
        self.bodyWalls.removeNode()
        self.bodyProps.removeNode()
        del self.bodyWalls
        del self.bodyProps
        self.colorWalls.removeNode()
        self.colorProps.removeNode()
        del self.colorWalls
        del self.colorProps
        self.clothesWalls.removeNode()
        self.clothesProps.removeNode()
        del self.clothesWalls
        del self.clothesProps
        self.nameWalls.removeNode()
        self.nameProps.removeNode()
        del self.nameWalls
        del self.nameProps
        self.background.removeNode()
        del self.background
        self.floor.removeNode()
        del self.floor
        self.spotlight.removeNode()
        del self.spotlight
        self.smoke.removeNode()
        del self.smoke
        loader.unloadModel('phase_3/models/gui/create_a_toon_gui')
        loader.unloadModel('phase_3/models/gui/create_a_toon')
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        del self.music

    def backToStartMenu(self):
        self.gs.killToon()
        self.unload()
        messenger.send('StartMenu')

    def goToNextShop(self):
        if self.shop == "gs":
            self.exitGenderShop()
            self.enterBodyShop()
        elif self.shop == "bs":
            self.exitBodyShop()
            self.enterColorShop()
        elif self.shop == "cos":
            self.exitColorShop()
            self.enterClothingShop()
        elif self.shop == "cls":
            self.exitClothingShop()
            self.enterNameShop()

    def getToonName(self):
        return self.toonName

    def goBack(self):
        if self.shop == 'ns':
            self.exitNameShop()
            self.enterClothingShop()
        elif self.shop == 'cls':
            self.exitClothingShop()
            self.enterColorShop()
        elif self.shop == 'cos':
            self.exitColorShop()
            self.enterBodyShop()
        elif self.shop == 'bs':
            self.exitBodyShop()
            self.enterGenderShop()

    def setBackButtonState(self, state):
        self.guiLastButton['state'] = state

    def setNextButtonState(self, state):
        self.guiNextButton['state'] = state

    def rotateToonLeft(self, event):
        taskMgr.add(self.rotateToonLeftTask, 'rotateToonLeftTask')

    def rotateToonLeftTask(self, task):
        self.toon.setH(self.toon.getH() + -1)
        return task.cont

    def stopToonRotateLeftTask(self, event):
        taskMgr.remove('rotateToonLeftTask')

    def rotateToonRight(self, event):
        taskMgr.add(self.rotateToonRightTask, 'rotateToonRightTask')

    def rotateToonRightTask(self, task):
        self.toon.setH(self.toon.getH() - -1)
        return task.cont

    def stopToonRotateRightTask(self, event):
        taskMgr.remove('rotateToonRightTask')
