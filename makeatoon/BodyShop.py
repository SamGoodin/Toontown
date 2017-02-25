#Embedded file name: C:\Users\goodisam000\Desktop\Panda3D\BodyShop.py
from pandac.PandaModules import *
from direct.gui.DirectGui import *
import Globals
import random
from toon.Toon import Toon
HeadList = ['cat',
 'dog',
 'rabbit',
 'mouse',
 'duck',
 'pig',
 'horse',
 'bear',
 'monkey']
BodyList = ['dgs', 'dgm', 'dgl']
BodyAnims = {'dgs': {'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_book'},
 'dgm': {'neutral': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_book'},
 'dgl': {'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book'}}
LegsList = ['dgs', 'dgm', 'dgl']
LegsAnims = {'dgs': {'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book'},
 'dgm': {'neutral': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_book'},
 'dgl': {'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral',
         'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_run',
         'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_walk',
         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_leap_zhang',
         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_jump-zhang',
         'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_book'}}

class BodyShop:

    def __init__(self, makeAToon, toon):
        self.makeAToon = makeAToon
        self.toon = toon
        self.headIndex = HeadList.index(self.toon.species)
        self.bodyIndex = BodyList.index(self.toon.torsoStyle)
        self.legsIndex = LegsList.index(self.toon.legStyle)

    def load(self):
        self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
        guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
        shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
        shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
        self.upsellModel = loader.loadModel('phase_3/models/gui/tt_m_gui_ups_mainGui')
        upsellTex = self.upsellModel.find('**/tt_t_gui_ups_banner')
        self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
        self.parentFrame.setPos(-0.36, 0, -0.5)
        self.parentFrame.reparentTo(base.a2dTopRight)
        self.speciesFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6), relief=None, pos=(0, 0, -0.073), hpr=(0, 0, 0), scale=1.3, frameColor=(1, 1, 1, 1), text='Species', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.speciesLButton = DirectButton(parent=self.speciesFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.changeSpeciesLeft)
        self.speciesRButton = DirectButton(parent=self.speciesFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7), image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.changeSpeciesRight)
        self.headFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6), relief=None, pos=(0, 0, -0.3), hpr=(0, 0, 2), scale=0.9, frameColor=(1, 1, 1, 1), text='Head', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.headLButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), extraArgs=[-1])
        self.headRButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7), image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), extraArgs=[1])
        self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(0.6, 0.6, 0.6), relief=None, pos=(0, 0, -0.5), hpr=(0, 0, -2), scale=0.9, frameColor=(1, 1, 1, 1), text='Body', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.torsoLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.changeBodyLeft)
        self.torsoRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7), image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.changeBodyRight)
        self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6), relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=0.9, frameColor=(1, 1, 1, 1), text='Legs', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.changeLegsLeft)
        self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7), image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.changeLegsRight)
        self.parentFrame.hide()
        self.headFrame.hide()
        self.headLButton.hide()
        self.headRButton.hide()
        if self.headIndex == 0:
            self.speciesLButton['state'] = DGG.DISABLED
            self.speciesRButton['state'] = DGG.NORMAL
        elif self.headIndex == len(HeadList) - 1:
            self.speciesRButton['state'] = DGG.DISABLED
            self.speciesLButton['state'] = DGG.NORMAL
        else:
            self.speciesLButton['state'] = DGG.NORMAL
            self.speciesRButton['state'] = DGG.NORMAL
        if self.bodyIndex == 0:
            self.torsoLButton['state'] = DGG.DISABLED
            self.torsoRButton['state'] = DGG.NORMAL
        elif self.bodyIndex == len(BodyList) - 1:
            self.torsoRButton['state'] = DGG.DISABLED
            self.torsoLButton['state'] = DGG.NORMAL
        else:
            self.torsoLButton['state'] = DGG.NORMAL
            self.torsoRButton['state'] = DGG.NORMAL
        if self.legsIndex == 0:
            self.legLButton['state'] = DGG.DISABLED
            self.legRButton['state'] = DGG.NORMAL
        elif self.legsIndex == len(LegsList) - 1:
            self.legRButton['state'] = DGG.DISABLED
            self.legLButton['state'] = DGG.NORMAL
        else:
            self.legLButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.upsellModel.removeNode()
        del self.upsellModel
        self.parentFrame.destroy()
        self.speciesFrame.destroy()
        self.headFrame.destroy()
        self.bodyFrame.destroy()
        self.legsFrame.destroy()
        self.speciesLButton.destroy()
        self.speciesRButton.destroy()
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.torsoLButton.destroy()
        self.torsoRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        del self.parentFrame
        del self.speciesFrame
        del self.headFrame
        del self.bodyFrame
        del self.legsFrame
        del self.speciesLButton
        del self.speciesRButton
        del self.headLButton
        del self.headRButton
        del self.torsoLButton
        del self.torsoRButton
        del self.legLButton
        del self.legRButton

    def enter(self):
        self.showButtons()

    def exit(self):
        self.hideButtons()
        return self.toon

    def changeLegsLeft(self):
        self.toon.stop()
        self.toon.unloadAnims(LegsAnims[LegsList[self.legsIndex]], 'legs')
        self.legsIndex -= 1
        newLegsChoice = LegsList[self.legsIndex]
        self.toon.removePart('legs')
        if 'legs' in self.toon._Actor__commonBundleHandles:
            del self.toon._Actor__commonBundleHandles['legs']
        newLegs = loader.loadModel('phase_3/models/char/tt_a_chr_' + newLegsChoice + '_shorts_legs_1000')
        otherParts = newLegs.findAllMatches('**/boots*') + newLegs.findAllMatches('**/shoes')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        self.toon.loadModel(newLegs, 'legs')
        self.toon.loadAnims(LegsAnims[newLegsChoice], 'legs')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.attach('torso', 'legs', 'joint_hips')
        self.toon.loop('neutral')
        self.toon.setRandomLegsColor()
        self.toon.rescaleToon()
        del self.toon.shadowJoint
        self.toon.initializeDropShadow()
        self.toon.legsType = newLegsChoice
        if self.legsIndex == 0:
            self.legLButton['state'] = DGG.DISABLED
        else:
            self.legLButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL

    def changeLegsRight(self):
        self.toon.stop()
        self.toon.unloadAnims(LegsAnims[LegsList[self.legsIndex]], 'legs')
        self.legsIndex += 1
        newLegsChoice = LegsList[self.legsIndex]
        self.toon.removePart('legs')
        if 'legs' in self.toon._Actor__commonBundleHandles:
            del self.toon._Actor__commonBundleHandles['legs']
        newLegs = loader.loadModel('phase_3/models/char/tt_a_chr_' + newLegsChoice + '_shorts_legs_1000')
        otherParts = newLegs.findAllMatches('**/boots*') + newLegs.findAllMatches('**/shoes')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        self.toon.loadModel(newLegs, 'legs')
        self.toon.loadAnims(LegsAnims[newLegsChoice], 'legs')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.attach('torso', 'legs', 'joint_hips')
        self.toon.loop('neutral')
        self.toon.setRandomLegsColor()
        self.toon.rescaleToon()
        del self.toon.shadowJoint
        self.toon.initializeDropShadow()
        self.toon.legsType = newLegsChoice
        if self.legsIndex == len(LegsList) - 1:
            self.legRButton['state'] = DGG.DISABLED
        else:
            self.legLButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL

    def changeBodyLeft(self):
        self.bodyIndex -= 1
        newBodyChoice = BodyList[self.bodyIndex]
        self.toon.removePart('torso')
        if 'torso' in self.toon._Actor__commonBundleHandles:
            del self.toon._Actor__commonBundleHandles['torso']
        newBody = loader.loadModel('phase_3/models/char/tt_a_chr_' + newBodyChoice + '_shorts_torso_1000')
        self.toon.loadModel(newBody, 'torso')
        self.toon.loadAnims(BodyAnims[newBodyChoice], 'torso')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.attach('torso', 'legs', 'joint_hips')
        self.toon.loop('neutral', 0)
        self.toon.setRandomTorsoColor()
        self.toon.generateRandomClothing()
        self.toon.rescaleToon()
        self.toon.bodyType = newBodyChoice
        if self.bodyIndex == 0:
            self.torsoLButton['state'] = DGG.DISABLED
        else:
            self.torsoLButton['state'] = DGG.NORMAL
            self.torsoRButton['state'] = DGG.NORMAL

    def changeBodyRight(self):
        self.bodyIndex += 1
        newBodyChoice = BodyList[self.bodyIndex]
        self.toon.removePart('torso')
        if 'torso' in self.toon._Actor__commonBundleHandles:
            del self.toon._Actor__commonBundleHandles['torso']
        newBody = loader.loadModel('phase_3/models/char/tt_a_chr_' + newBodyChoice + '_shorts_torso_1000')
        self.toon.loadModel(newBody, 'torso')
        self.toon.loadAnims(BodyAnims[newBodyChoice], 'torso')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.attach('torso', 'legs', 'joint_hips')
        self.toon.loop('neutral', 0)
        self.toon.setRandomTorsoColor()
        self.toon.generateRandomClothing()
        self.toon.rescaleToon()
        self.toon.bodyType = newBodyChoice
        if self.bodyIndex == len(BodyList) - 1:
            self.torsoRButton['state'] = DGG.DISABLED
        else:
            self.torsoLButton['state'] = DGG.NORMAL
            self.torsoRButton['state'] = DGG.NORMAL

    def changeSpeciesLeft(self):
        self.headIndex -= 1
        newHeadChoice = HeadList[self.headIndex]
        head = self.toon.getPart('head')
        head.removeNode()
        if newHeadChoice == 'dog':
            headType = random.choice(["dss", "dsl", "dls", "dll"])
        else:
            headType = newHeadChoice
        species = newHeadChoice
        newHead = self.toon.handleHead(headType, species)
        self.toon.loadModel(newHead, 'head')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.rescaleToon()
        if self.headIndex == len(HeadList) - 1:
            self.speciesRButton['state'] = DGG.DISABLED
        else:
            self.speciesLButton['state'] = DGG.NORMAL
            self.speciesRButton['state'] = DGG.NORMAL

    def changeSpeciesRight(self):
        self.headIndex += 1
        newHeadChoice = HeadList[self.headIndex]
        head = self.toon.getPart('head')
        head.removeNode()
        if newHeadChoice == 'dog':
            headType = random.choice(["dss", "dsl", "dls", "dll"])
        else:
            headType = newHeadChoice
        species = newHeadChoice
        newHead = self.toon.handleHead(headType, species)
        self.toon.loadModel(newHead, 'head')
        self.toon.attach('head', 'torso', 'def_head')
        self.toon.rescaleToon()
        if self.headIndex == len(HeadList) - 1:
            self.speciesRButton['state'] = DGG.DISABLED
        else:
            self.speciesLButton['state'] = DGG.NORMAL
            self.speciesRButton['state'] = DGG.NORMAL

    def showButtons(self):
        self.parentFrame.show()

    def hideButtons(self):
        self.parentFrame.hide()
