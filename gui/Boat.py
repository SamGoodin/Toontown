from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
import Globals
from direct.directutil import Mopath


class Boat:

    def __init__(self, boat, playground):
        self.boat = boat
        self.playground = playground
        self.boatFsm = ClassicFSM.ClassicFSM(
            'Boat',
            [
                State.State('off', self.enterOff, self.exitOff,
                            ['DockedEast']),
                State.State('DockedEast', self.enterDockedEast, self.exitDockedEast,
                            ['SailingWest']),
                State.State('SailingWest', self.enterSailingWest, self.exitSailingWest,
                            ['DockedWest']),
                State.State('DockedWest', self.enterDockedWest, self.exitDockedWest,
                            ['SailingEast']),
                State.State('SailingEast', self.enterSailingEast, self.exitSailingEast,
                            ['DockedEast'])
            ], 'off', 'off')
        self.boatFsm.enterInitialState()
        self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')

    def generateBoat(self):
        self.eastWestMopath = Mopath.Mopath()
        self.westEastMopath = Mopath.Mopath()
        self.eastWestMopathInterval = None
        self.westEastMopathInterval = None
        self.setupTracks()
        #self.accept('enterdonalds_boat_floor', self.enterOnBoat)
        #self.accept('exitdonalds_boat_floor', self.exitOnBoat)

    def setupTracks(self):
        boat = self.boat
        boat.unstash()
        self.eastWestMopath.loadFile('phase_6/paths/dd-e-w')
        self.eastWestMopathInterval = MopathInterval(self.eastWestMopath, boat)
        ewBoatTrack = ParallelEndTogether(Parallel(self.eastWestMopathInterval, SoundInterval(self.bellSound,
                                                                                              node=boat)),
                                          SoundInterval(self.foghornSound, node=boat), name='ew-boat')
        self.westEastMopath.loadFile('phase_6/paths/dd-w-e')
        self.westEastMopathInterval = MopathInterval(self.westEastMopath, boat)
        weBoatTrack = ParallelEndTogether(Parallel(self.westEastMopathInterval, SoundInterval(self.bellSound,
                                                                                              node=boat)),
                                          SoundInterval(self.foghornSound, node=boat), name='we-boat')
        PIER_TIME = 5.0
        eastPier = self.playground.find('**/east_pier')
        ePierHpr = VBase3(90, -44.2601, 0)
        ePierTargetHpr = VBase3(90, 0.25, 0)
        westPier = self.playground.find('**/west_pier')
        wPierHpr = VBase3(-90, -44.2601, 0)
        wPierTargetHpr = VBase3(-90, 0.25, 0)
        ePierDownTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierHpr, ePierTargetHpr),
                                  SoundInterval(self.dockSound, node=eastPier), name='e-pier-down')
        ePierUpTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierTargetHpr, ePierHpr),
                                SoundInterval(self.dockSound, node=eastPier), name='e-pier-up')
        wPierDownTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierHpr, wPierTargetHpr),
                                  SoundInterval(self.dockSound, node=westPier), name='w-pier-down')
        wPierUpTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierTargetHpr, wPierHpr),
                                SoundInterval(self.dockSound, node=westPier), name='w-pier-up')
        self.ewTrack = ParallelEndTogether(Parallel(ewBoatTrack, ePierDownTrack), wPierUpTrack, name='ew-track')
        self.weTrack = ParallelEndTogether(Parallel(weBoatTrack, wPierDownTrack), ePierUpTrack, name='we-track')
        self.start()

    def enterOnBoat(self):
        base.localAvatar.b_setParent(Globals.SPDonaldsBoat)
        base.playSfx(self.waterSound, looping=1)

    def exitOnBoat(self):
        base.localAvatar.b_setParent(Globals.SPRender)
        self.waterSound.stop()

    def enterDockedEast(self):
        taskMgr.doMethodLater(10.0, self.__departEast, 'depart-east')
        self.weTrack.finish()
        return None

    def exitDockedEast(self):
        taskMgr.remove('depart-east')
        return None

    def enterSailingWest(self, ts):
        taskMgr.doMethodLater(20.0, self.__dockWest, 'dock-west')
        self.ewTrack.start(ts)

    def exitSailingWest(self):
        taskMgr.remove('dock-west')
        self.ewTrack.finish()

    def enterDockedWest(self):
        taskMgr.doMethodLater(10.0, self.__departWest, 'depart-west')
        self.ewTrack.finish()
        return None

    def exitDockedWest(self):
        taskMgr.remove('depart-west')
        return None

    def enterSailingEast(self, ts):
        taskMgr.doMethodLater(20.0, self.__dockEast, 'dock-east')
        self.weTrack.start(ts)

    def exitSailingEast(self):
        #TODO: Boat
        taskMgr.remove('dock-east')
        self.weTrack.finish()
        return None

    def start(self):
        print self.boatFsm.request('DockedEast')

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def __departEast(self, task):
        self.boatFsm.request('SailingWest')
        return Task.done

    def __dockWest(self, task):
        self.boatFsm.request('DockedWest')
        return Task.done

    def __departWest(self, task):
        self.boatFsm.request('SailingEast')
        return Task.done

    def __dockEast(self, task):
        self.boatFsm.request('DockedEast')
        return Task.done