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
        self.doneEvent = "Match"
        self.doneStatus = "Match1"
        self.accept('y', self.fade)
        self.accept(self.doneStatus, self.fund)

    def fade(self):
        self.transitions.fadeOut(finishIval=EventInterval(self.doneEvent, [self.doneStatus]))
        jim = Sequence(Wait(2), Func(self.match))
        jim.setAutoFinish(True)
        jim.start()

    def fund(self, *args):
        print args

    def match(self):
        self.doneStatus = "Match"
        print self.doneStatus

w = Window()
w.run()