from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toon.Toon import Toon
import random


class ColorShop:

    def __init__(self, makeAToon, toonType):
        self.makeAToon = makeAToon
        self.toon = None
        self.toonClass = Toon()
        self.animalType = toonType

    def enter(self, toon):
        base.disableMouse()
        self.toon = toon
        self.colorList = self.toonClass.getColorList()
        self.length = len(self.colorList)
        self.entireColorChoice = random.randint(0, self.length-1)
        self.headChoice = random.randint(0, self.length-1)
        self.bodyChoice = random.randint(0, self.length-1)
        self.legsChoice = random.randint(0, self.length-1)
        self.swapAllColor(0)

    def swapAllColor(self, offset):
        self.entireColorChoice += offset
        self.changeAllColor(self.entireColorChoice)
        if self.entireColorChoice == 0:
            self.allLButton['state'] = DGG.DISABLED
            self.headLButton['state'] = DGG.DISABLED
            self.armLButton['state'] = DGG.DISABLED
            self.legLButton['state'] = DGG.DISABLED
            self.allRButton['state'] = DGG.NORMAL
            self.headRButton['state'] = DGG.NORMAL
            self.armRButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL
        elif self.entireColorChoice == self.length - 1:
            self.allLButton['state'] = DGG.NORMAL
            self.headLButton['state'] = DGG.NORMAL
            self.armLButton['state'] = DGG.NORMAL
            self.legLButton['state'] = DGG.NORMAL
            self.allRButton['state'] = DGG.DISABLED
            self.headRButton['state'] = DGG.DISABLED
            self.armRButton['state'] = DGG.DISABLED
            self.legRButton['state'] = DGG.DISABLED
        else:
            self.allLButton['state'] = DGG.NORMAL
            self.headLButton['state'] = DGG.NORMAL
            self.armLButton['state'] = DGG.NORMAL
            self.legLButton['state'] = DGG.NORMAL
            self.allRButton['state'] = DGG.NORMAL
            self.headRButton['state'] = DGG.NORMAL
            self.armRButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL

    def changeAllColor(self, offset):
        self.headChoice = self.entireColorChoice
        self.legsChoice = self.entireColorChoice
        self.bodyChoice = self.entireColorChoice
        self.swapHeadColor(0)
        self.swapBodyColor(0)
        self.swapLegColor(0)

    def swapHeadColor(self, offset, firstTime=False):
        self.headChoice += offset
        self.changeHeadColor(self.headChoice, firstTime)
        if self.headChoice == 0:
            self.headLButton['state'] = DGG.DISABLED
            self.headRButton['state'] = DGG.NORMAL
        elif self.headChoice == self.length - 1:
            self.headLButton['state'] = DGG.NORMAL
            self.headRButton['state'] = DGG.DISABLED
        else:
            self.headLButton['state'] = DGG.NORMAL
            self.headRButton['state'] = DGG.NORMAL

    def changeHeadColor(self, offset, firstTime):
        newColor = self.colorList[self.headChoice]
        self.toon = self.toonClass.setHeadColor(self.toon, self.animalType, newColor)

    def swapBodyColor(self, offset, firstTime=False):
        self.changeBodyColor(offset, firstTime)
        if self.bodyChoice == 0:
            self.armLButton['state'] = DGG.DISABLED
            self.armRButton['state'] = DGG.NORMAL
        elif self.bodyChoice == self.length - 1:
            self.armLButton['state'] = DGG.NORMAL
            self.armRButton['state'] = DGG.DISABLED
        else:
            self.armLButton['state'] = DGG.NORMAL
            self.armRButton['state'] = DGG.NORMAL

    def changeBodyColor(self, offset, firstTime):
        if not firstTime:
            self.bodyChoice += offset
        newColor = self.colorList[self.bodyChoice]
        self.toon = self.toonClass.setTorsoColor(self.toon, newColor)

    def swapLegColor(self, offset, firstTime=False):
        self.changeLegColor(offset, firstTime)
        if self.legsChoice == 0:
            self.legLButton['state'] = DGG.DISABLED
            self.legRButton['state'] = DGG.NORMAL
        elif self.legsChoice == self.length - 1:
            self.legLButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.DISABLED
        else:
            self.legLButton['state'] = DGG.NORMAL
            self.legRButton['state'] = DGG.NORMAL

    def changeLegColor(self, offset, firstTime):
        if not firstTime:
            self.legsChoice += offset
        newColor = self.colorList[self.legsChoice]
        self.toon = self.toonClass.setLegsColor(self.toon, newColor)

    def load(self):
        self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
        guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
        shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
        shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
        self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
        self.parentFrame.setPos(-0.36, 0, -0.5)
        self.parentFrame.reparentTo(base.a2dTopRight)
        self.toonFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6),
                                     relief=None, pos=(0, 0, -0.073), hpr=(0, 0, 0), scale=1.3, frameColor=(1, 1, 1, 1),
                                     text="Toon Color", text_scale=0.0575,
                                     text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.allLButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                       image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapAllColor,
                                       extraArgs=[-1])
        self.allRButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                       image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapAllColor,
                                       extraArgs=[1])
        self.headFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6),
                                     relief=None, pos=(0, 0, -0.3), hpr=(0, 0, 2), scale=0.9, frameColor=(1, 1, 1, 1),
                                     text="Head", text_scale=0.0625, text_pos=(-0.001, -0.015),
                                     text_fg=(1, 1, 1, 1))
        self.headLButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
                                                                                   shuffleArrowDown,
                                                                                   shuffleArrowRollover,
                                                                                   shuffleArrowDisabled),
                                        image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                        image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapHeadColor,
                                        extraArgs=[-1])
        self.headRButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
                                                                                   shuffleArrowDown,
                                                                                   shuffleArrowRollover,
                                                                                   shuffleArrowDisabled),
                                        image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                        image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapHeadColor,
                                        extraArgs=[1])
        self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(0.6, 0.6, 0.6),
                                     relief=None, pos=(0, 0, -0.5), hpr=(0, 0, -2), scale=0.9, frameColor=(1, 1, 1, 1),
                                     text="Body", text_scale=0.0625, text_pos=(-0.001, -0.015),
                                     text_fg=(1, 1, 1, 1))
        self.armLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                       image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapBodyColor,
                                       extraArgs=[-1])
        self.armRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                       image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapBodyColor,
                                       extraArgs=[1])
        self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6),
                                     relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=0.9, frameColor=(1, 1, 1, 1),
                                     text="Legs", text_scale=0.0625, text_pos=(-0.001, -0.015),
                                     text_fg=(1, 1, 1, 1))
        self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                       image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapLegColor,
                                       extraArgs=[-1])
        self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
                                                                                  shuffleArrowDown,
                                                                                  shuffleArrowRollover,
                                                                                  shuffleArrowDisabled),
                                       image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                       image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapLegColor,
                                       extraArgs=[1])

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.parentFrame.destroy()
        self.toonFrame.destroy()
        self.headFrame.destroy()
        self.bodyFrame.destroy()
        self.legsFrame.destroy()
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.armLButton.destroy()
        self.armRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        self.allLButton.destroy()
        self.allRButton.destroy()
        del self.parentFrame
        del self.toonFrame
        del self.headFrame
        del self.bodyFrame
        del self.legsFrame
        del self.headLButton
        del self.headRButton
        del self.armLButton
        del self.armRButton
        del self.legLButton
        del self.legRButton
        del self.allLButton
        del self.allRButton

    def exit(self):
        self.parentFrame.hide()
        return self.toon