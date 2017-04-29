from direct.showbase.ShowBase import ShowBase
import Globals
from pandac.PandaModules import *
loadPrcFile('config/Config.prc')
from direct.task.Task import Task


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        cbm = CullBinManager.getGlobalPtr()
        cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
        cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)

        self.vfs = VirtualFileSystem.getGlobalPtr()
        for mount in Globals.mounts:
            self.vfs.mount("multifiles/" + mount, "/", 0)

        self.sky = self.loader.loadModel("phase_3.5/models/props/TT_sky.bam")
        self.sky.setTag('sky', 'Regular')
        self.sky.setFogOff()
        self.sky.setScale(1.0)
        self.ttc = self.loader.loadModel('phase_15/hood/toontown_central.bam')
        self.ttc.reparentTo(self.render)
        self.sky.reparentTo(camera)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        self.sky.reparentTo(camera)
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)
        skyTrackTask = Task(self.skyTrack)
        skyTrackTask.h = 0
        skyTrackTask.cloud1 = self.sky.find('**/cloud1')
        skyTrackTask.cloud2 = self.sky.find('**/cloud2')
        if not skyTrackTask.cloud1.isEmpty() and not skyTrackTask.cloud2.isEmpty():
            taskMgr.add(skyTrackTask, 'skyTrack')
        else:
            notify.warning("Couln't find clouds!")
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)

    def skyTrack(self, task):
        return self.cloudSkyTrack(task)

    def cloudSkyTrack(self, task):
        task.h += globalClock.getDt() * 0.25
        if task.cloud1.isEmpty() or task.cloud2.isEmpty():
            notify.warning("Couln't find clouds!")
            return Task.done
        task.cloud1.setH(task.h)
        task.cloud2.setH(-task.h * 0.8)
        return Task.cont

w = Window()
w.run()