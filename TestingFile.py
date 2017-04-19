from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.showbase.Transitions import Transitions


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.transitions = Transitions(self.loader)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.doneEvent = None

    def fade(self):
        base.transitions.fadeOut(finishIval=EventInterval(self.doneEvent, [self.doneStatus]))

w = Window()
w.run()