from direct.gui.DirectGui import *
from pandac.PandaModules import *
import Globals
from direct.showbase.Transitions import Transitions


class MessageBox(DirectFrame):

    def __init__(self, string):
        geom = loader.loadModel('phase_3/models/gui/dialog_box_gui')
        gscale = (Globals.RPdirectFrame[0]*.8, Globals.RPdirectFrame[1]*.8, Globals.RPdirectFrame[2] * 1.1)
        DirectFrame.__init__(self, relief=None, geom=geom, geom_color=Globals.GlobalDialogColor,
                             geom_pos=Point3(0, 0, 0), geom_scale=gscale, pos=(0, 0, 0))
        self.initialiseoptions(MessageBox)
        self.setScale(.8)
        self.label = DirectLabel(parent=self, relief=None, pos=(0, 0, .2), text=string, text_scale=0.1)
        self._battleGui = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.okayButton = DirectButton(parent=self, relief=None,
                                       image=(self._battleGui.find('**/ChtBx_OKBtn_UP'),
                                              self._battleGui.find('**/ChtBx_OKBtn_DN'),
                                              self._battleGui.find('**/ChtBx_OKBtn_Rllvr')),
                                       pos=(0.0, 0, -0.19), scale=(0.39, 1.0, 0.39), image_scale=(4, 4, 4),
                                       text=('', 'Okay', 'Okay', ''),
                                       text_scale=Globals.RPskipScale, text_fg=Vec4(1, 1, 1, 1),
                                       text_shadow=Vec4(0, 0, 0, 1), text_pos=Globals.RPskipPos, textMayChange=0,
                                       command=self.delete)
        loader.unloadModel(geom)
        loader.unloadModel(self._battleGui)
        taskMgr.doMethodLater(5, self.delete, 'Popup')
        return

    def delete(self):
        self.label.destroy()
        self.okayButton.destroy()
        DirectFrame.destroy(self)

