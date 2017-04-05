from direct.task import Task
from pandac.PandaModules import *

notify = directNotify.newCategory('SkyUtil')


class Sky:

    def __init__(self):
        self.sky = None

    def setupSky(self, skyFile):
        self.sky = loader.loadModel(skyFile)
        self.sky.setTag('sky', 'Regular')
        self.sky.setScale(5.0)
        self.sky.setFogOff()
        self.sky.setDepthTest(True)
        self.sky.setDepthWrite(False)
        self.sky.reparentTo(render)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        self.sky.setZ(0.0)
        self.sky.setHpr(0, 0, 0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)
        skyTrackTask = Task.Task(self.cloudSkyTrack)
        skyTrackTask.h = 0
        skyTrackTask.cloud1 = self.sky.find('**/cloud1')
        skyTrackTask.cloud2 = self.sky.find('**/cloud2')
        if not skyTrackTask.cloud1.isEmpty() and not skyTrackTask.cloud2.isEmpty():
            taskMgr.add(skyTrackTask, 'skyTrack')
        else:
            notify.warning("Couldn't find clouds!")

    def cloudSkyTrack(self, task):
        task.h += globalClock.getDt() * 0.25
        if task.cloud1.isEmpty() or task.cloud2.isEmpty():
            notify.warning("Couldn't find clouds!")
            return Task.done

        task.cloud1.setH(task.h)
        task.cloud2.setH(-task.h * 0.8)
        return Task.cont

    def unload(self):
        self.sky.removeNode()
        del self.sky