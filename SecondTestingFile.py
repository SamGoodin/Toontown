from pandac.PandaModules import *
loadPrcFile(
    'config/Config.prc'
)
from direct.showbase.ShowBase import ShowBase
import Globals


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        #Keep VFS here to use files
        self.vfs = VirtualFileSystem.getGlobalPtr()
        for mount in Globals.mounts:
            self.vfs.mount("multifiles/" + mount, "resources", 0)

        from direct.showbase.Transitions import Transitions

        transition = Transitions(self.loader)
        transition.IrisModelName = 'phase_3/models/misc/iris'
        transition.FadeModelName = 'phase_3/models/misc/fade'

        base.accept("1", transition.irisIn)
        base.accept("2", transition.irisOut)

T = Window()
T.run()