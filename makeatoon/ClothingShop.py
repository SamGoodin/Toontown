from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toon.Toon import Toon
import random


class ClothingShop:

    def __init__(self, toon):
        self.toonClass = Toon()
        self.shirts = self.toonClass.getShirtsList()
        self.shorts = self.toonClass.getShortsList()
        self.shirtsLength = len(self.shirts)
        self.shortsLength = len(self.shorts)
        self.shirtChoice = random.randint(0, self.shirtsLength-1)
        self.shortsChoice = random.randint(0, self.shortsLength-1)
        self.toon = toon

    def enter(self):
        self.swapShirt(0)
        self.swapShorts(0)

    def swapShirt(self, offset):
        self.shirtChoice += offset
        self.toon.setShirt(self.shirtChoice)
        if self.shirtChoice == 0:
            self.topLButton['state'] = DGG.DISABLED
            self.topRButton['state'] = DGG.NORMAL
        elif self.shirtChoice == self.shirtsLength - 1:
            self.topLButton['state'] = DGG.NORMAL
            self.topRButton['state'] = DGG.DISABLED
        else:
            self.topLButton['state'] = DGG.NORMAL
            self.topRButton['state'] = DGG.NORMAL

    def swapShorts(self, offset):
        self.shortsChoice += offset
        self.toon.setShorts(self.shortsChoice)
        if self.shortsChoice == 0:
            self.bottomLButton['state'] = DGG.DISABLED
            self.bottomRButton['state'] = DGG.NORMAL
        elif self.shortsChoice == self.shortsLength - 1:
            self.bottomLButton['state'] = DGG.NORMAL
            self.bottomRButton['state'] = DGG.DISABLED
        else:
            self.bottomLButton['state'] = DGG.NORMAL
            self.bottomRButton['state'] = DGG.NORMAL


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
        self.shirtFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6),
                                      relief=None, pos=(0, 0, -0.4), hpr=(0, 0, 3), scale=1.2, frameColor=(1, 1, 1, 1),
                                      text="Shirts", text_scale=0.0575, text_pos=(-0.001, -0.015),
                                      text_fg=(1, 1, 1, 1))
        self.topLButton = DirectButton(parent=self.shirtFrame, relief=None, image=(shuffleArrowUp,
                                                                                   shuffleArrowDown,
                                                                                   shuffleArrowRollover,
                                                                                   shuffleArrowDisabled),
                                       image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                       image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapShirt,
                                       extraArgs=[-1])
        self.topRButton = DirectButton(parent=self.shirtFrame, relief=None, image=(shuffleArrowUp,
                                                                                   shuffleArrowDown,
                                                                                   shuffleArrowRollover,
                                                                                   shuffleArrowDisabled),
                                       image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                       image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapShirt,
                                       extraArgs=[1])
        self.bottomFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=(-0.6, 0.6, 0.6),
                                       relief=None, pos=(0, 0, -0.65), hpr=(0, 0, -2), scale=1.2,
                                       frameColor=(1, 1, 1, 1), text="Shorts", text_scale=0.0575,
                                       text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.bottomLButton = DirectButton(parent=self.bottomFrame, relief=None, image=(shuffleArrowUp,
                                                                                       shuffleArrowDown,
                                                                                       shuffleArrowRollover,
                                                                                       shuffleArrowDisabled),
                                          image_scale=(0.6, 0.6, 0.6), image1_scale=(0.7, 0.7, 0.7),
                                          image2_scale=(0.7, 0.7, 0.7), pos=(-0.2, 0, 0), command=self.swapShorts,
                                          extraArgs=[-1])
        self.bottomRButton = DirectButton(parent=self.bottomFrame, relief=None, image=(shuffleArrowUp,
                                                                                       shuffleArrowDown,
                                                                                       shuffleArrowRollover,
                                                                                       shuffleArrowDisabled),
                                          image_scale=(-0.6, 0.6, 0.6), image1_scale=(-0.7, 0.7, 0.7),
                                          image2_scale=(-0.7, 0.7, 0.7), pos=(0.2, 0, 0), command=self.swapShorts,
                                          extraArgs=[1])

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.parentFrame.destroy()
        self.shirtFrame.destroy()
        self.bottomFrame.destroy()
        self.topLButton.destroy()
        self.topRButton.destroy()
        self.bottomLButton.destroy()
        self.bottomRButton.destroy()
        del self.parentFrame
        del self.shirtFrame
        del self.bottomFrame
        del self.topLButton
        del self.topRButton
        del self.bottomLButton
        del self.bottomRButton

    def exit(self):
        self.parentFrame.hide()