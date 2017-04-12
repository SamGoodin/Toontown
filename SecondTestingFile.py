from pandac.PandaModules import *
loadPrcFile(
    'config/Config.prc'
)
from direct.showbase.ShowBase import ShowBase


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

T = Window()
T.run()