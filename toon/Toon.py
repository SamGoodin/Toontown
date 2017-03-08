import random

from direct.actor.Actor import Actor
from direct.controls import ControlManager
from direct.controls.GhostWalker import GhostWalker
from direct.controls.GravityWalker import GravityWalker
from direct.controls.ObserverWalker import ObserverWalker
from direct.controls.SwimWalker import SwimWalker
from direct.controls.TwoDWalker import TwoDWalker
from direct.distributed.ClockDelta import *
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.task import Task
from panda3d.core import *
from gui.nametag import NametagGlobals
from gui.nametag.NametagGroup import NametagGroup
import Globals
from gui.LaffMeter import LaffMeter
from toon.ShadowCaster import ShadowCaster

allColorsList = [(1.0, 1.0, 1.0, 1.0),
                 (0.96875, 0.691406, 0.699219, 1.0),
                 (0.933594, 0.265625, 0.28125, 1.0),
                 (0.863281, 0.40625, 0.417969, 1.0),
                 (0.710938, 0.234375, 0.4375, 1.0),
                 (0.570312, 0.449219, 0.164062, 1.0),
                 (0.640625, 0.355469, 0.269531, 1.0),
                 (0.996094, 0.695312, 0.511719, 1.0),
                 (0.832031, 0.5, 0.296875, 1.0),
                 (0.992188, 0.480469, 0.167969, 1.0),
                 (0.996094, 0.898438, 0.320312, 1.0),
                 (0.996094, 0.957031, 0.597656, 1.0),
                 (0.855469, 0.933594, 0.492188, 1.0),
                 (0.550781, 0.824219, 0.324219, 1.0),
                 (0.242188, 0.742188, 0.515625, 1.0),
                 (0.304688, 0.96875, 0.402344, 1.0),
                 (0.433594, 0.90625, 0.835938, 1.0),
                 (0.347656, 0.820312, 0.953125, 1.0),
                 (0.191406, 0.5625, 0.773438, 1.0),
                 (0.558594, 0.589844, 0.875, 1.0),
                 (0.285156, 0.328125, 0.726562, 1.0),
                 (0.460938, 0.378906, 0.824219, 1.0),
                 (0.546875, 0.28125, 0.75, 1.0),
                 (0.726562, 0.472656, 0.859375, 1.0),
                 (0.898438, 0.617188, 0.90625, 1.0),
                 (0.7, 0.7, 0.8, 1.0),
                 (0.3, 0.3, 0.35, 1.0)]

Shirts = ['phase_3/maps/desat_shirt_1.jpg',
 'phase_3/maps/desat_shirt_2.jpg',
 'phase_3/maps/desat_shirt_3.jpg',
 'phase_3/maps/desat_shirt_4.jpg',
 'phase_3/maps/desat_shirt_5.jpg',
 'phase_3/maps/desat_shirt_6.jpg',
 'phase_3/maps/desat_shirt_7.jpg',
 'phase_3/maps/desat_shirt_8.jpg',
 'phase_3/maps/desat_shirt_9.jpg',
 'phase_3/maps/desat_shirt_10.jpg',
 'phase_3/maps/desat_shirt_15.jpg',
 'phase_3/maps/desat_shirt_16.jpg',
 'phase_3/maps/desat_shirt_19.jpg',
 'phase_3/maps/desat_shirt_20.jpg',
 'phase_4/maps/male_shirt1.jpg',
 'phase_4/maps/male_shirt2_palm.jpg',
 'phase_4/maps/male_shirt3c.jpg',
 'phase_4/maps/shirt_ghost.jpg',
 'phase_4/maps/shirt_pumkin.jpg',
 'phase_4/maps/holiday_shirt1.jpg',
 'phase_4/maps/holidayShirt3b.jpg',
 'phase_4/maps/shirtMale4B.jpg',
 'phase_4/maps/shirt6New.jpg',
 'phase_4/maps/shirtMaleNew7.jpg',
 'phase_4/maps/Vday1Shirt5.jpg',
 'phase_4/maps/Vday1Shirt6SHD.jpg',
 'phase_4/maps/Vday1Shirt4.jpg',
 'phase_4/maps/Vday_shirt2c.jpg',
 'phase_4/maps/shirtTieDyeNew.jpg',
 'phase_4/maps/male_shirt1.jpg',
 'phase_4/maps/StPats_shirt1.jpg',
 'phase_4/maps/StPats_shirt2.jpg',
 'phase_4/maps/ContestfishingVestShirt2.jpg',
 'phase_4/maps/ContestFishtankShirt1.jpg',
 'phase_4/maps/ContestPawShirt1.jpg',
 'phase_4/maps/CowboyShirt1.jpg',
 'phase_4/maps/CowboyShirt2.jpg',
 'phase_4/maps/CowboyShirt3.jpg',
 'phase_4/maps/CowboyShirt4.jpg',
 'phase_4/maps/CowboyShirt5.jpg',
 'phase_4/maps/CowboyShirt6.jpg',
 'phase_4/maps/4thJulyShirt1.jpg',
 'phase_4/maps/4thJulyShirt2.jpg',
 'phase_4/maps/shirt_Cat7_01.jpg',
 'phase_4/maps/shirt_Cat7_02.jpg',
 'phase_4/maps/contest_backpack3.jpg',
 'phase_4/maps/contest_leder.jpg',
 'phase_4/maps/contest_mellon2.jpg',
 'phase_4/maps/contest_race2.jpg',
 'phase_4/maps/PJBlueBanana2.jpg',
 'phase_4/maps/PJRedHorn2.jpg',
 'phase_4/maps/PJGlasses2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_desat4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_summer2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_marathon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine3.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistA.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mailbox.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_loonyLabs.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_hydrant.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_doodle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_getConnectedMoverShaker.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_anniversary.jpg']

Sleeves = ['phase_3/maps/desat_sleeve_1.jpg',
 'phase_3/maps/desat_sleeve_2.jpg',
 'phase_3/maps/desat_sleeve_3.jpg',
 'phase_3/maps/desat_sleeve_4.jpg',
 'phase_3/maps/desat_sleeve_5.jpg',
 'phase_3/maps/desat_sleeve_6.jpg',
 'phase_3/maps/desat_sleeve_7.jpg',
 'phase_3/maps/desat_sleeve_8.jpg',
 'phase_3/maps/desat_sleeve_9.jpg',
 'phase_3/maps/desat_sleeve_10.jpg',
 'phase_3/maps/desat_sleeve_15.jpg',
 'phase_3/maps/desat_sleeve_16.jpg',
 'phase_3/maps/desat_sleeve_19.jpg',
 'phase_3/maps/desat_sleeve_20.jpg',
 'phase_4/maps/male_sleeve1.jpg',
 'phase_4/maps/male_sleeve2_palm.jpg',
 'phase_4/maps/male_sleeve3c.jpg',
 'phase_4/maps/shirt_Sleeve_ghost.jpg',
 'phase_4/maps/shirt_Sleeve_pumkin.jpg',
 'phase_4/maps/holidaySleeve1.jpg',
 'phase_4/maps/holidaySleeve3.jpg',
 'phase_4/maps/male_sleeve4New.jpg',
 'phase_4/maps/sleeve6New.jpg',
 'phase_4/maps/SleeveMaleNew7.jpg',
 'phase_4/maps/Vday5Sleeve.jpg',
 'phase_4/maps/Vda6Sleeve.jpg',
 'phase_4/maps/Vday_shirt4sleeve.jpg',
 'phase_4/maps/Vday2cSleeve.jpg',
 'phase_4/maps/sleeveTieDye.jpg',
 'phase_4/maps/male_sleeve1.jpg',
 'phase_4/maps/StPats_sleeve.jpg',
 'phase_4/maps/StPats_sleeve2.jpg',
 'phase_4/maps/ContestfishingVestSleeve1.jpg',
 'phase_4/maps/ContestFishtankSleeve1.jpg',
 'phase_4/maps/ContestPawSleeve1.jpg',
 'phase_4/maps/CowboySleeve1.jpg',
 'phase_4/maps/CowboySleeve2.jpg',
 'phase_4/maps/CowboySleeve3.jpg',
 'phase_4/maps/CowboySleeve4.jpg',
 'phase_4/maps/CowboySleeve5.jpg',
 'phase_4/maps/CowboySleeve6.jpg',
 'phase_4/maps/4thJulySleeve1.jpg',
 'phase_4/maps/4thJulySleeve2.jpg',
 'phase_4/maps/shirt_sleeveCat7_01.jpg',
 'phase_4/maps/shirt_sleeveCat7_02.jpg',
 'phase_4/maps/contest_backpack_sleeve.jpg',
 'phase_4/maps/Contest_leder_sleeve.jpg',
 'phase_4/maps/contest_mellon_sleeve2.jpg',
 'phase_4/maps/contest_race_sleeve.jpg',
 'phase_4/maps/PJSleeveBlue.jpg',
 'phase_4/maps/PJSleeveRed.jpg',
 'phase_4/maps/PJSleevePurple.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_desat4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_marathon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine3.jpg',
 'phase_4/maps/tt_t_chr_shirtSleeve_scientist.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mailbox.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_loonyLabs.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_hydrant.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_doodle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_getConnectedMoverShaker.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_anniversary.jpg']

BoyShorts = ['phase_3/maps/desat_shorts_1.jpg',
 'phase_3/maps/desat_shorts_2.jpg',
 'phase_3/maps/desat_shorts_4.jpg',
 'phase_3/maps/desat_shorts_6.jpg',
 'phase_3/maps/desat_shorts_7.jpg',
 'phase_3/maps/desat_shorts_8.jpg',
 'phase_3/maps/desat_shorts_9.jpg',
 'phase_3/maps/desat_shorts_10.jpg',
 'phase_4/maps/VdayShorts2.jpg',
 'phase_4/maps/shorts4.jpg',
 'phase_4/maps/shorts1.jpg',
 'phase_4/maps/shorts5.jpg',
 'phase_4/maps/CowboyShorts1.jpg',
 'phase_4/maps/CowboyShorts2.jpg',
 'phase_4/maps/4thJulyShorts1.jpg',
 'phase_4/maps/shortsCat7_01.jpg',
 'phase_4/maps/Blue_shorts_1.jpg',
 'phase_4/maps/Red_shorts_1.jpg',
 'phase_4/maps/Purple_shorts_1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter3.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter4.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween3.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistA.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistB.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistC.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing05.jpg']

