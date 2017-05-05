from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from hood.folder import InteractiveAnimatedProp
from hood.folder import GenericAnimatedProp
import Globals

class HydrantInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantInteractiveProp')
    BattleCheerText = Globals.InteractivePropTrackBonusTerms[5]
    ZoneToIdles = {Globals.ToontownCentralId: (('tt_a_ara_ttc_hydrant_idle0',
                                        1,
                                        1,
                                        None,
                                        3,
                                        10),
                                       ('tt_a_ara_ttc_hydrant_idle2',
                                        1,
                                        1,
                                        None,
                                        3,
                                        10),
                                       ('tt_a_ara_ttc_hydrant_idle1',
                                        1,
                                        1,
                                        None,
                                        3,
                                        10),
                                       ('tt_a_ara_ttc_hydrant_idleAwesome3',
                                        1,
                                        1,
                                        None,
                                        3,
                                        10)),
     Globals.DonaldsDockId: (('tt_a_ara_ttc_hydrant_idle0',
                                    1,
                                    1,
                                    None,
                                    3,
                                    10),
                                   ('tt_a_ara_ttc_hydrant_idle2',
                                    1,
                                    1,
                                    None,
                                    3,
                                    10),
                                   ('tt_a_ara_ttc_hydrant_idle1',
                                    1,
                                    1,
                                    None,
                                    3,
                                    10),
                                   ('tt_a_ara_ttc_hydrant_idleAwesome3',
                                    1,
                                    1,
                                    None,
                                    3,
                                    10)),
     Globals.DaisyGardensId: (('tt_a_ara_dga_hydrant_idle0',
                                     3,
                                     10,
                                     'tt_a_ara_dga_hydrant_idle0settle',
                                     3,
                                     10),
                                    ('tt_a_ara_dga_hydrant_idleLook1',
                                     1,
                                     1,
                                     None,
                                     3,
                                     10),
                                    ('tt_a_ara_dga_hydrant_idleSneeze2',
                                     1,
                                     1,
                                     None,
                                     3,
                                     10),
                                    ('tt_a_ara_dga_hydrant_idleAwesome3',
                                     1,
                                     1,
                                     None,
                                     3,
                                     10)),
     Globals.MinniesMelodylandId: (('tt_a_ara_mml_hydrant_idle0',
                                          3,
                                          10,
                                          'tt_a_ara_mml_hydrant_idle0settle',
                                          3,
                                          10),
                                         ('tt_a_ara_mml_hydrant_idle2',
                                          3,
                                          10,
                                          'tt_a_ara_mml_hydrant_idle2settle',
                                          3,
                                          10),
                                         ('tt_a_ara_mml_hydrant_idle1',
                                          3,
                                          10,
                                          'tt_a_ara_mml_hydrant_idle1settle',
                                          3,
                                          10),
                                         ('tt_a_ara_mml_hydrant_idleAwesome3',
                                          1,
                                          1,
                                          None,
                                          3,
                                          10)),
     Globals.TheBrrrghId: (('tt_a_ara_tbr_hydrant_idleShiver1',
                                  1,
                                  1,
                                  None,
                                  3,
                                  10),
                                 ('tt_a_ara_tbr_hydrant_idleRubNose0',
                                  1,
                                  1,
                                  None,
                                  3,
                                  10),
                                 ('tt_a_ara_tbr_hydrant_idleSneeze2',
                                  1,
                                  1,
                                  None,
                                  3,
                                  10),
                                 ('tt_a_ara_tbr_hydrant_idleAwesome3',
                                  1,
                                  1,
                                  None,
                                  3,
                                  10)),
     Globals.DonaldsDreamlandId: (('tt_a_ara_ddl_hydrant_idle0',
                                         3,
                                         10,
                                         None,
                                         0,
                                         0),
                                        ('tt_a_ara_ddl_hydrant_idle1',
                                         1,
                                         1,
                                         None,
                                         0,
                                         0),
                                        ('tt_a_ara_ddl_hydrant_idle2',
                                         1,
                                         1,
                                         None,
                                         0,
                                         0),
                                        ('tt_a_ara_ddl_hydrant_idleAwesome3',
                                         1,
                                         1,
                                         None,
                                         0,
                                         0))}
    ZoneToIdleIntoFightAnims = {Globals.ToontownCentralId: 'tt_a_ara_ttc_hydrant_idleIntoFight',
     Globals.DonaldsDockId: 'tt_a_ara_ttc_hydrant_idleIntoFight',
     Globals.DaisyGardensId: 'tt_a_ara_dga_hydrant_idleIntoFight',
     Globals.MinniesMelodylandId: 'tt_a_ara_mml_hydrant_idleIntoFight',
     Globals.TheBrrrghId: 'tt_a_ara_tbr_hydrant_idleIntoFight',
     Globals.DonaldsDreamlandId: 'tt_a_ara_ddl_hydrant_idleIntoFight'}
    ZoneToVictoryAnims = {Globals.ToontownCentralId: 'tt_a_ara_ttc_hydrant_victoryDance',
     Globals.DonaldsDockId: 'tt_a_ara_ttc_hydrant_victoryDance',
     Globals.DaisyGardensId: 'tt_a_ara_dga_hydrant_victoryDance',
     Globals.MinniesMelodylandId: 'tt_a_ara_mml_hydrant_victoryDance',
     Globals.TheBrrrghId: 'tt_a_ara_tbr_hydrant_victoryDance',
     Globals.DonaldsDreamlandId: 'tt_a_ara_ddl_hydrant_victoryDance'}
    ZoneToSadAnims = {Globals.ToontownCentralId: 'tt_a_ara_ttc_hydrant_fightSad',
     Globals.DonaldsDockId: 'tt_a_ara_ttc_hydrant_fightSad',
     Globals.DaisyGardensId: 'tt_a_ara_dga_hydrant_fightSad',
     Globals.MinniesMelodylandId: 'tt_a_ara_mml_hydrant_fightSad',
     Globals.TheBrrrghId: 'tt_a_ara_tbr_hydrant_fightSad',
     Globals.DonaldsDreamlandId: 'tt_a_ara_ddl_hydrant_fightSad'}
    ZoneToFightAnims = {Globals.ToontownCentralId: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
     Globals.DonaldsDockId: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
     Globals.DaisyGardensId: ('tt_a_ara_dga_hydrant_fightBoost', 'tt_a_ara_dga_hydrant_fightCheer', 'tt_a_ara_dga_hydrant_fightIdle'),
     Globals.MinniesMelodylandId: ('tt_a_ara_mml_hydrant_fightBoost', 'tt_a_ara_mml_hydrant_fightCheer', 'tt_a_ara_mml_hydrant_fightIdle'),
     Globals.TheBrrrghId: ('tt_a_ara_tbr_hydrant_fightBoost', 'tt_a_ara_tbr_hydrant_fightCheer', 'tt_a_ara_tbr_hydrant_fightIdle'),
     Globals.DonaldsDreamlandId: ('tt_a_ara_ddl_hydrant_fightBoost', 'tt_a_ara_ddl_hydrant_fightCheer', 'tt_a_ara_ddl_hydrant_fightIdle')}
    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        self.leftWater = None
        self.rightWater = None
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(self, node, Globals.HYDRANTS_BUFF_BATTLES)
        return

    def setupActor(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)
        if not self.hoodId == Globals.TheBrrrghId:
            water = loader.loadModel('phase_5/models/char/tt_m_efx_hydrantSquirt')
            self.leftWater = water.find('**/efx_hydrantSquirtLeft')
            self.rightWater = water.find('**/efx_hydrantSquirtRight')
            dx_left_water = self.node.find('**/dx_left_water')
            if self.leftWater:
                self.leftWater.reparentTo(dx_left_water)
                base.leftWater = self.leftWater
                self.leftWater.hide()
            else:
                self.notify.warning('couldnt find %s in rig for hood %d' % ('dx_left_water', self.hoodId))
            dx_right_water = self.node.find('**/dx_right_water')
            if self.rightWater:
                self.rightWater.reparentTo(dx_right_water)
                self.rightWater.hide()
            else:
                self.notify.warning('couldnt find %s in rig for hood %d' % ('dx_left_water', self.hoodId))

    def hideWater(self):
        if self.leftWater:
            self.leftWater.hide()
        if self.rightWater:
            self.rightWater.hide()

    def showWater(self):
        if self.leftWater:
            self.leftWater.show()
        if self.rightWater:
            self.rightWater.show()

    def hasOverrideIval(self, origAnimName):
        result = False
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == Globals.TheBrrrghId:
            result = True
        return result

    def getOverrideIval(self, origAnimName):
        result = Sequence()
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == Globals.TheBrrrghId:
            result.append(Func(self.showWater))
            if 'fightBoost' in origAnimName:
                animKey = 'fight0'
            else:
                animKey = 'fight1'
            animAndSound = self.createAnimAndSoundIval(animKey)
            result.append(animAndSound)
            result.append(Func(self.hideWater))
        return result