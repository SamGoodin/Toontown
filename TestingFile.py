from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task.Task import Task
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

w = Window()
w.run()