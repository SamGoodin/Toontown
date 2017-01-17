from direct.gui.DirectGui import *
from pandac.PandaModules import *
import Globals


class MessageBox(DirectFrame):

    def __init__(self, string):
        DirectFrame.__init__(self, relief=None, geom=loader.loadModel('phase_3/models/gui/dialog_box_gui'), geom_color=Globals.GlobalDialogColor,
                            geom_scale=1)
        self.label = DirectLabel(parent=self, relief=None, pos=(0, 0, 0), text=string, text_scale=0.1)
        return
