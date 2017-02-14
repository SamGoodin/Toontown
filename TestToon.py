from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *

class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.button = Button()

class Button(DirectButton):

    def __init__(self):
        DirectButton.__init__(self)
        self.initialiseoptions(Button)
        self['image'] = Actor('Resources/phase_3/models/char/mouse-heads-1000.bam')
        self.reparentTo(aspect2d)
        self.setScale(.2)
        self['pressEffect'] = 1


        '''DirectButton(image=None, relief=None, text_font=Globals.getSignFont(), text="Make A\nToon",
                              text0_scale=0.1, text1_scale=0.12, text2_scale=0.12, text_pos=(0, 0), scale=1.01,
                              pressEffect=1, rolloverSound=Globals.getRolloverSound(),
                              clickSound=Globals.getClickSound(), pos=(POSITIONS[num]),
                              text0_fg=(0, 1, 0.8, 0.5), text1_fg=(0, 1, 0.8, 1), text2_fg=(0.3, 1, 0.9, 1),
                              extraArgs=ButtonNames[num])'''


game = Window()
game.run()