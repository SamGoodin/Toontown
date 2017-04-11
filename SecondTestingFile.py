from panda3d.core import *
import os
from direct.showbase.ShowBase import ShowBase

class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.vfs = VirtualFileSystem.getGlobalPtr()
        for filename in os.listdir(os.getcwd()):
            self.vfs.mount(filename, ".", VirtualFileSystem.MFReadOnly)
        loadPrcFileData('', 'cursor-filename phase_3/etc/toonmono.cur')

T = Window()
T.run()