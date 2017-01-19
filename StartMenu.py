from pandac.PandaModules import *
from direct.gui.DirectGui import *
import Globals
import os.path
import json

POSITIONS = (Vec3(-0.860167, 0, 0.359333),
 Vec3(0, 0, 0.346533),
 Vec3(0.848, 0, 0.3293),
 Vec3(-0.863554, 0, -0.445659),
 Vec3(0.00799999, 0, -0.5481),
 Vec3(0.894907, 0, -0.445659))


class StartMenu:

    def __init__(self):
        pass

    def enter(self):
        base.disableMouse()
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        self.logoutButton.show()
        self.pickAToonBG.setBin('background', 1)
        self.pickAToonBG.reparentTo(aspect2d)
        base.setBackgroundColor(Vec4(0.145, 0.368, 0.78, 1))

    def enterMakeAToon(self):
        messenger.send('enterMAT')
        self.exit()

    def quit(self):
        self.exit()
        messenger.send('exit')

    def exit(self):
        self.title.reparentTo(hidden)
        self.quitButton.hide()
        self.logoutButton.hide()
        self.pickAToonBG.reparentTo(hidden)
        base.setBackgroundColor(0.3, 0.3, 0.3, 1)
        self.unloadStartMenu()

    def loadStartMenu(self):
        if os.path.isfile("data/ToonData.json"):
            #File exists
            pass
        else:
            #File Doesn't
            pass
        self.ac = AvatarChoice()
        gui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
        gui.flattenMedium()
        gui2 = loader.loadModel('phase_3/models/gui/quit_button')
        gui2.flattenMedium()
        newGui = loader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui')
        newGui.flattenMedium()
        self.pickAToonBG = newGui.find('**/tt_t_gui_pat_background')
        self.pickAToonBG.flattenStrong()
        self.pickAToonBG.setPos(0.0, 2.73, 0.0)
        self.pickAToonBG.setScale(1.5, 1, 2)
        self.title = OnscreenText("Pick A Toon To Play", scale=0.15, parent=hidden,
                                  font=Globals.getSignFont(), fg=(1, 0.9, 0.1, 1), pos=(0.0, 0.82))
        self.title.flattenStrong()
        quitHover = gui.find('**/QuitBtn_RLVR')
        self.quitButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None,
                                       text="Quit", text_font=Globals.getSignFont(),
                                       text_fg=(0.977, 0.816, 0.133, 1), text_pos=(0, -0.035),
                                       text_scale=0.1, image_scale=1, image1_scale=1.05,
                                       image2_scale=1.05, scale=1.05, pos=(-0.25, 0, 0.075), command=self.quit)
        self.quitButton.flattenMedium()
        self.quitButton.reparentTo(base.a2dBottomRight)
        self.logoutButton = DirectButton(relief=None, image=(quitHover, quitHover, quitHover),
                                         text="Logout", text_font=Globals.getSignFont(),
                                         text_fg=(0.977, 0.816, 0.133, 1), text_scale=0.1,
                                         text_pos=(0, -0.035), pos=(0.15, 0, 0.05), image_scale=1.15, image1_scale=1.15,
                                         image2_scale=1.18, scale=0.5, command=self.quit)
        self.logoutButton.reparentTo(base.a2dBottomLeft)
        self.logoutButton.flattenMedium()
        self.logoutButton.hide()
        self.ac.createButtons()
        for button in self.ac.buttonList:
            button['command'] = self.enterMakeAToon
        gui.removeNode()
        gui2.removeNode()
        newGui.removeNode()
        self.enter()

    def unloadStartMenu(self):
        for button in self.ac.buttonList:
            button.destroy()
            del button
        self.title.removeNode()
        del self.title
        self.quitButton.destroy()
        del self.quitButton
        self.logoutButton.destroy()
        del self.logoutButton
        self.pickAToonBG.removeNode()
        del self.pickAToonBG


class AvatarChoice:

    def __init__(self):
        self.buttonList = []
        self.button = None

    def createButtons(self):
        num = 0
        while num < 6:
            self.button = DirectButton(image=None, relief=None, text_font=Globals.getSignFont(), text="Make A\nToon",
                                       text0_scale=0.1, text1_scale=0.12, text2_scale=0.12, text_pos=(0, 0), scale=1.01,
                                       pressEffect=1, rolloverSound=Globals.getRolloverSound(),
                                       clickSound=Globals.getClickSound(), pos=(POSITIONS[num]),
                                       text0_fg=(0, 1, 0.8, 0.5), text1_fg=(0, 1, 0.8, 1), text2_fg=(0.3, 1, 0.9, 1))
            self.buttonList.append(self.button)
            num += 1

    def destroy(self):
        for button in self.buttonList:
            button.destroy()
        del self.buttonList
