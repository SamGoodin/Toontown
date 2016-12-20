from pandac.PandaModules import *
from direct.gui.DirectGui import *
import Globals
from Toon import Toon

class GenderShop:

    def __init__(self, makeAToon):
        self.toon = Toon()
        self.makeAToon = makeAToon

    def showButtons(self):
        self.boyButton.show()

    def hideButtons(self):
        self.boyButton.hide()
        self.girlButton.hide()

    def load(self):
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiBoyUp = gui.find('**/tt_t_gui_mat_boyUp')
        guiBoyDown = gui.find('**/tt_t_gui_mat_boyDown')
        guiGirlUp = gui.find('**/tt_t_gui_mat_girlUp')
        guiGirlDown = gui.find('**/tt_t_gui_mat_girlDown')
        self.boyButton = DirectButton(relief=None, image=(guiBoyUp,
                                                          guiBoyDown,
                                                          guiBoyUp,
                                                          guiBoyDown), image_scale=(0.6, 0.6, 0.6),
                                      image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7),
                                      pos=(-0.4, 0, -0.8), command=self.createRandomBoy, text=('',
                                                                 'Boy',
                                                                 'Boy',
                                                                 ''),
                                      text_font=Globals.getInterfaceFont(), text_scale=0.08, text_pos=(0, 0.19),
                                      text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
        self.boyButton.hide()
        self.boyButton.setPos(-0.45, 0, 0.19)
        self.boyButton.reparentTo(base.a2dBottomCenter)
        self.girlButton = DirectButton(relief=None, image=(guiGirlUp,
                                                           guiGirlDown,
                                                           guiGirlUp,
                                                           guiGirlDown), image_scale=(0.6, 0.6, 0.6),
                                       image1_scale=(0.7, 0.7, 0.7), image2_scale=(0.7, 0.7, 0.7),
                                       pos=(0.4, 0, -0.8), text=('',
                                                                'Girl',
                                                                'Girl',
                                                                ''),
                                       text_font=Globals.getInterfaceFont(), text_scale=0.08,
                                       text_pos=(0, 0.19), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
        self.girlButton.hide()
        self.girlButton.setPos(0.45, 0, 0.19)
        self.girlButton.reparentTo(base.a2dBottomCenter)
        gui.removeNode()
        del gui

    def createRandomBoy(self):
        if self.toon:
            self.toon.delete()
        self.toon.createRandomBoy()
        self.toon.reparentTo(render)
        self.toon.loop("neutral")
        self.toon.setHpr(180, 0, 0)
        self.makeAToon.setNextButtonState(DGG.NORMAL)

    def enter(self):
        self.boyButton.show()

    def exit(self):
        self.boyButton.hide()

    def getToon(self):
        return self.toonClass.getToon()

    def getAnimalType(self):
        return self.toonClass.getAnimalType()

    def getBodyType(self):
        return self.toonClass.getBodyType()

    def getLegsType(self):
        return self.toonClass.getLegsType()

    def killToon(self):
        if self.toon:
            self.toon.delete()

    def unload(self):
        self.boyButton.destroy()
        self.girlButton.destroy()
        del self.boyButton
        del self.girlButton
        self.makeAToon = None