LegDict = {'s': '/models/char/tt_a_chr_dgs_shorts_legs_',
           'm': '/models/char/tt_a_chr_dgm_shorts_legs_',
           'l': '/models/char/tt_a_chr_dgl_shorts_legs_'}

LegsAnimDict =  {'dgl': {'neutral': "phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgl_shorts_legs_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_legs_teleport'},
                 'dgm': {'neutral': "phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgm_shorts_legs_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_teleport'},
                 'dgs': {'neutral': "phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgs_shorts_legs_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport'}}

TorsoAnimDict = {'dgl': {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgl_shorts_torso_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport'},
                 'dgm': {"neutral": "phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgm_shorts_torso_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_teleport'},
                 'dgs': {"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_neutral",
                         'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_walk',
                         "run":     "phase_3/models/char/tt_a_chr_dgs_shorts_torso_run",
                         'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_jump-zstart',
                         'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_jump',
                         'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_leap_zend',
                         'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_running-jump',
                         'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_jump-zend',
                         'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_jump-zhang',
                         'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_leap_zstart',
                         'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_leap_zhang',
                         'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_torso_teleport'}}

HeadAnimDict =  {'dll': {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral",
                         "run":     "phase_3/models/char/tt_a_chr_dgl_shorts_head_run",
                         'book':    'phase_3.5/models/char/tt_a_chr_dgl_shorts_head_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_head_teleport'},
                 'dls': {"neutral": "phase_3/models/char/tt_a_chr_dgm_shorts_head_neutral",
                         "run":     "phase_3/models/char/tt_a_chr_dgm_shorts_head_run",
                         'book':    'phase_3.5/models/char/tt_a_chr_dgm_shorts_head_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_head_teleport'},
                 'dsl': {"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_head_neutral",
                         "run":     "phase_3/models/char/tt_a_chr_dgs_shorts_head_run",
                         'book':    'phase_3.5/models/char/tt_a_chr_dgs_shorts_head_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_head_teleport'},
                 'dss': {'neutral': 'phase_3/models/char/tt_a_chr_dgm_skirt_head_neutral',
                         "run":     "phase_3/models/char/tt_a_chr_dgm_skirt_head_run",
                         'book':    'phase_3.5/models/char/tt_a_chr_dgm_skirt_head_book',
                         'teleport': 'phase_3.5/models/char/tt_a_chr_dgm_skirt_head_teleport'}}

DogMuzzleDict = {'dls': 'phase_3/models/char/dogMM_Shorts-headMuzzles-1000',
 'dss': 'phase_3/models/char/dogMM_Skirt-headMuzzles-1000',
 'dsl': 'phase_3/models/char/dogSS_Shorts-headMuzzles-1000',
 'dll': 'phase_3/models/char/dogLL_Shorts-headMuzzles-1000'}

HeadDict = {
            'dss': 'phase_3/models/char/tt_a_chr_dgm_skirt_head_1000',
            'dsl': 'phase_3/models/char/tt_a_chr_dgs_shorts_head_1000',
            'dls': 'phase_3/models/char/tt_a_chr_dgm_shorts_head_1000',
            'dll': 'phase_3/models/char/tt_a_chr_dgl_shorts_head_1000',
            'mouse': 'phase_3/models/char/mouse-heads-1000',
            'rabbit': 'phase_3/models/char/rabbit-heads-1000',
            'pig': 'phase_3/models/char/pig-heads-1000',
            'monkey': 'phase_3/models/char/monkey-heads-1000',
            'horse': 'phase_3/models/char/horse-heads-1000',
            'duck': 'phase_3/models/char/duck-heads-1000',
            'cat': 'phase_3/models/char/cat-heads-1000',
            'bear': 'phase_3/models/char/bear-heads-1000'
        }


class Toon(Actor, ShadowCaster):
    sleepTimeout = base.config.GetInt('sleep-timeout', 120)

    def __init__(self):
        Actor.__init__(self)
        ShadowCaster.__init__(self)
        self.controlManager = ControlManager.ControlManager(True, False)
        self.head = None
        self.legs = None
        self.torso = None
        self.forceJumpIdle = False
        self.toon = None
        self.__bookActors = []
        self.__holeActors = []
        self.sleepCallback = None
        self.animalType = None
        self.headColor = None
        self.torsoColor = None
        self.__stareAtName = 'stareAt-'
        self.__lookName = 'look-'
        self.legColor = None
        self.avatarControlsEnabled = None
        self.jumpLandAnimFixTask = None
        self.effectTrack = None
        self.emoteTrack = None
        self.runTimeout = 2.5
        self.sleepFlag = 0
        self.isDisguised = 0
        self.movingFlag = 0
        self.swimmingFlag = 0
        self.forwardSpeed = 0.0
        self.rotateSpeed = 0.0
        self.hp = 100
        self.animMultiplier = 1.0
        self.randGen = random.Random()
        self.randGen.seed(random.random())
        self.animFSM = ClassicFSM('Toon', [State('off', self.enterOff, self.exitOff),
                                           State('neutral', self.enterNeutral, self.exitNeutral),
                                           State('run', self.enterRun, self.exitRun),
                                           State('jump', self.enterJump, self.exitJump),
                                           State('jumpAirborne', self.enterJumpAirborne, self.exitJumpAirborne),
                                           State('jumpLand', self.enterJumpLand, self.exitJumpLand),
                                           State('Happy', self.enterHappy, self.exitHappy),
                                           State('openBook', self.enterBook, self.exitBook, ['readBook', 'closeBook']),
                                           State('readBook', self.enterReadBook, self.exitReadBook),
                                           State('closeBook', self.enterCloseBook, self.exitCloseBook),
                                           State('teleportOut', self.enterTeleportOut, self.exitTeleportOut),
                                           State('TeleportIn', self.enterTeleportIn, self.exitTeleportIn)],
                                  'off', 'off')
        animStateList = self.animFSM.getStates()
        self.animFSM.enterInitialState()
        self.cheesyEffect = None
        self.standWalkRunReverse = None
        self.__stareAtNode = NodePath()
        self.__defaultStarePoint = Point3(0, 0, 0)
        self.__stareAtPoint = self.__defaultStarePoint
        self.__stareAtTime = 0
        self.lookAtTrack = None
        self.lookAtPositionCallbackArgs = None
        self.soundTeleport = base.loadSfx('phase_3.5/audio/sfx/AV_teleport.ogg')
        self.nametagNodePath = None
        self.nametag = NametagGroup()
        self.nametag.setAvatar(self)
        self.nametag.setFont(Globals.getInterfaceFont())
        self.nametag.setChatFont(Globals.getInterfaceFont())
        self.nametag3d = self.attachNewNode('nametag3d')
        self.nametag3d.setTag('cam', 'nametag')
        self.nametag3d.setLightOff()
        Globals.renderReflection(False, self.nametag3d, 'otp_avatar_nametag', None)
        self.getGeomNode().showThrough(BitMask32.bit(2))
        self.nametag3d.hide(BitMask32.bit(2))
        self.collTube = None
        self.battleTube = None
        self.ghostMode = 0

    def enterNeutral(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * self.randGen.random()))
        self.loop(anim, restart=0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim
        self.setActiveShadow(1)

    def exitNeutral(self):
        self.stop()

    def getTeleportInTrack(self):
        hole = self.getHoleActors()[0]
        hole.setBin('shadow', 0)
        hole.setDepthTest(0)
        hole.setDepthWrite(0)
        holeTrack = Sequence()
        holeTrack.append(Func(hole.reparentTo, self))
        pos = Point3(0, -2.4, 0)
        holeTrack.append(Func(hole.setPos, self, pos))
        holeTrack.append(ActorInterval(hole, 'hole', startTime=3.4, endTime=3.1))
        holeTrack.append(Wait(0.6))
        holeTrack.append(ActorInterval(hole, 'hole', startTime=3.1, endTime=3.4))

        def restoreHole(hole):
            hole.setPos(0, 0, 0)
            hole.detachNode()
            hole.clearBin()
            hole.clearDepthTest()
            hole.clearDepthWrite()

        holeTrack.append(Func(restoreHole, hole))
        toonTrack = Sequence(Wait(0.3), Func(self.getGeomNode().show), Func(self.nametag3d.show),
                             ActorInterval(self, 'jump', startTime=0.45))
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('teleportIn')
        else:
            trackName = 'teleportIn'
        return Parallel(holeTrack, toonTrack, name=trackName)

    def enterTeleportIn(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.show()
        self.playingAnim = 'teleport'
        self.pose('teleport', self.getNumFrames('teleport') - 1)
        self.getGeomNode().hide()
        self.nametag3d.hide()
        self.track = self.getTeleportInTrack()
        if callback:
            self.track.setDoneEvent(self.track.getName())
            self.acceptOnce(self.track.getName(), callback, extraArgs)
        self.track.start(ts)
        self.setActiveShadow(0)

    def exitTeleportIn(self):
        self.playingAnim = None
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        if not self.ghostMode and not self.isDisguised:
            self.getGeomNode().show()
            self.nametag3d.show()
        return

    def getHoleActors(self):
        if self.__holeActors:
            return self.__holeActors
        holeActor = Actor('phase_3.5/models/props/portal-mod', {'hole': 'phase_3.5/models/props/portal-chan'})
        holeActor2 = Actor(other=holeActor)
        holeActor3 = Actor(other=holeActor)
        self.__holeActors = [holeActor, holeActor2, holeActor3]
        for ha in self.__holeActors:
            holeName = 'toon-portal'
            ha.setName(holeName)

        return self.__holeActors

    def getTeleportOutTrack(self, autoFinishTrack=1):

        def showHoles(holes, hands):
            for hole, hand in zip(holes, hands):
                hole.reparentTo(hand)

        def reparentHoles(holes, toon):
            holes[0].reparentTo(toon)
            holes[1].detachNode()
            holes[2].detachNode()
            holes[0].setBin('shadow', 0)
            holes[0].setDepthTest(0)
            holes[0].setDepthWrite(0)

        def cleanupHoles(holes):
            holes[0].detachNode()
            holes[0].clearBin()
            holes[0].clearDepthTest()
            holes[0].clearDepthWrite()

        holes = self.getHoleActors()
        hands = self.getRightHands()
        holeTrack = Track((0.0, Func(showHoles, holes, hands)),
                          (0.5, SoundInterval(self.soundTeleport, node=self)),
                          (1.708, Func(reparentHoles, holes, self)), (3.4, Func(cleanupHoles, holes)))
        trackName = 'teleportOut'
        track = Parallel(holeTrack, name=trackName, autoFinish=autoFinishTrack)
        for hole in holes:
            track.append(ActorInterval(hole, 'hole', duration=3.4))

        track.append(ActorInterval(self, 'teleport', duration=3.4))
        return track

    def enterTeleportOut(self, callback=None, extraArgs=[]):
        messenger.send('hideAllGui')
        self.disableAvatarControls()
        self.track = self.getTeleportOutTrack()
        self.track.setDoneEvent(self.track.getName())
        self.acceptOnce(self.track.getName(), self.exitTeleportOut)
        holeClip = PlaneNode('holeClip')
        self.holeClipPath = self.attachNewNode(holeClip)
        self.getGeomNode().setClipPlane(self.holeClipPath)
        self.track.start(0)
        self.setActiveShadow(0)

    def exitTeleportOut(self):
        self.track.finish()
        messenger.send('showAllGui')
        self.enableAvatarControls()

    def enterHappy(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (('neutral', 1.0),
                                    ('walk', 1.0),
                                    ('run', 1.0),
                                    ('walk', -1.0))
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)
        self.setActiveShadow(1)
        return

    def exitHappy(self):
        self.standWalkRunReverse = None
        self.stop()
        return

    def enterBook(self):
        bookTracks = Parallel()
        for bookActor in self.getBookActors():
            bookTracks.append(ActorInterval(bookActor, 'book', startTime=1.2, endTime=1.5))
        bookTracks.append(ActorInterval(self, 'book', startTime=1.2, endTime=1.5))
        self.track = Sequence(Func(self.showBooks), bookTracks, Wait(0.1), name='openBook')
        self.track.start(0)
        self.setActiveShadow(0)

    def getBookActors(self):
        if self.__bookActors:
            return self.__bookActors
        bookActor = Actor('phase_3.5/models/props/book-mod', {'book': 'phase_3.5/models/props/book-chan'})
        bookActor2 = Actor(other=bookActor)
        bookActor3 = Actor(other=bookActor)
        self.__bookActors = [bookActor, bookActor2, bookActor3]
        hands = self.getRightHands()
        for bookActor, hand in zip(self.__bookActors, hands):
            bookActor.reparentTo(hand)
            bookActor.hide()

        return self.__bookActors

    def showBooks(self):
        for bookActor in self.getBookActors():
            bookActor.show()

    def hideBooks(self):
        for bookActor in self.getBookActors():
            bookActor.hide()

    def exitBook(self):
        self.track.finish()
        self.track = None
        self.hideBooks()

    def enterReadBook(self):
        self.showBooks()
        for bookActor in self.getBookActors():
            bookActor.pingpong('book', fromFrame=38, toFrame=118)

        self.pingpong('book', fromFrame=38, toFrame=118)
        self.setActiveShadow(0)

    def exitReadBook(self):
        self.hideBooks()
        for bookActor in self.getBookActors():
            bookActor.stop()

    def enterCloseBook(self):
        messenger.send('disableGui')
        bookTracks = Parallel()
        for bookActor in self.getBookActors():
            bookTracks.append(ActorInterval(bookActor, 'book', startTime=4.96, endTime=6.5))

        bookTracks.append(ActorInterval(self, 'book', startTime=4.96, endTime=6.5))
        self.track = Sequence(Func(self.showBooks), bookTracks, Func(self.hideBooks), name='closeBook')
        self.track.start(0)
        self.setActiveShadow(0)

    def exitCloseBook(self):
        self.track.finish()
        self.track = None
        messenger.send('enableGui')

    def enterJumpAirborne(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if not self.isDisguised:
            if self.playingAnim == 'neutral' or self.forceJumpIdle:
                anim = 'jump-idle'
            else:
                anim = 'running-jump-idle'
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.loop(anim)
        self.setActiveShadow(1)

    def exitJumpAirborne(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterJump(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if not self.isDisguised:
            if self.playingAnim == 'neutral':
                anim = 'jump'
            else:
                anim = 'running-jump'
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.play(anim)
        self.setActiveShadow(1)

    def exitJump(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterJumpLand(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if not self.isDisguised:
            if self.playingAnim == 'running-jump-idle':
                anim = 'running-jump-land'
                skipStart = 0.2
            else:
                anim = 'jump-land'
                skipStart = 0.0
            self.playingAnim = anim
            self.setPlayRate(animMultiplier, anim)
            self.play(anim)
        self.setActiveShadow(1)

    def exitJumpLand(self):
        self.stop()
        self.playingAnim = 'neutral'

    def setSpeed(self, forwardSpeed, rotateSpeed):
        self.forwardSpeed = forwardSpeed
        self.rotateSpeed = rotateSpeed
        action = None
        if self.standWalkRunReverse != None:
            if forwardSpeed >= Globals.RunCutOff:
                action = Globals.RUN_INDEX
            elif forwardSpeed > Globals.WalkCutOff:
                action = Globals.WALK_INDEX
            elif forwardSpeed < -Globals.WalkCutOff:
                action = Globals.REVERSE_INDEX
            elif rotateSpeed != 0.0:
                action = Globals.WALK_INDEX
            else:
                action = Globals.STAND_INDEX
            anim, rate = self.standWalkRunReverse[action]
            if anim != self.playingAnim:
                self.playingAnim = anim
                self.playingRate = rate
                self.stop()
                self.loop(anim)
                self.setPlayRate(rate, anim)
                if self.isDisguised:
                    rightHand = self.suit.rightHand
                    numChildren = rightHand.getNumChildren()
                    if numChildren > 0:
                        anim = 'tray-' + anim
                        if anim == 'tray-run':
                            anim = 'tray-walk'
                    self.suit.stop()
                    self.suit.loop(anim)
                    self.suit.setPlayRate(rate, anim)
            elif rate != self.playingRate:
                self.playingRate = rate
                if not self.isDisguised:
                    self.setPlayRate(rate, anim)
                else:
                    self.suit.setPlayRate(rate, anim)
            showWake, wakeWaterHeight = (None, None)
            if showWake and self.getZ(render) < wakeWaterHeight and abs(forwardSpeed) > Globals.WalkCutOff:
                currT = globalClock.getFrameTime()
                deltaT = currT - self.lastWakeTime
                if action == Globals.RUN_INDEX and deltaT > Globals.WakeRunDelta or deltaT > Globals.WakeWalkDelta:
                    self.getWake().createRipple(wakeWaterHeight, rate=1, startFrame=4)
                    self.lastWakeTime = currT
        return action

    def enterOff(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.setActiveShadow(0)
        self.playingAnim = None
        return

    def exitOff(self):
        pass

    def enterRun(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.loop('run')
        self.setPlayRate(animMultiplier, 'run')
        self.setActiveShadow(1)

    def exitRun(self):
        self.stop()

    def getColorList(self):
        return allColorsList

    def getShirtsList(self):
        return Shirts

    def getShortsList(self):
        return BoyShorts

    def getRightHands(self):
        return self.rightHands

    def createAdvancedToon(self, species, torsoType, legType):
        if species == "dog":
            headType = random.choice(["dss", "dsl", "dls", "dll"])
            head = HeadDict[headType]
        else:
            headType = None
            head = HeadDict[species]

        TorsoDict = {
            'dgs': 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000',
            'dgm': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000',
            'dgl': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000'
        }
        torso = TorsoDict[torsoType]
        self.torsoStyle = torsoType

        LegDict = {
            'dgs': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000',
            'dgm': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000',
            'dgl': 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000'
        }
        legs = LegDict[legType]
        self.legStyle = legType
        self.head = self.handleHead(headType, self.species)
        self.loadModel(self.head, 'head')
        self.loadModel(torso, "torso")
        self.loadModel(legs, "legs")
        self.getPart("legs").findAllMatches('**/boots_short').stash()
        self.getPart("legs").findAllMatches('**/boots_long').stash()
        self.getPart("legs").findAllMatches('**/shoes').stash()
        bodyScale = Globals.toonBodyScales[self.species]
        headScale = Globals.toonHeadScales[self.species]
        self.getGeomNode().setScale(headScale[0] * bodyScale * 1.3, headScale[1] * bodyScale * 1.3,
                                    headScale[2] * bodyScale * 1.3)
        self.loadAnims(TorsoAnimDict[torsoType], "torso")
        self.loadAnims(LegsAnimDict[legType], "legs")
        self.attach("head", "torso", "def_head")
        self.attach("torso", "legs", "joint_hips")
        rightHand = NodePath('rightHand')
        self.rightHands = []
        if not self.getPart('torso').find('**/def_joint_right_hold').isEmpty():
            hand = self.getPart('torso').find('**/def_joint_right_hold')
        self.rightHands.append(hand)
        self.rescaleToon()

    def createToonWithData(self, species, headType, torsoType, legType, headColor, torsoColor, legColor, shirt, shorts, name):
        self.species = species

        if species == "dog":
            head = HeadDict[headType]
        else:
            head = HeadDict[species]
        self.headStyle = headType
        self.headType = head

        TorsoDict = {
            'dgs': 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000',
            'dgm': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000',
            'dgl': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000'
        }
        torso = TorsoDict[torsoType]
        self.torsoStyle = torsoType

        LegDict = {
            'dgs': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000',
            'dgm': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000',
            'dgl': 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000'
        }
        legs = LegDict[legType]
        self.legStyle = legType
        self.headColor = tuple(headColor)
        self.torsoColor = tuple(torsoColor)
        self.legColor = tuple(legColor)
        self.head = self.handleHead(headType, self.species, headColor)
        self.loadModel(self.head, 'head')
        self.loadModel(torso, "torso")
        self.loadModel(legs, "legs")
        self.getPart("legs").findAllMatches('**/boots_short').stash()
        self.getPart("legs").findAllMatches('**/boots_long').stash()
        self.getPart("legs").findAllMatches('**/shoes').stash()
        self.bodyScale = Globals.toonBodyScales[self.species]
        self.headScale = Globals.toonHeadScales[self.species]
        self.getGeomNode().setScale(self.headScale[0] * self.bodyScale * 1.3, self.headScale[1] * self.bodyScale * 1.3,
                                    self.headScale[2] * self.bodyScale * 1.3)
        self.loadAnims(TorsoAnimDict[torsoType], "torso")
        self.loadAnims(LegsAnimDict[legType], "legs")
        self.attach("head", "torso", "def_head")
        self.attach("torso", "legs", "joint_hips")
        self.setTorsoColor(tuple(torsoColor))
        self.setLegsColor(tuple(legColor))
        self.setName(name)
        self.setShirt(shirt)
        self.setShorts(shorts)
        rightHand = NodePath('rightHand')
        self.rightHands = []
        if not self.getPart('torso').find('**/def_joint_right_hold').isEmpty():
            hand = self.getPart('torso').find('**/def_joint_right_hold')
        self.rightHands.append(hand)
        self.rescaleToon()

    def setupLaffMeter(self):
        self.laffMeter = LaffMeter(110, 110, self.species, self.headColor)
        self.laffMeter.setScale(0.075)
        self.laffMeter.reparentTo(base.a2dBottomLeft)
        if self.species == 'monkey':
            self.laffMeter.setPos(0.153, 0.0, 0.13)
        else:
            self.laffMeter.setPos(0.133, 0.0, 0.13)

        return self.laffMeter

    def handleHead(self, headStyle, species, headColor=None, gui=None):
        head = Actor()
        if species == "dog":
            headModel = HeadDict[headStyle]
            head.loadModel(headModel, "head")
            head.loadAnims(HeadAnimDict[headStyle], 'head')
        else:
            headModel = HeadDict[species]
            head.loadModel(headModel, "head")
        if gui:
            self.fixHeadShortShort(head, gui=gui)
        else:
            self.fixHeadShortShort(head)
        self.setupMuzzlesGui(headStyle, head, species)
        if not headColor:
            headColor = random.choice(allColorsList)
        self.setHeadColor(tuple(headColor), head, species)
        if gui:
            self.__fixEyes(head, species, 1)
        else:
            self.__fixEyes(head, species)
        bodyScale = Globals.toonBodyScales[species]
        head.setScale(bodyScale / .75)
        self.species = species
        self.headColor = tuple(headColor)
        return head

    def setData(self):
        import json, os
        data = None
        headStyle = None
        dataExists = False
        if os.path.isfile("data/ToonData.json"):
            dataExists = True
            with open('data/ToonData.json') as jsonFile:
                data = json.load(jsonFile)
        buttonColors = ['red', 'green', 'purple', 'blue', 'pink', 'yellow']
        toonData = {}
        for color in buttonColors:
            toonData[color] = {}
            if dataExists:
                headStyle = data[color].get('head')
            if base.buttonPressed == color:
                toonData[color].update({
                    'species': self.species,
                    'head': self.headStyle,
                    'torso': self.bodyType,
                    'legs': self.legsType,
                    'headColor': self.headColor,
                    'torsoColor': self.torsoColor,
                    'legColor': self.legColor,
                    'name': self.getName(),
                    'lastPlayground': Globals.TTCZone,
                    'shirt': self.shirtChoice,
                    'shorts': self.shortsChoice
                })
            elif headStyle:
                toonData[color].update(data[color])
            else:
                toonData[color].update({
                    'species': None,
                    'head': None,
                    'torso': None,
                    'legs': None,
                    'headColor': None,
                    'torsoColor': None,
                    'legColor': None,
                    'name': None,
                    'lastPlayground': None,
                    'shirt': None,
                    'shorts': None
                })
        with open('data/ToonData.json', 'w') as f:
            json.dump(toonData, f, sort_keys=True, indent=2)

    def createRandomBoy(self):
        choice = random.choice(['dog', 'cat', 'horse', 'monkey', 'rabbit', 'mouse', 'duck', 'bear', 'pig'])
        self.species = choice
        self.bodyType = random.choice(['dgl', 'dgm', 'dgs'])
        self.legsType = random.choice(['dgl', 'dgm', 'dgs'])
        self.createAdvancedToon(choice, self.bodyType, self.legsType)
        self.setRandomColor()
        self.generateRandomClothing()

    def initializeNametag3d(self):
        self.deleteNametag3d()
        nametagNode = self.nametag.getNametag3d()
        self.nametagNodePath = self.nametag3d.attachNewNode(nametagNode)
        iconNodePath = self.nametag.getIcon()
        for cJoint in self.getNametagJoints():
            cJoint.clearNetTransforms()
            cJoint.addNetTransform(nametagNode)
        self.nametag.setText(self.getName())
        nametagNode.showNametag()
        nametagNode.showChat()
        nametagNode.showThought()
        nametagNode.update()
        self.nametag3d.setBin('fixed', 0)
        self.nametag.updateAll()

    def getNametagJoints(self):
        joints = []
        for lodName in self.getLODNames():
            bundle = self.getPartBundle('legs', lodName)
            joint = bundle.findChild('joint_nameTag')
            if joint:
                joints.append(joint)

        return joints

    def deleteNametag3d(self):
        if self.nametagNodePath:
            self.nametagNodePath.removeNode()
            self.nametagNodePath = None

    def getToon(self):
        return self

    def hideHead(self):
        self.getPart('head').hide()

    def delete(self):
        if 'legs' in self._Actor__commonBundleHandles:
            del self._Actor__commonBundleHandles['legs']
        if 'torso' in self._Actor__commonBundleHandles:
            del self._Actor__commonBundleHandles['torso']
        self.stop()
        self.unloadAnims()
        for part in self.getPartNames():
            self.removePart(part)
        self.species = None
        self.legsType = None
        self.bodyType = None

    def fixHeadShortShort(self, head, copy=None, gui=None):
        if gui:
            otherParts = head.findAllMatches('**/*long*')
            for partNum in xrange(0, otherParts.getNumPaths()):
                if copy:
                    otherParts.getPath(partNum).removeNode()
                else:
                    otherParts.getPath(partNum).stash()
        else:
            otherParts = head.findAllMatches('**/*long*')
            for partNum in xrange(0, otherParts.getNumPaths()):
                if copy:
                    otherParts.getPath(partNum).removeNode()
                else:
                    otherParts.getPath(partNum).stash()
            self.headStyle = self.species[:1] + "ss"
        return

    def __fixEyes(self, head, species, forGui=0):
        mode = -3
        if forGui:
            mode = -2
        head.drawInFront('eyes*', 'head-front*', mode)
        if base.config.GetBool('want-new-anims', 1):
            if not head.find('joint_pupil*').isEmpty():
                head.drawInFront('joint_pupil*', 'eyes*', -1)
            else:
                head.drawInFront('def_*_pupil', 'eyes*', -1)
        else:
            head.drawInFront('joint_pupil*', 'eyes*', -1)
        __eyes = head.find('**/eyes*')
        if not __eyes.isEmpty():
            __eyes.setColorOff()
            __lpupil = None
            __rpupil = None
            if base.config.GetBool('want-new-anims', 1):
                if not head.find('**/joint_pupilL*').isEmpty():
                    lp = head.find('**/joint_pupilL*')
                    rp = head.find('**/joint_pupilR*')
                else:
                    lp = head.find('**/def_left_pupil*')
                    rp = head.find('**/def_right_pupil*')
            else:
                lp = __eyes.find('**/joint_pupilL*')
                rp = __eyes.find('**/joint_pupilR*')
            if lp.isEmpty() or rp.isEmpty():
                print 'Unable to locate pupils.'
            else:
                leye = __eyes.attachNewNode('leye')
                reye = __eyes.attachNewNode('reye')
                lmat = Mat4(0.802174, 0.59709, 0, 0, -0.586191, 0.787531, 0.190197, 0, 0.113565, -0.152571, 0.981746, 0,
                            -0.233634, 0.418062, 0.0196875, 1)
                leye.setMat(lmat)
                rmat = Mat4(0.786788, -0.617224, 0, 0, 0.602836, 0.768447, 0.214658, 0, -0.132492, -0.16889, 0.976689,
                            0, 0.233634, 0.418062, 0.0196875, 1)
                reye.setMat(rmat)
                __lpupil = leye.attachNewNode('lpupil')
                __rpupil = reye.attachNewNode('rpupil')
                lpt = __eyes.attachNewNode('')
                rpt = __eyes.attachNewNode('')
                lpt.wrtReparentTo(__lpupil)
                rpt.wrtReparentTo(__rpupil)
                lp.reparentTo(lpt)
                rp.reparentTo(rpt)
                __lpupil.adjustAllPriorities(1)
                __rpupil.adjustAllPriorities(1)
                if species != 'dog':
                    __lpupil.flattenStrong()
                    __rpupil.flattenStrong()
        return

    def setupMuzzlesGui(self, headType, head, species):
        allMuzzles = []
        surpriseMuzzles = []
        angryMuzzles = []
        sadMuzzles = []
        smileMuzzles = []
        laughMuzzles = []

        def hideAddNonEmptyItemToList(item, list):
            if not item.isEmpty():
                item.hide()
                list.append(item)

        def hideNonEmptyItem(item):
            if not item.isEmpty():
                item.hide()

        if species != 'dog':
            muzzle = head.find('**/muzzle*neutral')
        else:
            muzzle = head.find('**/muzzle*')
            muzzles = loader.loadModel(DogMuzzleDict[headType])
            if not head.find('**/def_head').isEmpty():
                muzzles.reparentTo(head.find('**/def_head'))
            else:
                muzzles.reparentTo(head.find('**/joint_toHead'))
        surpriseMuzzle = head.find('**/muzzle*surprise')
        angryMuzzle = head.find('**/muzzle*angry')
        sadMuzzle = head.find('**/muzzle*sad')
        smileMuzzle = head.find('**/muzzle*smile')
        laughMuzzle = head.find('**/muzzle*laugh')
        allMuzzles.append(muzzle)
        hideAddNonEmptyItemToList(surpriseMuzzle, surpriseMuzzles)
        hideAddNonEmptyItemToList(angryMuzzle, angryMuzzles)
        hideAddNonEmptyItemToList(sadMuzzle, sadMuzzles)
        hideAddNonEmptyItemToList(smileMuzzle, smileMuzzles)
        hideAddNonEmptyItemToList(laughMuzzle, laughMuzzles)

    def setupMuzzles(self, head):
        self.__muzzles = []
        self.__surpriseMuzzles = []
        self.__angryMuzzles = []
        self.__sadMuzzles = []
        self.__smileMuzzles = []
        self.__laughMuzzles = []

        def hideAddNonEmptyItemToList(item, list):
            if not item.isEmpty():
                item.hide()
                list.append(item)

        def hideNonEmptyItem(item):
            if not item.isEmpty():
                item.hide()

        if self.species != 'dog':
            muzzle = self.getPart('head').find('**/muzzle*neutral')
        else:
            muzzle = self.getPart('head').find('**/muzzle*')
            muzzles = loader.loadModel(DogMuzzleDict[head])
            if not self.getPart('head').find('**/def_head').isEmpty():
                muzzles.reparentTo(self.getPart('head').find('**/def_head'))
            else:
                muzzles.reparentTo(self.getPart('head').find('**/joint_toHead'))
        surpriseMuzzle = self.find('**/muzzle*surprise')
        angryMuzzle = self.find('**/muzzle*angry')
        sadMuzzle = self.find('**/muzzle*sad')
        smileMuzzle = self.find('**/muzzle*smile')
        laughMuzzle = self.find('**/muzzle*laugh')
        self.__muzzles.append(muzzle)
        hideAddNonEmptyItemToList(surpriseMuzzle, self.__surpriseMuzzles)
        hideAddNonEmptyItemToList(angryMuzzle, self.__angryMuzzles)
        hideAddNonEmptyItemToList(sadMuzzle, self.__sadMuzzles)
        hideAddNonEmptyItemToList(smileMuzzle, self.__smileMuzzles)
        hideAddNonEmptyItemToList(laughMuzzle, self.__laughMuzzles)

    def setRandomColor(self):
        self.setRandomHeadColor()
        self.setRandomTorsoColor()
        self.setRandomLegsColor()

    def getHeadColor(self):
        parts = self.find('**/head*')
        return parts.getColor()

    def setRandomHeadColor(self):
        self.headColor = random.choice(allColorsList)
        parts = self.findAllMatches('**/head*')
        parts.setColor(self.headColor)
        if self.species == 'cat' or self.species == 'rabbit' or self.species == 'bear' or \
                        self.species == 'mouse' or self.species == 'pig':
            parts = self.findAllMatches('**/ear?-*')
            parts.setColor(self.headColor)

    def setHeadColor(self, color, gui=None, species=None):
        if gui:
            parts = gui.findAllMatches('**/head*')
            parts.setColor(color)
            if species == 'cat' or species == 'rabbit' or species == 'bear' or \
                            species == 'mouse' or species == 'pig':
                parts = gui.findAllMatches('**/ear?-*')
                parts.setColor(color)
        else:
            parts = self.findAllMatches('**/head*')
            parts.setColor(color)
            if self.species == 'cat' or self.species == 'rabbit' or self.species == 'bear' or \
                            self.species == 'mouse' or self.species == 'pig':
                parts = self.findAllMatches('**/ear?-*')
                parts.setColor(color)
            self.headColor = color

    def getTorsoColor(self):
        return self.torsoColor

    def setRandomTorsoColor(self):
        torso = self.getPart('torso')
        self.torsoColor = random.choice(allColorsList)
        for pieceName in ('arms', 'neck'):
            piece = self.find('**/' + pieceName)
            piece.setColor(self.torsoColor)
        hands = self.find('**/hands')
        hands.setColor(1, 1, 1, 1)

    def setTorsoColor(self, color):
        torso = self.getPart('torso')
        self.torsoColor = color
        for pieceName in ('arms', 'neck'):
            piece = torso.find('**/' + pieceName)
            piece.setColor(self.torsoColor)
        hands = torso.find('**/hands')
        hands.setColor(1, 1, 1, 1)

    def getLegColor(self):
        return self.legColor

    def setRandomLegsColor(self):
        legs = self.getPart('legs')
        self.legColor = random.choice(allColorsList)
        for pieceName in ('legs', 'feet'):
            piece = self.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)

    def setLegsColor(self, color):
        legs = self.getPart('legs')
        self.legColor = color
        for pieceName in ('legs', 'feet'):
            piece = legs.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)

    def generateRandomClothing(self):
        torso = self.getPart('torso')
        shirt = self.findAllMatches('**/torso-top')
        sleeves = self.findAllMatches('**/sleeves')
        bottom = self.findAllMatches('**/torso-bot')
        sizeofShirts = len(Shirts)
        self.shirtChoice = random.randrange(0, sizeofShirts)
        shirtTexture = loader.loadTexture(Shirts[self.shirtChoice])
        sleeveTexture = loader.loadTexture(Sleeves[self.shirtChoice])
        sizeofShorts = len(BoyShorts)
        self.shortsChoice = random.randrange(0, sizeofShorts)
        bottomTexture = loader.loadTexture(BoyShorts[self.shortsChoice])
        shirt.setTexture(shirtTexture, 1)
        sleeves.setTexture(sleeveTexture, 1)
        bottom.setTexture(bottomTexture, 1)

    def setShirt(self, shirt1, toon=None):
        if toon:
            torso = toon.getPart('torso')
        else:
            torso = self.getPart('torso')
        shirt = torso.findAllMatches('**/torso-top')
        sleeves = torso.findAllMatches('**/sleeves')
        self.shirtChoice = shirt1
        shirtTexture = loader.loadTexture(Shirts[self.shirtChoice])
        sleeveTexture = loader.loadTexture(Shirts[self.shirtChoice])
        shirt.setTexture(shirtTexture, 1)
        sleeves.setTexture(sleeveTexture, 1)

    def setShorts(self, shorts, toon=None):
        if toon:
            torso = toon.getPart('torso')
        else:
            torso = self.getPart('torso')
        bottom = torso.findAllMatches('**/torso-bot')
        self.shortsChoice = shorts
        bottomTexture = loader.loadTexture(BoyShorts[self.shortsChoice])
        bottom.setTexture(bottomTexture, 1)

    def rescaleToon(self):
        bodyScale = Globals.toonBodyScales[self.species]
        headScale = Globals.toonHeadScales[self.species]
        self.getGeomNode().setScale(bodyScale)
        self.getPart('head').setScale(headScale)
        self.resetHeight()

    def resetHeight(self):
        bodyScale = Globals.toonBodyScales[self.species]
        headScale = Globals.toonHeadScales[self.species][2]
        shoulderHeight = Globals.legHeightDict[self.legStyle] * bodyScale +\
                         Globals.torsoHeightDict[self.torsoStyle] * bodyScale
        height = shoulderHeight + Globals.headHeightDict[self.headStyle] * headScale
        self.shoulderHeight = shoulderHeight
        self.setHeight(height)

    def setHeight(self, height):
        self.height = height
        self.adjustNametag3d()
        if self.collTube:
            self.collTube.setPointB(0, 0, height - self.getRadius())
            if self.collNodePath:
                self.collNodePath.forceRecomputeBounds()
        if self.battleTube:
            self.battleTube.setPointB(0, 0, height - self.getRadius())

    def adjustNametag3d(self):
        self.nametag3d.setPos(0, 0, self.height + 1.5)

    def getAirborneHeight(self):
        height = self.getPos(self.shadowPlacer.shadowNodePath)
        return height.getZ() + 0.025

    def getRadius(self):
        return 1

    def initializeBodyCollisions(self, collIdStr='string'):
        '''self.collTube = CollisionTube(0, 0, 0.5, 0, 0, self.height - self.getRadius(), self.getRadius())
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collTube)
        self.collNodePath = self.attachNewNode(self.collNode)
        if self.ghostMode:
            self.collNode.setCollideMask(BitMask32(2048))
        else:
            self.collNode.setCollideMask(BitMask32(1))
        self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | BitMask32(256))'''
        pass


    def setupControls(self, avatarRadius = 1.4, floorOffset = Globals.FloorOffset, reach = 4.0,
                      wallBitmask = Globals.WallBitmask, floorBitmask = Globals.FloorBitmask,
                      ghostBitmask = Globals.GhostBitmask):
        self.cTrav = CollisionTraverser('base.cTrav')
        base.pushCTrav(self.cTrav)
        self.cTrav.setRespectPrevTransform(1)
        walkControls = GravityWalker(legacyLifter=False)
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        walkControls.setAirborneHeightFunc(self.getAirborneHeight())
        self.controlManager.add(walkControls, 'walk')
        self.physControls = walkControls
        twoDControls = TwoDWalker()
        twoDControls.setWallBitMask(wallBitmask)
        twoDControls.setFloorBitMask(floorBitmask)
        twoDControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        twoDControls.setAirborneHeightFunc(self.getAirborneHeight())
        self.controlManager.add(twoDControls, 'twoD')
        swimControls = SwimWalker()
        swimControls.setWallBitMask(wallBitmask)
        swimControls.setFloorBitMask(floorBitmask)
        swimControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        swimControls.setAirborneHeightFunc(self.getAirborneHeight())
        self.controlManager.add(swimControls, 'swim')
        ghostControls = GhostWalker()
        ghostControls.setWallBitMask(ghostBitmask)
        ghostControls.setFloorBitMask(floorBitmask)
        ghostControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        ghostControls.setAirborneHeightFunc(self.getAirborneHeight())
        self.controlManager.add(ghostControls, 'ghost')
        observerControls = ObserverWalker()
        observerControls.setWallBitMask(ghostBitmask)
        observerControls.setFloorBitMask(floorBitmask)
        observerControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        observerControls.setAirborneHeightFunc(self.getAirborneHeight())
        self.controlManager.add(observerControls, 'observer')
        self.controlManager.use('walk', self)
        self.accept('arrow_up', self.startRunWatch)
        self.accept('arrow_up-up', self.stopRunWatch)
        self.accept('control-arrow_up', self.startRunWatch)
        self.accept('control-arrow_up-up', self.stopRunWatch)
        self.accept('alt-arrow_up', self.startRunWatch)
        self.accept('alt-arrow_up-up', self.stopRunWatch)
        self.accept('shift-arrow_up', self.startRunWatch)
        self.accept('shift-arrow_up-up', self.stopRunWatch)
        self.soundRun = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_runloop.ogg')
        self.soundWalk = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_walkloop.ogg')
        self.enableAvatarControls()
        self.startTrackAnimToSpeed()
        self.setWalkSpeedNormal()

    def startTrackAnimToSpeed(self):
        taskName = 'trackAnimToSpeed'
        taskMgr.remove(taskName)
        task = Task.Task(self.trackAnimToSpeed)
        self.lastMoved = globalClock.getFrameTime()
        self.lastState = None
        self.lastAction = None
        self.trackAnimToSpeed(task)
        taskMgr.add(self.trackAnimToSpeed, taskName, 35)
        return

    def stopTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.remove(taskName)
        self.stopSound()

    def setWalkSpeedNormal(self):
        self.controlManager.setSpeeds(Globals.ToonForwardSpeed, Globals.ToonJumpForce,
                                      Globals.ToonReverseSpeed, Globals.ToonRotateSpeed)

    def startLookAround(self):
        taskMgr.remove(self.__lookName)
        t = self.randGen.random() * 5.0 + 2.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)

    def __lookAround(self, task):
        self.findSomethingToLookAt()
        t = self.randGen.random() * 4.0 + 3.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)
        return Task.done

    def findSomethingToLookAt(self):
        if self.lookAtPositionCallbackArgs != None:
            pnt = self.lookAtPositionCallbackArgs[0].getLookAtPosition(self.lookAtPositionCallbackArgs[1],
                                                                       self.lookAtPositionCallbackArgs[2])
            self.startStareAt(self, pnt)
            return
        if self.randGen.random() < 0.33:
            lookAtPnt = self.getRandomForwardLookAtPoint()
        else:
            lookAtPnt = self.__defaultStarePoint
        self.lerpLookAt(lookAtPnt, blink=1)
        return

    def getRandomForwardLookAtPoint(self):
        x = self.randGen.choice((-0.8,
                                 -0.5,
                                 0,
                                 0.5,
                                 0.8))
        z = self.randGen.choice((-0.5,
                                 0,
                                 0.5,
                                 0.8))
        return Point3(x, 1.5, z)

    def startStareAt(self, node, point):
        taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        self.__stareAtNode = node
        if point != None:
            self.__stareAtPoint = point
        else:
            self.__stareAtPoint = self.__defaultStarePoint
        self.__stareAtTime = globalClock.getFrameTime()
        taskMgr.add(self.__stareAt, self.__stareAtName)
        return

    def lerpLookAt(self, point, time=1.0, blink=0):
        '''taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        lodNames = self.getLODNames()
        if lodNames:
            lodName = lodNames[0]
        else:
            return 0
        head = self.getPart('head', lodName)
        startHpr = head.getHpr()
        startLpupil = self.__lpupil.getPos()
        startRpupil = self.__rpupil.getPos()
        self.__lookHeadAt(None, point, lod=lodName)
        self.__lookPupilsAt(None, point)
        endHpr = head.getHpr()
        endLpupil = self.__lpupil.getPos() * 0.5
        endRpupil = self.__rpupil.getPos() * 0.5
        head.setHpr(startHpr)
        self.__lpupil.setPos(startLpupil)
        self.__rpupil.setPos(startRpupil)
        if startHpr.almostEqual(endHpr, 10):
            return 0
        if blink:
            self.blinkEyes()
        lookToTgt_TimeFraction = 0.2
        lookToTgtTime = time * lookToTgt_TimeFraction
        returnToEyeCenterTime = time - lookToTgtTime - 0.5
        origin = Point3(0, 0, 0)
        blendType = 'easeOut'
        self.lookAtTrack = Parallel(
            Sequence(LerpPosInterval(self.__lpupil, lookToTgtTime, endLpupil, blendType=blendType), Wait(0.5),
                     LerpPosInterval(self.__lpupil, returnToEyeCenterTime, origin, blendType=blendType)),
            Sequence(LerpPosInterval(self.__rpupil, lookToTgtTime, endRpupil, blendType=blendType), Wait(0.5),
                     LerpPosInterval(self.__rpupil, returnToEyeCenterTime, origin, blendType=blendType)),
            name=self.__stareAtName)
        for lodName in self.getLODNames():
            head = self.getPart('head', lodName)
            self.lookAtTrack.append(LerpHprInterval(head, time, endHpr, blendType='easeInOut'))

        self.lookAtTrack.start()'''
        return 1

    def trackAnimToSpeed(self, task):
        speed, rotSpeed, slideSpeed = self.controlManager.getSpeeds()
        if speed != 0.0 or rotSpeed != 0.0 or inputState.isSet('jump'):
            if not self.movingFlag:
                self.movingFlag = 1
        elif self.movingFlag:
            self.movingFlag = 0
            self.startLookAround()
        if self.movingFlag or self.hp <= 0:
            self.wakeUp()
        elif not self.sleepFlag:
            now = globalClock.getFrameTime()
            if now - self.lastMoved > self.sleepTimeout:
                self.gotoSleep()
        state = None
        if self.sleepFlag:
            state = 'Sleep'
        elif self.hp > 0:
            state = 'Happy'
        else:
            state = 'Sad'
        if state != self.lastState:
            self.lastState = state
            self.b_setAnimState(state, self.animMultiplier)
            if state == 'Sad':
                self.setWalkSpeedSlow()
            else:
                self.setWalkSpeedNormal()
        if self.cheesyEffect == Globals.CEFlatProfile or self.cheesyEffect == Globals.CEFlatPortrait:
            needH = None
            if rotSpeed > 0.0:
                needH = -10
            elif rotSpeed < 0.0:
                needH = 10
            elif speed != 0.0:
                needH = 0
            if needH != None and self.lastNeedH != needH:
                node = self.getGeomNode().getChild(0)
                lerp = Sequence(LerpHprInterval(node, 0.5, Vec3(needH, 0, 0), blendType='easeInOut'),
                                name='cheesy-lerp-hpr', autoPause=1)
                lerp.start()
                self.lastNeedH = needH
        else:
            self.lastNeedH = None
        action = self.setSpeed(speed, rotSpeed)
        if action != self.lastAction:
            self.lastAction = action
            if self.emoteTrack:
                self.emoteTrack.finish()
                self.emoteTrack = None
            if action == Globals.WALK_INDEX or action == Globals.REVERSE_INDEX:
                self.walkSound()
            elif action == Globals.RUN_INDEX:
                self.runSound()
            else:
                self.stopSound()
        return Task.cont

    def wakeUp(self):
        if self.sleepCallback != None:
            taskMgr.remove('sleepwatch')
            self.startSleepWatch(self.sleepCallback)
        self.lastMoved = globalClock.getFrameTime()
        if self.sleepFlag:
            self.sleepFlag = 0
        return

    def hasTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        return taskMgr.hasTaskNamed(taskName)

    def enableAvatarControls(self):
        if self.avatarControlsEnabled:
            return
        self.avatarControlsEnabled = 1
        self.setupAnimationEvents()
        self.controlManager.enable()

    def disableAvatarControls(self):
        if not self.avatarControlsEnabled:
            return
        self.avatarControlsEnabled = 0
        self.ignoreAnimationEvents()
        self.controlManager.disable()

    def setupAnimationEvents(self):
        self.accept('jumpStart', self.jumpStart, [])
        self.accept('jumpHardLand', self.jumpHardLand, [])
        self.accept('jumpLand', self.jumpLand, [])

    def ignoreAnimationEvents(self):
        self.ignore('jumpStart')
        self.ignore('jumpHardLand')
        self.ignore('jumpLand')

    def stopJumpLandTask(self):
        if self.jumpLandAnimFixTask:
            self.jumpLandAnimFixTask.remove()
            self.jumpLandAnimFixTask = None
        return

    def jumpStart(self):
        if not self.sleepFlag and self.hp > 0:
            self.b_setAnimState('jumpAirborne', 1.0)
            self.stopJumpLandTask()

    def returnToWalk(self, task):
        if self.sleepFlag:
            state = 'Sleep'
        elif self.hp > 0:
            state = 'Happy'
        else:
            state = 'Sad'
        self.b_setAnimState(state, 1.0)
        return Task.done

    def runSound(self):
        self.soundWalk.stop()
        base.playSfx(self.soundRun, looping=1)

    def walkSound(self):
        self.soundRun.stop()
        base.playSfx(self.soundWalk, looping=1)

    def stopSound(self):
        self.soundRun.stop()
        self.soundWalk.stop()

    if 1:
        def jumpLandAnimFix(self, jumpTime):
            if self.playingAnim != 'run' and self.playingAnim != 'walk':
                return taskMgr.doMethodLater(jumpTime, self.returnToWalk, 'walkReturnTask')

        def jumpHardLand(self):
            if self.allowHardLand():
                self.b_setAnimState('jumpLand', 1.0)
                self.stopJumpLandTask()
                self.jumpLandAnimFixTask = self.jumpLandAnimFix(1.0)
            '''if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()'''

        def jumpLand(self):
            self.jumpLandAnimFixTask = self.jumpLandAnimFix(0.01)
            '''if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()'''

    def allowHardLand(self):
        return not self.sleepFlag and self.hp > 0

    def startRunWatch(self):

        def setRun(ignored):
            messenger.send('running-on')
        taskMgr.doMethodLater(self.runTimeout, setRun, 'runWatch')
        return Task.cont

    def stopRunWatch(self):
        taskMgr.remove('runWatch')
        messenger.send('running-off')
        return Task.cont

    def b_setAnimState(self, animName, animMultiplier=1.0, callback=None, extraArgs=[]):
        self.d_setAnimState(animName, animMultiplier, None, extraArgs)
        self.setAnimState(animName, animMultiplier, None, None, callback, extraArgs)
        return

    def d_setAnimState(self, animName, animMultiplier=1.0, timestamp=None, extraArgs=[]):
        timestamp = globalClockDelta.getFrameNetworkTime()
        #self.sendUpdate('setAnimState', [animName, animMultiplier, timestamp])

    def setAnimState(self, animName, animMultiplier=1.0, timestamp=None, animType=None, callback=None, extraArgs=[]):
        if not animName or animName == 'None':
            return
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        if base.config.GetBool('check-invalid-anims', True):
            if animMultiplier > 1.0 and animName in ['neutral']:
                animMultiplier = 1.0
        if self.animFSM.getStateNamed(animName):
            self.animFSM.request(animName, [animMultiplier,
                                            ts,
                                            callback,
                                            extraArgs])
        return

    #-----------------------------------CAMERA STUFF--------------------------------------------------------------------

    def initializeSmartCamera(self):
        self.fov = 52.0
        self.cTrav = CollisionTraverser('base.cTrav')
        base.pushCTrav(self.cTrav)
        self.cTrav.setRespectPrevTransform(1)
        self.isPageUp = 0
        self.isPageDown = 0
        self.__idealCameraObstructed = 0
        self.closestObstructionDistance = 0.0
        self.cameraIndex = 0
        self.auxCameraPositions = []
        self.cameraZOffset = 0.0
        self.__onLevelGround = 0
        self.__camCollCanMove = 0
        self.__geom = render
        self.__disableSmartCam = 0
        self.initializeSmartCameraCollisions()
        self._smartCamEnabled = False
        self.startUpdateSmartCamera()

    def initializeSmartCameraCollisions(self):
        self.ccTrav = CollisionTraverser('LocalAvatar.ccTrav')
        self.ccLine = CollisionSegment(0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        self.ccLineNode = CollisionNode('ccLineNode')
        self.ccLineNode.addSolid(self.ccLine)
        self.ccLineNodePath = self.attachNewNode(self.ccLineNode)
        self.ccLineBitMask = BitMask32(4)
        self.ccLineNode.setFromCollideMask(self.ccLineBitMask)
        self.ccLineNode.setIntoCollideMask(BitMask32.allOff())
        self.camCollisionQueue = CollisionHandlerQueue()
        self.ccTrav.addCollider(self.ccLineNodePath, self.camCollisionQueue)
        self.ccSphere = CollisionSphere(0, 0, 0, 1)
        self.ccSphereNode = CollisionNode('ccSphereNode')
        self.ccSphereNode.addSolid(self.ccSphere)
        self.ccSphereNodePath = base.camera.attachNewNode(self.ccSphereNode)
        self.ccSphereNode.setFromCollideMask(BitMask32(4))
        self.ccSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.camPusher = CollisionHandlerPusher()
        self.camPusher.addCollider(self.ccSphereNodePath, base.camera)
        self.camPusher.setCenter(self)
        self.ccPusherTrav = CollisionTraverser('LocalAvatar.ccPusherTrav')
        self.ccSphere2 = self.ccSphere
        self.ccSphereNode2 = CollisionNode('ccSphereNode2')
        self.ccSphereNode2.addSolid(self.ccSphere2)
        self.ccSphereNodePath2 = base.camera.attachNewNode(self.ccSphereNode2)
        self.ccSphereNode2.setFromCollideMask(BitMask32(4))
        self.ccSphereNode2.setIntoCollideMask(BitMask32.allOff())
        self.camPusher2 = CollisionHandlerPusher()
        self.ccPusherTrav.addCollider(self.ccSphereNodePath2, self.camPusher2)
        self.camPusher2.addCollider(self.ccSphereNodePath2, base.camera)
        self.camPusher2.setCenter(self)
        self.camFloorRayNode = self.attachNewNode('camFloorRayNode')
        self.ccRay = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRayNode = CollisionNode('ccRayNode')
        self.ccRayNode.addSolid(self.ccRay)
        self.ccRayNodePath = self.camFloorRayNode.attachNewNode(self.ccRayNode)
        self.ccRayBitMask = BitMask32(2)
        self.ccRayNode.setFromCollideMask(self.ccRayBitMask)
        self.ccRayNode.setIntoCollideMask(BitMask32.allOff())
        self.ccTravFloor = CollisionTraverser('LocalAvatar.ccTravFloor')
        self.camFloorCollisionQueue = CollisionHandlerQueue()
        self.ccTravFloor.addCollider(self.ccRayNodePath, self.camFloorCollisionQueue)
        self.ccTravOnFloor = CollisionTraverser('LocalAvatar.ccTravOnFloor')
        self.ccRay2 = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRay2Node = CollisionNode('ccRay2Node')
        self.ccRay2Node.addSolid(self.ccRay2)
        self.ccRay2NodePath = self.camFloorRayNode.attachNewNode(self.ccRay2Node)
        self.ccRay2BitMask = BitMask32(2)
        self.ccRay2Node.setFromCollideMask(self.ccRay2BitMask)
        self.ccRay2Node.setIntoCollideMask(BitMask32.allOff())
        self.ccRay2MoveNodePath = hidden.attachNewNode('ccRay2MoveNode')
        self.camFloorCollisionBroadcaster = CollisionHandlerFloor()
        self.camFloorCollisionBroadcaster.setInPattern('on-floor')
        self.camFloorCollisionBroadcaster.setOutPattern('off-floor')
        self.camFloorCollisionBroadcaster.addCollider(self.ccRay2NodePath, self.ccRay2MoveNodePath)

    def getHeight(self):
        return self.height

    def getClampedAvatarHeight(self):
        return max(self.getHeight(), 3.0)

    def initCameraPositions(self):
        camHeight = self.getClampedAvatarHeight()
        heightScaleFactor = camHeight * 0.3333333333
        defLookAt = Point3(0.0, 1.5, camHeight)
        scXoffset = 3.0
        scPosition = (Point3(scXoffset - 1, -10.0, camHeight + 5.0), Point3(scXoffset, 2.0, camHeight))
        self.cameraPositions = [(Point3(0.0, -9.0 * heightScaleFactor, camHeight),
                                 defLookAt,
                                 Point3(0.0, camHeight, camHeight * 4.0),
                                 Point3(0.0, camHeight, camHeight * -1.0),
                                 0),
                                (Point3(0.0, 0.7, camHeight),
                                 defLookAt,
                                 Point3(0.0, camHeight, camHeight * 1.33),
                                 Point3(0.0, camHeight, camHeight * 0.66),
                                 1),
                                (Point3(5.7 * heightScaleFactor, 7.65 * heightScaleFactor, camHeight + 2.0),
                                 Point3(0.0, 1.0, camHeight),
                                 Point3(0.0, 1.0, camHeight * 4.0),
                                 Point3(0.0, 1.0, camHeight * -1.0),
                                 0),
                                (Point3(0.0, 8.65 * heightScaleFactor, camHeight),
                                 Point3(0.0, 1.0, camHeight),
                                 Point3(0.0, 1.0, camHeight * 4.0),
                                 Point3(0.0, 1.0, camHeight * -1.0),
                                 0),
                                (Point3(-camHeight * 3, 0.0, camHeight),
                                 Point3(0.0, 0.0, camHeight),
                                 Point3(0.0, camHeight, camHeight * 1.1),
                                 Point3(0.0, camHeight, camHeight * 0.9),
                                 1),
                                (Point3(camHeight * 3, 0.0, camHeight),
                                 Point3(0.0, 0.0, camHeight),
                                 Point3(0.0, camHeight, camHeight * 1.1),
                                 Point3(0.0, camHeight, camHeight * 0.9),
                                 1),
                                (Point3(0.0, -24.0 * heightScaleFactor, camHeight + 4.0),
                                 defLookAt,
                                 Point3(0.0, 1.5, camHeight * 4.0),
                                 Point3(0.0, 1.5, camHeight * -1.0),
                                 0),
                                (Point3(0.0, -12.0 * heightScaleFactor, camHeight + 4.0),
                                 defLookAt,
                                 Point3(0.0, 1.5, camHeight * 4.0),
                                 Point3(0.0, 1.5, camHeight * -1.0),
                                 0)] + self.auxCameraPositions

    def setCameraPositionByIndex(self, index):
        self.setCameraSettings(self.cameraPositions[index])

    def setIdealCameraPos(self, pos):
        self.__idealCameraPos = Point3(pos)
        self.updateSmartCameraCollisionLineSegment()

    def getIdealCameraPos(self):
        return Point3(self.__idealCameraPos)

    def getVisibilityPoint(self):
        return Point3(0.0, 0.0, self.getHeight())

    def putCameraFloorRayOnAvatar(self):
        self.camFloorRayNode.setPos(self, 0, 0, 5)

    def updateSmartCameraCollisionLineSegment(self):
        pointB = self.getIdealCameraPos()
        pointA = self.getVisibilityPoint()
        vectorAB = Vec3(pointB - pointA)
        lengthAB = vectorAB.length()
        if lengthAB > 0.001:
            self.ccLine.setPointA(pointA)
            self.ccLine.setPointB(pointB)

    def setCameraSettings(self, camSettings):
        self.setIdealCameraPos(camSettings[0])
        if self.isPageUp and self.isPageDown or not self.isPageUp and not self.isPageDown:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[1])
        elif self.isPageUp:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[2])
        elif self.isPageDown:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[3])
        else:
            pass
        self.__disableSmartCam = camSettings[4]
        if self.__disableSmartCam:
            self.putCameraFloorRayOnAvatar()
            self.cameraZOffset = 0.0

    def startUpdateSmartCamera(self, push=1):
        if self._smartCamEnabled:
            return
        self._smartCamEnabled = True
        self.__floorDetected = 0
        self.__cameraHasBeenMoved = 0
        self.recalcCameraSphere()
        self.initCameraPositions()
        self.setCameraPositionByIndex(self.cameraIndex)
        self.posCamera(0, 0.0)
        self.__instantaneousCamPos = camera.getPos()
        if push:
            self.cTrav.addCollider(self.ccSphereNodePath, self.camPusher)
            self.ccTravOnFloor.addCollider(self.ccRay2NodePath, self.camFloorCollisionBroadcaster)
            self.__disableSmartCam = 0
        else:
            self.__disableSmartCam = 1
        self.__lastPosWrtRender = camera.getPos(render)
        self.__lastHprWrtRender = camera.getHpr(render)
        taskName = 'updateSmartCamera'
        taskMgr.remove(taskName)
        taskMgr.add(self.updateSmartCamera, taskName, priority=47)
        self.enableSmartCameraViews()

    def enableSmartCameraViews(self):
        self.accept('tab', self.nextCameraPos, [1])
        self.accept('shift-tab', self.nextCameraPos, [0])
        self.accept('page_up', self.pageUp)
        self.accept('page_down', self.pageDown)

    def positionCameraWithPusher(self, pos, lookAt):
        camera.setPos(pos)
        self.ccPusherTrav.traverse(self.__geom)
        camera.lookAt(lookAt)

    def lerpCameraFov(self, fov, time):
        taskMgr.remove('cam-fov-lerp-play')
        oldFov = base.camLens.getHfov()
        if abs(fov - oldFov) > 0.1:
            def setCamFov(fov):
                base.camLens.setMinFov(fov / (4. / 3.))

            self.camLerpInterval = LerpFunctionInterval(setCamFov, fromData=oldFov, toData=fov, duration=time,
                                                        name='cam-fov-lerp')
            self.camLerpInterval.start()

    def pageUp(self):
        if not self.avatarControlsEnabled:
            return
        self.wakeUp()
        if not self.isPageUp:
            self.isPageDown = 0
            self.isPageUp = 1
            self.lerpCameraFov(70, 0.6)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    def pageDown(self):
        if not self.avatarControlsEnabled:
            return
        self.wakeUp()
        if not self.isPageDown:
            self.isPageUp = 0
            self.isPageDown = 1
            self.lerpCameraFov(70, 0.6)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    def clearPageUpDown(self):
        if self.isPageDown or self.isPageUp:
            self.lerpCameraFov(self.fov, 0.6)
            self.isPageDown = 0
            self.isPageUp = 0
            self.setCameraPositionByIndex(self.cameraIndex)

    def nextCameraPos(self, forward):
        if not self.avatarControlsEnabled:
            return
        self.wakeUp()
        self.__cameraHasBeenMoved = 1
        if forward:
            self.cameraIndex += 1
            if self.cameraIndex > len(self.cameraPositions) - 1:
                self.cameraIndex = 0
        else:
            self.cameraIndex -= 1
            if self.cameraIndex < 0:
                self.cameraIndex = len(self.cameraPositions) - 1
        self.setCameraPositionByIndex(self.cameraIndex)

    def getCompromiseCameraPos(self):
        if self.__idealCameraObstructed == 0:
            compromisePos = self.getIdealCameraPos()
        else:
            visPnt = self.getVisibilityPoint()
            idealPos = self.getIdealCameraPos()
            distance = Vec3(idealPos - visPnt).length()
            ratio = self.closestObstructionDistance / distance
            compromisePos = idealPos * ratio + visPnt * (1 - ratio)
            liftMult = 1.0 - ratio * ratio
            compromisePos = Point3(compromisePos[0], compromisePos[1],
                                   compromisePos[2] + self.getHeight() * 0.4 * liftMult)
        compromisePos.setZ(compromisePos[2] + self.cameraZOffset)
        return compromisePos

    def updateSmartCamera(self, task):
        if not self.__camCollCanMove and not self.__cameraHasBeenMoved:
            if self.__lastPosWrtRender == camera.getPos(render):
                if self.__lastHprWrtRender == camera.getHpr(render):
                    return Task.cont
        self.__cameraHasBeenMoved = 0
        self.__lastPosWrtRender = camera.getPos(render)
        self.__lastHprWrtRender = camera.getHpr(render)
        self.__idealCameraObstructed = 0
        if not self.__disableSmartCam:
            self.ccTrav.traverse(self.__geom)
            if self.camCollisionQueue.getNumEntries() > 0:
                try:
                    self.camCollisionQueue.sortEntries()
                    self.handleCameraObstruction(self.camCollisionQueue.getEntry(0))
                except AssertionError:
                    pass
            if not self.__onLevelGround:
                self.handleCameraFloorInteraction()
        if not self.__idealCameraObstructed:
            self.nudgeCamera()
        if not self.__disableSmartCam:
            self.ccPusherTrav.traverse(self.__geom)
            self.putCameraFloorRayOnCamera()
        self.ccTravOnFloor.traverse(self.__geom)
        return Task.cont

    def handleCameraObstruction(self, camObstrCollisionEntry):
        collisionPoint = camObstrCollisionEntry.getSurfacePoint(self.ccLineNodePath)
        collisionVec = Vec3(collisionPoint - self.ccLine.getPointA())
        distance = collisionVec.length()
        self.__idealCameraObstructed = 1
        self.closestObstructionDistance = distance
        self.popCameraToDest()

    def nudgeCamera(self):
        CLOSE_ENOUGH = 0.1
        curCamPos = self.__instantaneousCamPos
        curCamHpr = camera.getHpr()
        targetCamPos = self.getCompromiseCameraPos()
        targetCamLookAt = self.getLookAtPoint()
        posDone = 0
        if Vec3(curCamPos - targetCamPos).length() <= CLOSE_ENOUGH:
            camera.setPos(targetCamPos)
            posDone = 1
        camera.setPos(targetCamPos)
        camera.lookAt(targetCamLookAt)
        targetCamHpr = camera.getHpr()
        hprDone = 0
        if Vec3(curCamHpr - targetCamHpr).length() <= CLOSE_ENOUGH:
            hprDone = 1
        if posDone and hprDone:
            return
        lerpRatio = 0.15
        lerpRatio = 1 - pow(1 - lerpRatio, globalClock.getDt() * 30.0)
        self.__instantaneousCamPos = targetCamPos * lerpRatio + curCamPos * (1 - lerpRatio)
        if self.__disableSmartCam or not self.__idealCameraObstructed:
            newHpr = targetCamHpr * lerpRatio + curCamHpr * (1 - lerpRatio)
        else:
            newHpr = targetCamHpr
        camera.setPos(self.__instantaneousCamPos)
        camera.setHpr(newHpr)

    def putCameraFloorRayOnCamera(self):
        self.camFloorRayNode.setPos(self.ccSphereNodePath, 0, 0, 0)

    def handleCameraFloorInteraction(self):
        self.putCameraFloorRayOnCamera()
        self.ccTravFloor.traverse(self.__geom)
        if self.__onLevelGround:
            return
        if self.camFloorCollisionQueue.getNumEntries() == 0:
            return
        self.camFloorCollisionQueue.sortEntries()
        camObstrCollisionEntry = self.camFloorCollisionQueue.getEntry(0)
        camHeightFromFloor = camObstrCollisionEntry.getSurfacePoint(self.ccRayNodePath)[2]
        self.cameraZOffset = camera.getPos()[2] + camHeightFromFloor
        if self.cameraZOffset < 0:
            self.cameraZOffset = 0
        if self.__floorDetected == 0:
            self.__floorDetected = 1
            self.popCameraToDest()

    def popCameraToDest(self):
        newCamPos = self.getCompromiseCameraPos()
        newCamLookAt = self.getLookAtPoint()
        self.positionCameraWithPusher(newCamPos, newCamLookAt)
        self.__instantaneousCamPos = camera.getPos()

    def posCamera(self, lerp, time):
        if not lerp:
            self.positionCameraWithPusher(self.getCompromiseCameraPos(), self.getLookAtPoint())
        else:
            camPos = self.getCompromiseCameraPos()
            savePos = camera.getPos()
            saveHpr = camera.getHpr()
            self.positionCameraWithPusher(camPos, self.getLookAtPoint())
            x = camPos[0]
            y = camPos[1]
            z = camPos[2]
            destHpr = camera.getHpr()
            h = destHpr[0]
            p = destHpr[1]
            r = destHpr[2]
            camera.setPos(savePos)
            camera.setHpr(saveHpr)
            taskMgr.remove('posCamera')
            camera.lerpPosHpr(x, y, z, h, p, r, time, task='posCamera')

    def setLookAtPoint(self, la):
        self.__curLookAt = Point3(la)

    def getLookAtPoint(self):
        return Point3(self.__curLookAt)

    def recalcCameraSphere(self):
        nearPlaneDist = base.camLens.getNear()
        hFov = base.camLens.getHfov()
        vFov = base.camLens.getVfov()
        hOff = nearPlaneDist * math.tan(deg2Rad(hFov / 2.0))
        vOff = nearPlaneDist * math.tan(deg2Rad(vFov / 2.0))
        camPnts = [Point3(hOff, nearPlaneDist, vOff),
                   Point3(-hOff, nearPlaneDist, vOff),
                   Point3(hOff, nearPlaneDist, -vOff),
                   Point3(-hOff, nearPlaneDist, -vOff),
                   Point3(0.0, 0.0, 0.0)]
        avgPnt = Point3(0.0, 0.0, 0.0)
        for camPnt in camPnts:
            avgPnt = avgPnt + camPnt

        avgPnt = avgPnt / len(camPnts)
        sphereRadius = 0.0
        for camPnt in camPnts:
            dist = Vec3(camPnt - avgPnt).length()
            if dist > sphereRadius:
                sphereRadius = dist

        avgPnt = Point3(avgPnt)
        self.ccSphereNodePath.setPos(avgPnt)
        self.ccSphereNodePath2.setPos(avgPnt)
        self.ccSphere.setRadius(sphereRadius)