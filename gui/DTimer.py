from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
import time

class DTimer:
    notify = DirectNotifyGlobal.directNotify.newCategory('DTimer')

    def __init__(self):
        self.generate()
        self.setStartTime(globalClockDelta.getRealNetworkTime(bits=32))

    def generate(self):
        base.DTimer = self

    def delete(self):
        base.DTimer = None
        return

    def setStartTime(self, time):
        self.startTime = time

    def getStartTime(self):
        return self.startTime

    def getTime(self):
        elapsedTime = globalClockDelta.localElapsedTime(self.startTime, bits=32)
        return elapsedTime