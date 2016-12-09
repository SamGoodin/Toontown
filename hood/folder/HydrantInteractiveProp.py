from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from hood.folder import InteractiveAnimatedProp
from hood.folder import GenericAnimatedProp
import Globals

class HydrantInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantInteractiveProp')
    BattleCheerText = Globals.InteractivePropTrackBonusTerms[5]
    ZoneToIdles = {Globals.ToontownCentral: (('tt_a_ara_ttc_hydrant_idle0',
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
     Globals.DonaldsDock: (('tt_a_ara_ttc_hydrant_idle0',
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
     Globals.DaisyGardens: (('tt_a_ara_dga_hydrant_idle0',
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
     Globals.MinniesMelodyland: (('tt_a_ara_mml_hydrant_idle0',
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
     Globals.TheBrrrgh: (('tt_a_ara_tbr_hydrant_idleShiver1',
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
     Globals.DonaldsDreamland: (('tt_a_ara_ddl_hydrant_idle0',
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
    ZoneToIdleIntoFightAnims = {Globals.ToontownCentral: 'tt_a_ara_ttc_hydrant_idleIntoFight',
     Globals.DonaldsDock: 'tt_a_ara_ttc_hydrant_idleIntoFight',
     Globals.DaisyGardens: 'tt_a_ara_dga_hydrant_idleIntoFight',
     Globals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_idleIntoFight',
     Globals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_idleIntoFight',
     Globals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_idleIntoFight'}
    ZoneToVictoryAnims = {Globals.ToontownCentral: 'tt_a_ara_ttc_hydrant_victoryDance',
     Globals.DonaldsDock: 'tt_a_ara_ttc_hydrant_victoryDance',
     Globals.DaisyGardens: 'tt_a_ara_dga_hydrant_victoryDance',
     Globals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_victoryDance',
     Globals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_victoryDance',
     Globals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_victoryDance'}
    ZoneToSadAnims = {Globals.ToontownCentral: 'tt_a_ara_ttc_hydrant_fightSad',
     Globals.DonaldsDock: 'tt_a_ara_ttc_hydrant_fightSad',
     Globals.DaisyGardens: 'tt_a_ara_dga_hydrant_fightSad',
     Globals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_fightSad',
     Globals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_fightSad',
     Globals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_fightSad'}
    ZoneToFightAnims = {Globals.ToontownCentral: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
     Globals.DonaldsDock: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
     Globals.DaisyGardens: ('tt_a_ara_dga_hydrant_fightBoost', 'tt_a_ara_dga_hydrant_fightCheer', 'tt_a_ara_dga_hydrant_fightIdle'),
     Globals.MinniesMelodyland: ('tt_a_ara_mml_hydrant_fightBoost', 'tt_a_ara_mml_hydrant_fightCheer', 'tt_a_ara_mml_hydrant_fightIdle'),
     Globals.TheBrrrgh: ('tt_a_ara_tbr_hydrant_fightBoost', 'tt_a_ara_tbr_hydrant_fightCheer', 'tt_a_ara_tbr_hydrant_fightIdle'),
     Globals.DonaldsDreamland: ('tt_a_ara_ddl_hydrant_fightBoost', 'tt_a_ara_ddl_hydrant_fightCheer', 'tt_a_ara_ddl_hydrant_fightIdle')}
    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        self.leftWater = None
        self.rightWater = None
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(self, node, Globals.HYDRANTS_BUFF_BATTLES)
        return

    def setupActor(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)
        if not self.hoodId == Globals.TheBrrrgh:
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
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == Globals.TheBrrrgh:
            result = True
        return result

    def getOverrideIval(self, origAnimName):
        result = Sequence()
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == Globals.TheBrrrgh:
            result.append(Func(self.showWater))
            if 'fightBoost' in origAnimName:
                animKey = 'fight0'
            else:
                animKey = 'fight1'
            animAndSound = self.createAnimAndSoundIval(animKey)
            result.append(animAndSound)
            result.append(Func(self.hideWater))
        return result