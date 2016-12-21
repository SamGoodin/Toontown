import random
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.actor.Actor import Actor
from toon.ShadowCaster import ShadowCaster
from direct.distributed import DistributedSmoothNode
from direct.controls import ControlManager
from direct.controls.GhostWalker import GhostWalker
from direct.controls.GravityWalker import GravityWalker
from direct.controls.ObserverWalker import ObserverWalker
from direct.controls.SwimWalker import SwimWalker
from direct.controls.TwoDWalker import TwoDWalker
from direct.task import Task
from panda3d.core import *
from direct.distributed.ClockDelta import *
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State

import Globals



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

LegsAnimDict =  {'dgl': {'neutral': "phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral"},
                 'dgm': {'neutral': "phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral"},
                 'dgs': {'neutral': "phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral"}}
TorsoAnimDict = {'dgl': {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral"},
                 'dgm': {"neutral": "phase_3/models/char/tt_a_chr_dgm_shorts_head_neutral"},
                 'dgs': {"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_head_neutral"}}
HeadAnimDict =  {'dgl': {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral"},
                 'dgm': {"neutral": "phase_3/models/char/tt_a_chr_dgm_shorts_head_neutral"},
                 'dgs': {"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_head_neutral"}}
animList = (('neutral', 'neutral'), ('run', 'run'))


class Toon(Actor):
    sleepTimeout = base.config.GetInt('sleep-timeout', 120)


    def __init__(self):
        print 'work'
        Actor.__init__(self, None, None, other=None, flattenable=0, setFinal=1)
        #DistributedSmoothNode.DistributedSmoothNode.__init__(self, None)
        self.controlManager = ControlManager.ControlManager(True, False)
        self.head = None
        self.legs = None
        self.torso = None
        self.forceJumpIdle = False
        self.toon = None
        self.sleepCallback = None
        self.animalType = None
        self.headColor = None
        self.torsoColor = None
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
        self.animFSM = ClassicFSM('Toon', [State('off', self.enterOff, self.exitOff),
                                           State('neutral', self.enterNeutral, self.exitNeutral),
                                           State('run', self.enterRun, self.exitRun),
                                           State('jump', self.enterJump, self.exitJump),
                                           State('jumpAirborne', self.enterJumpAirborne, self.exitJumpAirborne),
                                           State('Happy', self.enterHappy, self.exitHappy)
                                           ],
                                  'off', 'off')
        animStateList = self.animFSM.getStates()
        self.animFSM.enterInitialState()
        self.cheesyEffect = None
        self.standWalkRunReverse = None
        self.accept('arrow_up', self.enterRun)

    def enterNeutral(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * self.randGen.random()))
        self.loop(anim, restart=0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim
        self.setActiveShadow(1)

    def exitNeutral(self):
        self.stop()

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
        #self.motion.exit()
        return

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
            #self.motion.enter()
            #self.motion.setState(anim, rate)
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
        #self.setActiveShadow(0)
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

    def createOther(self, head, torso, torsoName, legs, legsName, headName=None):
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 20)
        levelOneOut = base.config.GetInt('lod1-out', 0)
        levelTwoIn = base.config.GetInt('lod2-in', 80)
        levelTwoOut = base.config.GetInt('lod2-out', 20)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 80)
        self.addLOD(1000, levelOneIn, levelOneOut)
        #self.addLOD(500, levelTwoIn, levelTwoOut)
        #self.addLOD(250, levelThreeIn, levelThreeOut)
        self.loadModel(head, 'head', '1000', True)
        self.loadModel(torso, 'torso', '1000', True)
        self.loadModel(legs, 'legs', '1000', True)
        self.showPart('head', '1000')
        self.showPart('torso', '1000')
        self.showPart('legs', '1000')
        self.loadAnims(LegsAnimDict[legsName], 'legs', '1000')
        self.loadAnims(TorsoAnimDict[torsoName], 'torso', '1000')
        if headName:
            self.loadAnims(HeadAnimDict[headName], 'head', '1000')
        self.findAllMatches('**/boots_short').stash()
        self.findAllMatches('**/boots_long').stash()
        self.findAllMatches('**/shoes').stash()
        '''
        toon = Actor(

            {"head": head,
             "torso": "phase_3/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_1000",
             "legs": legs},

            {"torso": {"neutral": "phase_3/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_neutral",
                       "run": "phase_3/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_run",
                       "walk": "phase_3.5/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_walk",
                       "running-jump-idle": "phase_3.5/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_leap_zhang",
                       "jump-idle": "phase_3.5/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_jump-zhang",
                       "book": "phase_3.5/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_book"},
             "legs": {"neutral": "phase_3/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_neutral",
                      "run": "phase_3/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_run",
                      "walk": "phase_3.5/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_walk",
                      "running-jump-idle": "phase_3.5/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_leap_zhang",
                      "jump-idle": "phase_3.5/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_jump-zhang",
                      "book": "phase_3.5/models/char/tt_a_chr_" + legsName + "_" + gender + "_legs_book"}
             }
        )
        return toon'''

    def createToon(self, headName, torso, legs):
        print headName, torso, legs
        legsName = legs
        torsoName = torso
        legs = loader.loadModel("phase_3/models/char/tt_a_chr_" + legs + "_shorts_legs_1000")
        otherParts = legs.findAllMatches('**/boots*') + legs.findAllMatches('**/shoes')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        torsoModel = loader.loadModel("phase_3/models/char/tt_a_chr_" + torso + "_shorts_torso_1000")
        if headName == "dgl" or headName == "dgm" or headName == "dgs":
            head = "phase_3/models/char/tt_a_chr_" + headName + "_shorts_head_1000"
            self.createOther(head, torsoModel, torsoName, legs, legsName, headName)
        else:
            head = "phase_3/models/char/" + headName + "-heads-1000"
            '''otherParts = head.findAllMatches('**/*long*')
            for partNum in range(0, otherParts.getNumPaths()):
                otherParts.getPath(partNum).removeNode()
            ntrlMuzzle = head.find('**/*muzzle*neutral')
            otherParts = head.findAllMatches('**/*muzzle*')
            for partNum in range(0, otherParts.getNumPaths()):
                part = otherParts.getPath(partNum)
                if part != ntrlMuzzle:
                    otherParts.getPath(partNum).removeNode()'''
            self.createOther(head, torsoModel, torsoName, legs, legsName)
        self.attach("head", "torso", "def_head")
        self.attach("torso", "legs", "joint_hips")
        return self

    def createRandomBoy(self):
        choice = random.choice(['dog', 'cat', 'horse', 'monkey', 'rabbit', 'mouse', 'duck', 'bear', 'pig'])
        self.animalType = choice
        self.bodyType = random.choice(['dgl', 'dgm', 'dgs'])
        self.legsType = random.choice(['dgl', 'dgm', 'dgs'])
        if choice is not 'dog':
            self.createToon(choice, self.bodyType, self.legsType)
        else:
            self.dogHead = random.choice(["dgl", "dgm", "dgs"])
            self.createToon(self.dogHead, self.bodyType, self.legsType)
        self.setRandomColor()
        self.generateRandomClothing()
        self.rescaleToon()

    def getDogHead(self):
        return self.dogHead

    def getToon(self):
        return self

    def getAnimalType(self):
        return self.animalType

    def getBodyType(self):
        return self.bodyType

    def getLegsType(self):
        return self.legsType

    def setRandomColor(self):
        self.setRandomHeadColor(self.animalType)
        self.setRandomTorsoColor()
        self.setRandomLegsColor()

    def getHeadColor(self):
        parts = self.find('**/head*')
        return parts.getColor()

    def setRandomHeadColor(self, animalType):
        self.headColor = random.choice(allColorsList)
        parts = self.findAllMatches('**/head*')
        parts.setColor(self.headColor)
        if animalType == 'cat' or animalType == 'rabbit' or animalType == 'bear' or \
                        animalType == 'mouse' or animalType == 'pig':
            parts = self.findAllMatches('**/ear?-*')
            parts.setColor(self.headColor)

    def setHeadColor(self, animalType, color):
        parts = self.findAllMatches('**/head*')
        parts.setColor(color)
        if animalType == 'cat' or animalType == 'rabbit' or animalType == 'bear' or \
                        animalType == 'mouse' or animalType == 'pig':
            parts = self.findAllMatches('**/ear?-*')
            parts.setColor(color)

    def getTorsoColor(self):
        return self.torsoColor

    def setRandomTorsoColor(self):
        torso = self.getPart('torso')
        self.torsoColor = random.choice(allColorsList)
        for pieceName in ('arms', 'neck'):
            piece = torso.find('**/' + pieceName)
            piece.setColor(self.torsoColor)
        hands = torso.find('**/hands')
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
            piece = legs.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)

    def setLegsColor(self, color):
        legs = self.getPart('legs')
        self.legColor = color
        for pieceName in ('legs', 'feet'):
            piece = legs.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)

    def generateRandomClothing(self):
        torso = self.getPart('torso')
        shirt = torso.findAllMatches('**/torso-top')
        sleeves = torso.findAllMatches('**/sleeves')
        bottom = torso.findAllMatches('**/torso-bot')
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

    def setShirt(self, shirt1):
        torso = self.getPart('torso')
        shirt = torso.findAllMatches('**/torso-top')
        sleeves = torso.findAllMatches('**/sleeves')
        self.shirtChoice = shirt1
        shirtTexture = loader.loadTexture(Shirts[self.shirtChoice])
        sleeveTexture = loader.loadTexture(Shirts[self.shirtChoice])
        shirt.setTexture(shirtTexture, 1)
        sleeves.setTexture(sleeveTexture, 1)

    def setShorts(self, shorts):
        torso = self.getPart('torso')
        bottom = torso.findAllMatches('**/torso-bot')
        self.shortsChoice = shorts
        bottomTexture = loader.loadTexture(BoyShorts[self.shortsChoice])
        bottom.setTexture(bottomTexture, 1)

    def rescaleToon(self):
        bodyScale = Globals.toonBodyScales[self.animalType]
        headScale = Globals.toonHeadScales[self.animalType]
        self.getGeomNode().setScale(bodyScale * 1.34)
        self.getPart('head').setScale(headScale)
        if self.legsType == 'dgl':
            self.getPart('legs').setScale(.9)

    def getAirborneHeight(self):
        height = self.getPos(self.shadowPlacer.shadowNodePath)
        return height.getZ() + 0.025

    def setupControls(self, avatarRadius = 1.4, floorOffset = Globals.FloorOffset, reach = 4.0,
                      wallBitmask = Globals.WallBitmask, floorBitmask = Globals.FloorBitmask,
                      ghostBitmask = Globals.GhostBitmask):
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

    def setupAnimationEvents(self):
        self.accept('jumpStart', self.jumpStart, [])
        self.accept('jumpHardLand', self.jumpHardLand, [])
        self.accept('jumpLand', self.jumpLand, [])

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
                return taskMgr.doMethodLater(jumpTime, self.returnToWalk, self.uniqueName('walkReturnTask'))

        def jumpHardLand(self):
            if self.allowHardLand():
                self.b_setAnimState('jumpLand', 1.0)
                self.stopJumpLandTask()
                self.jumpLandAnimFixTask = self.jumpLandAnimFix(1.0)
            if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()

        def jumpLand(self):
            self.jumpLandAnimFixTask = self.jumpLandAnimFix(0.01)
            if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()

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

    def setupCameraPositions(self):
        camHeight = max(2.0, 3.0)
        defLookAt = Point3(0.0, 1.5, 0)
        self.cameraPositions = (Point3(0.0, -10.0, camHeight - .5))
        base.camera.setPos(Point3(self.cameraPositions))
        base.camera.setHpr(defLookAt)

    def getToonStuff(self):
        onScreenDebug.enabled = True
        base.taskMgr.add(self.updateOnScreenDebug, 'UpdateOSD')

    def updateOnScreenDebug(self, task):
        onScreenDebug.add('Avatar Pos', self.getPos())
        onScreenDebug.add('Avatar HPR', self.getHpr())

        return Task.cont

    def startLookAround(self):
        taskMgr.remove(self.__lookName)
        t = random.Random().random() * 5.0 + 2.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)

    def __lookAround(self, task):
        #self.findSomethingToLookAt()
        t = random.Random().random() * 4.0 + 3.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)
        return Task.done

    def stopLookAround(self):
        taskMgr.remove(self.__lookName)
        self.stopStareAt()

