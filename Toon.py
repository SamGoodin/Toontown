from direct.actor.Actor import Actor
import random
from pandac.PandaModules import *
import Globals
from panda3d.core import *
from direct.controls.GravityWalker import GravityWalker
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.task import Task


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

LoadedAnims = {}

LegDict = {'s': '/models/char/tt_a_chr_dgs_shorts_legs_',
           'm': '/models/char/tt_a_chr_dgm_shorts_legs_',
           'l': '/models/char/tt_a_chr_dgl_shorts_legs_'}

LegsAnimDict = {}
animList = (('neutral', 'neutral'), ('run', 'run'))


class Toon(Actor):

    def __init__(self):
        Actor.__init__(self)
        self.head = None
        self.legs = None
        self.torso = None
        self.example = None
        self.toon = None
        self.animalType = None
        self.headColor = None
        self.torsoColor = None
        self.legColor = None
        self.accept("0", self.getToonStuff)

    def getColorList(self):
        return allColorsList

    def getShirtsList(self):
        return Shirts

    def getShortsList(self):
        return BoyShorts

    def createDog(self, head, headAnim, torso, legs, legsName, gender):
        toon = Actor(

            {"head": head,
             "torso": "phase_3/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_1000",
             "legs": legs},

            {"head": {"neutral": "phase_3/models/char/tt_a_chr_" + headAnim + "_" + gender + "_head_neutral",
                      "run": "phase_3/models/char/tt_a_chr_" + headAnim + "_" + gender + "_head_run",
                      "walk": "phase_3.5/models/char/tt_a_chr_" + headAnim + "_" + gender + "_head_walk",
                      "running-jump-idle": "phase_3.5/models/char/tt_a_chr_" + headAnim + "_" + gender + "_head_leap_zhang",
                      "jump-idle": "phase_3.5/models/char/tt_a_chr_" + headAnim + "_" + gender + "_head_jump-zhang"},
             "torso": {"neutral": "phase_3/models/char/tt_a_chr_" + torso + "_" + gender + "_torso_neutral",
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
        return toon

    def createOther(self, head, torso, legs, legsName, gender):
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
        return toon

    def createToon(self, head1, torso, legs, gender):
        self.toon = None
        legsName = legs
        legs = loader.loadModel("phase_3/models/char/tt_a_chr_" + legs + "_" + gender + "_legs_1000")
        otherParts = legs.findAllMatches('**/boots*') + legs.findAllMatches('**/shoes')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        if head1 == "dgl" or head1 == "dgm" or head1 == "dgs":
            head = "phase_3/models/char/tt_a_chr_" + head1 + "_" + gender + "_head_1000"
            self.toon = self.createDog(head, head1, torso, legs, legsName, gender)
        else:
            head = loader.loadModel("phase_3/models/char/" + head1 + "-heads-1000")
            otherParts = head.findAllMatches('**/*long*')
            for partNum in range(0, otherParts.getNumPaths()):
                otherParts.getPath(partNum).removeNode()
            ntrlMuzzle = head.find('**/*muzzle*neutral')
            otherParts = head.findAllMatches('**/*muzzle*')
            for partNum in range(0, otherParts.getNumPaths()):
                part = otherParts.getPath(partNum)
                if part != ntrlMuzzle:
                    otherParts.getPath(partNum).removeNode()
            self.toon = self.createOther(head, torso, legs, legsName, gender)

        self.toon.attach("head", "torso", "def_head")
        self.toon.attach("torso", "legs", "joint_hips")
        return self.toon

    def createRandomBoy(self):
        self.toon = None
        choice = random.choice(['dog', 'cat', 'horse', 'monkey', 'rabbit', 'mouse', 'duck', 'bear', 'pig'])
        self.animalType = choice
        self.bodyType = random.choice(['dgl', 'dgm', 'dgs'])
        self.legsType = random.choice(['dgl', 'dgm', 'dgs'])
        if choice is not 'dog':
            self.toon = self.createToon(choice, self.bodyType, self.legsType, 'shorts')
        else:
            self.dogHead = random.choice(["dgl", "dgm", "dgs"])
            self.toon = self.createToon(self.dogHead, self.bodyType, self.legsType, 'shorts')
        self.toon = self.setRandomColor(self.toon)
        self.toon = self.generateRandomClothing(self.toon)
        self.toon = self.rescaleToon(self.toon)
        return self.toon

    def getDogHead(self):
        return self.dogHead

    def getToon(self):
        return self.toon

    def getAnimalType(self):
        return self.animalType

    def getBodyType(self):
        return self.bodyType

    def getLegsType(self):
        return self.legsType

    def createExample(self):
        self.example = None
        self.example = Actor(
            {"head": "phase_3/models/char/tt_a_chr_dgl_shorts_head_1000",
             "torso": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000",
             "legs": "phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000"},

            {"head": {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral",
                      "run": "phase_3/models/char/tt_a_chr_dgl_shorts_head_run"},
             "torso": {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral",
                       "run": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_run"},
             "legs": {"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_legs_neutral",
                      "run": "phase_3/models/char/tt_a_chr_dgl_shorts_legs_run"}
             }
        )
        
        self.example.attach("head", "torso", "def_head")
        self.example.attach("torso", "legs", "joint_hips")
        return self.example

    def setRandomColor(self, toon):
        toon = self.setRandomHeadColor(toon, self.animalType)
        toon = self.setRandomTorsoColor(toon)
        toon = self.setRandomLegsColor(toon)
        return toon

    def getHeadColor(self, toon):
        parts = toon.find('**/head*')
        return parts.getColor()

    def setRandomHeadColor(self, toon, animalType):
        self.headColor = random.choice(allColorsList)
        parts = toon.findAllMatches('**/head*')
        parts.setColor(self.headColor)
        if animalType == 'cat' or animalType == 'rabbit' or animalType == 'bear' or \
                        animalType == 'mouse' or animalType == 'pig':
            parts = toon.findAllMatches('**/ear?-*')
            parts.setColor(self.headColor)
        return toon

    def setHeadColor(self, toon, animalType, color):
        parts = toon.findAllMatches('**/head*')
        parts.setColor(color)
        if animalType == 'cat' or animalType == 'rabbit' or animalType == 'bear' or \
                        animalType == 'mouse' or animalType == 'pig':
            parts = toon.findAllMatches('**/ear?-*')
            parts.setColor(color)
        return toon

    def getTorsoColor(self):
        return self.torsoColor

    def setRandomTorsoColor(self, toon):
        torso = toon.getPart('torso')
        self.torsoColor = random.choice(allColorsList)
        for pieceName in ('arms', 'neck'):
            piece = torso.find('**/' + pieceName)
            piece.setColor(self.torsoColor)
        hands = torso.find('**/hands')
        hands.setColor(1, 1, 1, 1)
        return toon

    def setTorsoColor(self, toon, color):
        torso = toon.getPart('torso')
        self.torsoColor = color
        for pieceName in ('arms', 'neck'):
            piece = torso.find('**/' + pieceName)
            piece.setColor(self.torsoColor)
        hands = torso.find('**/hands')
        hands.setColor(1, 1, 1, 1)
        return toon

    def getLegColor(self):
        return self.legColor

    def setRandomLegsColor(self, toon):
        legs = toon.getPart('legs')
        self.legColor = random.choice(allColorsList)
        for pieceName in ('legs', 'feet'):
            piece = legs.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)
        return toon

    def setLegsColor(self, toon, color):
        legs = toon.getPart('legs')
        self.legColor = color
        for pieceName in ('legs', 'feet'):
            piece = legs.find('**/%s;+s' % pieceName)
            piece.setColor(self.legColor)
        return toon

    def generateRandomClothing(self, toon):
        torso = toon.getPart('torso')
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
        return toon

    def setShirt(self, toon, shirt1):
        torso = toon.getPart('torso')
        shirt = torso.findAllMatches('**/torso-top')
        sleeves = torso.findAllMatches('**/sleeves')
        self.shirtChoice = shirt1
        shirtTexture = loader.loadTexture(Shirts[self.shirtChoice])
        sleeveTexture = loader.loadTexture(Shirts[self.shirtChoice])
        shirt.setTexture(shirtTexture, 1)
        sleeves.setTexture(sleeveTexture, 1)
        return toon

    def setShorts(self, toon, shorts):
        torso = toon.getPart('torso')
        bottom = torso.findAllMatches('**/torso-bot')
        self.shortsChoice = shorts
        bottomTexture = loader.loadTexture(BoyShorts[self.shortsChoice])
        bottom.setTexture(bottomTexture, 1)
        return toon

    def rescaleToon(self, toon):
        bodyScale = Globals.toonBodyScales[self.animalType]
        headScale = Globals.toonHeadScales[self.animalType]
        toon.getGeomNode().setScale(bodyScale * 1.34)
        toon.getPart('head').setScale(headScale)
        if self.legsType == 'dgl':
            toon.getPart('legs').setScale(.9)
        return toon

    def setupControls(self, toon):
        wallBitmask = BitMask32(1)
        floorBitmask = BitMask32(2)
        base.cTrav = CollisionTraverser()
        walkControls = GravityWalker(legacyLifter=True)
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.setWalkSpeed(48.0, 64.0, 32.0, 320.0)
        walkControls.initializeCollisions(base.cTrav, toon, floorOffset=0.025, reach=4.0)
        walkControls.setAirborneHeightFunc(3.2375 + 0.025000000000000001)
        walkControls.enableAvatarControls()
        toon.physControls = walkControls
        self.toon = toon

        self.keyMap = {'left': 0, 'right': 0, 'forward': 0, 'backward': 0, 'control': 0}

        self.setWatchKey('arrow_up', 'forward', 'forward')
        self.setWatchKey('control-arrow_up', 'forward', 'forward')
        self.setWatchKey('alt-arrow_up', 'forward', 'forward')
        self.setWatchKey('shift-arrow_up', 'forward', 'forward')
        self.setWatchKey('arrow_down', 'reverse', 'backward')
        self.setWatchKey('control-arrow_down', 'reverse', 'backward')
        self.setWatchKey('alt-arrow_down', 'reverse', 'backward')
        self.setWatchKey('shift-arrow_down', 'reverse', 'backward')
        self.setWatchKey('arrow_left', 'turnLeft', 'left')
        self.setWatchKey('control-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('alt-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('shift-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('arrow_right', 'turnRight', 'right')
        self.setWatchKey('control-arrow_right', 'turnRight', 'right')
        self.setWatchKey('alt-arrow_right', 'turnRight', 'right')
        self.setWatchKey('shift-arrow_right', 'turnRight', 'right')
        self.setWatchKey('control', 'jump', 'control')

        self.movingNeutral, self.movingForward = (False, False)
        self.movingRotation, self.movingBackward = (False, False)
        self.movingJumping = False
        base.taskMgr.add(self.handleMovement, 'controlManager')
        self.getToonStuff()
        return self.toon

    def setWatchKey(self, key, input, keyMapName):
        def watchKey(active=True):
            if active == True:
                inputState.set(input, True)
                self.keyMap[keyMapName] = 1
            else:
                inputState.set(input, False)
                self.keyMap[keyMapName] = 0

        base.accept(key, watchKey, [True])
        base.accept(key + '-up', watchKey, [False])

    def setMovementAnimation(self, loopName, toon, playRate=1.0):
        if 'jump' in loopName:
            self.movingJumping = True
            self.movingForward = False
            self.movingNeutral = False
            self.movingRotation = False
            self.movingBackward = False
        elif loopName == 'run':
            self.movingJumping = False
            self.movingForward = True
            self.movingNeutral = False
            self.movingRotation = False
            self.movingBackward = False
        elif loopName == 'walk':
            self.movingJumping = False
            self.movingForward = False
            self.movingNeutral = False
            if playRate == -1.0:
                self.movingBackward = True
                self.movingRotation = False
            else:
                self.movingBackward = False
                self.movingRotation = True
        elif loopName == 'neutral':
            self.movingJumping = False
            self.movingForward = False
            self.movingNeutral = True
            self.movingRotation = False
            self.movingBackward = False
        else:
            self.movingJumping = False
            self.movingForward = False
            self.movingNeutral = False
            self.movingRotation = False
            self.movingBackward = False
        ActorInterval(toon, loopName, playRate=playRate).loop()

    def handleMovement(self, task):
        if self.keyMap['control'] == 1:
            if self.keyMap['forward'] or self.keyMap['backward'] or self.keyMap['left'] or self.keyMap['right']:
                if self.movingJumping == False:
                    if self.toon.physControls.isAirborne:
                        self.setMovementAnimation('running-jump-idle', self.toon, 1.0)
                    else:
                        if self.keyMap['forward']:
                            if self.movingForward == False:
                                self.setMovementAnimation('run', self.toon, 1.0)
                        elif self.keyMap['backward']:
                            if self.movingBackward == False:
                                self.setMovementAnimation('walk', self.toon, -1.0)
                        elif self.keyMap['left'] or self.keyMap['right']:
                            if self.movingRotation == False:
                                self.setMovementAnimation('walk', self.toon, 1.0)
                else:
                    if not self.toon.physControls.isAirborne:
                        if self.keyMap['forward']:
                            if self.movingForward == False:
                                self.setMovementAnimation('run', self.toon, 1.0)
                        elif self.keyMap['backward']:
                            if self.movingBackward == False:
                                self.setMovementAnimation('walk', self.toon, -1.0)
                        elif self.keyMap['left'] or self.keyMap['right']:
                            if self.movingRotation == False:
                                self.setMovementAnimation('walk', self.toon, 1.0)
            else:
                if self.movingJumping == False:
                    if self.toon.physControls.isAirborne:
                        self.setMovementAnimation('jump-idle', self.toon, 1.0)
                    else:
                        if self.movingNeutral == False:
                            self.setMovementAnimation('neutral', self.toon, 1.0)
                else:
                    if not self.toon.physControls.isAirborne:
                        if self.movingNeutral == False:
                            self.setMovementAnimation('neutral', self.toon, 1.0)
        elif self.keyMap['forward'] == 1:
            if self.movingForward == False:
                if not self.toon.physControls.isAirborne:
                    self.setMovementAnimation('run', self.toon, 1.0)
        elif self.keyMap['backward'] == 1:
            if self.movingBackward == False:
                if not self.toon.physControls.isAirborne:
                    self.setMovementAnimation('walk', self.toon, -1.0)
        elif self.keyMap['left'] or self.keyMap['right']:
            if self.movingRotation == False:
                if not self.toon.physControls.isAirborne:
                    self.setMovementAnimation('walk', self.toon, 1.0)
        else:
            if not self.toon.physControls.isAirborne:
                if self.movingNeutral == False:
                    self.setMovementAnimation('neutral', self.toon, 1.0)
        return Task.cont

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
        onScreenDebug.add('Avatar Pos', self.toon.getPos())
        onScreenDebug.add('Avatar HPR', self.toon.getHpr())

        return Task.cont

