from pandac.PandaModules import *

defaultBackgroundColor = (0.3, 0.3, 0.3, 1)
signFont = None
rolloverSound = None
clickSound = None

toonBodyScales = {'mouse': 0.6,
 'cat': 0.73,
 'duck': 0.66,
 'rabbit': 0.74,
 'horse': 0.85,
 'dog': 0.85,
 'monkey': 0.68,
 'bear': 0.85,
 'pig': 0.77}

toonHeadScales = {'mouse': Point3(1.0),
 'cat': Point3(1.0),
 'duck': Point3(1.0),
 'rabbit': Point3(1.0),
 'horse': Point3(1.0),
 'dog': Point3(1.0),
 'monkey': Point3(1.0),
 'bear': Point3(1.0),
 'pig': Point3(1.0)}

legHeightDict = {'dgs': 1.5,
 'dgm': 2.0,
 'dgl': 2.75}

torsoHeightDict = {'dgs': 1.5,
 'dgm': 1.75,
 'dgl': 2.25,}

headHeightDict = {'dls': 0.75,
 'dss': 0.5,
 'dsl': 0.5,
 'dll': 0.75,
 'cls': 0.75,
 'css': 0.5,
 'csl': 0.5,
 'cll': 0.75,
 'hls': 0.75,
 'hss': 0.5,
 'hsl': 0.5,
 'hll': 0.75,
 'mls': 0.75,
 'mss': 0.5,
 'rls': 0.75,
 'rss': 0.5,
 'rsl': 0.5,
 'rll': 0.75,
 'fls': 0.75,
 'fss': 0.5,
 'fsl': 0.5,
 'fll': 0.75,
 'pls': 0.75,
 'pss': 0.5,
 'psl': 0.5,
 'pll': 0.75,
 'bls': 0.75,
 'bss': 0.5,
 'bsl': 0.5,
 'bll': 0.75,
 'sls': 0.75,
 'sss': 0.5,
 'ssl': 0.5,
 'sll': 0.75}

def setSignFont(font):
    global signFont
    signFont = font

def getSignFont():
    global signFont
    return signFont

def setRolloverSound(rs):
    global rolloverSound
    rolloverSound = rs

def getRolloverSound():
    global rolloverSound
    return rolloverSound

def setClickSound(cs):
    global clickSound
    clickSound = cs

def getClickSound():
    global clickSound
    return clickSound

def setInterfaceFont(iF):
    global interfaceFont
    interfaceFont = iF

def getInterfaceFont():
    global interfaceFont
    return interfaceFont

WelcomeValleyToken = 0
WelcomeValleyBegin = 22000
WelcomeValleyEnd = 61000
DonaldsDockId = 1000
ToontownCentralId = 2000
TheBrrrghId = 3000
MinniesMelodylandId = 4000
DaisyGardensId = 5000
OutdoorZoneId = 6000
FunnyFarmId = 7000
GoofySpeedwayId = 8000
DonaldsDreamlandId = 9000
BossbotHQId = 10000
SellbotHQId = 11000
CashbotHQId = 12000
LawbotHQId = 13000
GolfZoneId = 17000
TutorialId = 15000
MyEstateId = 16000
GolfZoneId = 17000
PartyHoodId = 18000
EstateZone = "Estate"
TTCZone = "Toontown Central"
DDZone = "Donald's Dock"
DLZone = "Donald's Dreamland"
MMZone = "Minnie's Melodyland"
BRZone = "The Brrrgh"
DGZone = "Daisy Gardens"
GSZone = "Goofy Speedway"
BBHQ = "Bossbot HQ"
CBHQ = "Cashbot HQ"
LBHQ = "Lawbot HQ"
SBHQ = "Sellbot HQ"
OZZone = "Outdoor Zone"
GZone = "Golf Zone"
StreetZone = "-street"
hoodId2Name = {
        DonaldsDockId: 'dd',
        ToontownCentralId: 'tt',
        TheBrrrghId: 'br',
        MinniesMelodylandId: 'mm',
        DaisyGardensId: 'dg',
        OutdoorZoneId: 'oz',
        GoofySpeedwayId: 'gs',
        DonaldsDreamlandId: 'dl',
        BossbotHQId: 'bosshq',
        SellbotHQId: 'sellhq',
        CashbotHQId: 'cashhq',
        LawbotHQId: 'lawhq',
        GolfZoneId: 'gz'
    }
HoodsForTeleportAll = (DDZone,
                       TTCZone,
                       BRZone,
                       MMZone,
                       DGZone,
                       OZZone,
                       GSZone,
                       DLZone,
                       BBHQ,
                       SBHQ,
                       CBHQ,
                       LBHQ,
                       GZone
                       )

lDonaldsDock = ('to', 'in', DDZone)
lToontownCentral = ('to', 'in', TTCZone)
lTheBrrrgh = ('to', 'in', BRZone)
lMinniesMelodyland = ('to', 'in', MMZone)
lDaisyGardens = ('to', 'in', DGZone)
lOutdoorZone = ('to', 'in', OZZone)
lFunnyFarm = ('to the', 'in the', 'Funny Farm')
lGoofySpeedway = ('to', 'in', GSZone)
lDonaldsDreamland = ('to', 'in', DLZone)
lBossbotHQ = ('to', 'in', 'Bossbot HQ')
lSellbotHQ = ('to', 'in', 'Sellbot HQ')
lCashbotHQ = ('to', 'in', 'Cashbot HQ')
lLawbotHQ = ('to', 'in', 'Lawbot HQ')
lTutorial = ('to the', 'in the', 'Toon-torial')
lMyEstate = ('to', 'in', 'your house')
lWelcomeValley = ('to', 'in', 'Welcome Valley')
lGolfZone = ('to', 'in', "Chip 'n Dale's MiniGolf")
lPartyHood = ('to the', 'in the', "Party Grounds")

hoodNameMap = {DonaldsDockId: lDonaldsDock,
 ToontownCentralId: lToontownCentral,
 TheBrrrghId: lTheBrrrgh,
 MinniesMelodylandId: lMinniesMelodyland,
 DaisyGardensId: lDaisyGardens,
 OutdoorZoneId: lOutdoorZone,
 FunnyFarmId: lFunnyFarm,
 GoofySpeedwayId: lGoofySpeedway,
 DonaldsDreamlandId: lDonaldsDreamland,
 BossbotHQId: lBossbotHQ,
 SellbotHQId: lSellbotHQ,
 CashbotHQId: lCashbotHQ,
 LawbotHQId: lLawbotHQ,
 TutorialId: lTutorial,
 MyEstateId: lMyEstate,
 GolfZoneId: lGolfZone,
 PartyHoodId: lPartyHood}
safeZoneCountMap = {MyEstateId: 8,
 TutorialId: 6,
 ToontownCentralId: 6,
 DonaldsDockId: 10,
 MinniesMelodylandId: 5,
 GoofySpeedwayId: 500,
 TheBrrrghId: 8,
 DaisyGardensId: 9,
 FunnyFarmId: 500,
 DonaldsDreamlandId: 5,
 OutdoorZoneId: 500,
 GolfZoneId: 500,
 PartyHoodId: 500}
townCountMap = {MyEstateId: 8,
 TutorialId: 40,
 ToontownCentralId: 37,
 DonaldsDockId: 40,
 MinniesMelodylandId: 40,
 GoofySpeedwayId: 40,
 TheBrrrghId: 40,
 DaisyGardensId: 40,
 FunnyFarmId: 40,
 DonaldsDreamlandId: 40,
 OutdoorZoneId: 40,
 PartyHoodId: 20}
hoodCountMap = {MyEstateId: 2,
 TutorialId: 2,
 ToontownCentralId: 2,
 DonaldsDockId: 2,
 MinniesMelodylandId: 2,
 GoofySpeedwayId: 2,
 TheBrrrghId: 2,
 DaisyGardensId: 2,
 FunnyFarmId: 2,
 DonaldsDreamlandId: 2,
 OutdoorZoneId: 2,
 BossbotHQId: 2,
 SellbotHQId: 43,
 CashbotHQId: 2,
 LawbotHQId: 2,
 GolfZoneId: 2,
 PartyHoodId: 2}

Foreman = 'Factory Foreman'

TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'TOON TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "Control" key to jump.',
               'Press the "F9" key to take a screenshot, which will be saved in your Toontown Rewritten folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without a clothing ticket.',
               'Rewards for some ToonTasks allow you to carry more gags and jellybeans.',
               'You can have up to 50 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The Toontown Rewritten servers continually save all the necessary information.',
               'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.',
               'Some SpeedChat phrases play emotion animations on your Toon.',
               'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.',
               'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.',
               'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.',
               'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!',
               'The names of your True Friends will appear in Blue.',
               'See if you can collect all the fish in Toontown!',
               'Different ponds hold different fish. Try them all!',
               'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.',
               'You can sell your fish to the Fishermen or inside Pet Shops.',
               'Stronger fishing rods catch heavier fish but cost more jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'Heavier fish are worth more jellybeans to the Pet Shop.',
               'Rare fish are worth more jellybeans to the Pet Shop.',
               'You can sometimes find bags of jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more jellybeans.',
               'Adopt a Doodle at the Pet Shop!',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               "Show off your stylin' ride and turbo-boost your Laff limit at Goofy Speedway.",
               'Enter Goofy Speedway through the tire-shaped tunnel in Toontown Central Playground.',
               'Earn Laff points at Goofy Speedway.',
               'Goofy Speedway has six different race tracks. '),
 TIP_STREET: ('There are four types of Cogs: Lawbots, Cashbots, Sellbots, and Bossbots.',
              'Each Gag Track has different amounts of accuracy and damage.',
              'Sound gags will affect all Cogs but will wake up any lured Cogs.',
              'Defeating Cogs in strategic order can greatly increase your chances of winning battles.',
              'The Toon-Up Gag Track lets you heal other Toons in battle.',
              'Gag experience points are doubled during a Cog Invasion!',
              'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.',
              'In battle, gags are used in order from top to bottom as displayed on the Gag Menu.',
              'The row of circular lights over Cog Building elevators show how many floors will be inside.',
              'Click on a Cog to see more details.',
              'Using high level gags against low level Cogs will not earn any experience points.',
              'A gag that will earn experience has a blue background on the Gag Menu in battle.',
              'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.',
              'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.',
              'Each street in Toontown has different Cog levels and types.',
              'Sidewalks are safe from Cogs.',
              'On the streets, side doors tell knock-knock jokes when approached.',
              'Some ToonTasks train you for new Gag Tracks. You only get to choose six of the seven Gag Tracks, so choose carefully!',
              'Traps are only useful if you or your friends coordinate using Lure in battle.',
              'Higher level Lures are less likely to miss.',
              'Lower level gags have a lower accuracy against high level Cogs.',
              'Cogs cannot attack once they have been lured in battle.',
              'When you and your friends defeat a Cog building you are rewarded with portraits inside the rescued Toon Building.',
              'Using a Toon-Up gag on a Toon with a full Laff meter will not earn Toon-Up experience.',
              'Cogs will be briefly stunned when hit by any gag. This increases the chance that other gags in the same round will hit.',
              'Drop gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.',
              'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker Book.',
              'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.',
              'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.',
              'A maximum of four Toons can battle at once.',
              'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.',
              'The two most difficult Cogs of each type are only found in buildings.',
              'Drop gags never work against lured Cogs.',
              'Cogs tend to attack the Toon that has done them the most damage.',
              'Sound gags do not get bonus damage against lured Cogs.',
              'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.',
              'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
 TIP_MINIGAME: ('After you fill up your jellybean jar, any jellybeans you get from Trolley Games automatically spill over into your bank.',
                'You can use the arrow keys instead of the mouse in the "Match Minnie" Trolley Game.',
                'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.',
                'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.',
                'A perfect game of Match Minnie will double your points.',
                'In the Tug-of-War you are awarded more jellybeans if you play against a tougher Cog.',
                'Trolley Game difficulty varies by neighborhood; ' + TTCZone + ' has the easiest and ' + DLZone + ' has the hardest.',
                'Certain Trolley Games can only be played in a group.'),
 TIP_COGHQ: ('You must complete your Sellbot Disguise before visiting the V.P.',
             'You must complete your Cashbot Disguise before visiting the C.F.O.',
             'You must complete your Lawbot Disguise before visiting the Chief Justice.',
             'You can jump on Cog Goons to temporarily disable them.',
             'Collect Cog Merits by defeating Sellbot Cogs in battle.',
             'Collect Cogbucks by defeating Cashbot Cogs in battle.',
             'Collect Jury Notices by defeating Lawbot Cogs in battle.',
             'Collect Stock Options by defeating Bossbot Cogs in battle.',
             'You get more Merits, Cogbucks, Jury Notices, or Stock Options from higher level Cogs.',
             'When you collect enough Cog Merits to earn a promotion, go see the Sellbot V.P.!',
             'When you collect enough Cogbucks to earn a promotion, go see the Cashbot C.F.O.!',
             'When you collect enough Jury Notices to earn a promotion, go see the Lawbot Chief Justice!',
             'When you collect enough Stock Options to earn a promotion, go see the Bossbot C.E.O.!',
             'You can talk like a Cog when you are wearing your Cog Disguise.',
             'Up to eight Toons can join together to fight the Sellbot V.P.',
             'Up to eight Toons can join together to fight the Cashbot C.F.O.',
             'Up to eight Toons can join together to fight the Lawbot Chief Justice.',
             'Up to eight Toons can join together to fight the Bossbot C.E.O.',
             'Inside Cog Headquarters follow stairs leading up to find your way.',
             'Each time you battle through a Sellbot HQ factory, you will gain one part of your Sellbot Cog Disguise.',
             'You can check the progress of your Cog Disguise in your Shticker Book.',
             'You can check your promotion progress on your Disguise Page in your Shticker Book.',
             'Make sure you have full gags and a full Laff Meter before going to Cog Headquarters.',
             'As you get promoted, your Cog disguise updates.',
             'You must defeat the ' + Foreman + ' to recover a Sellbot Cog Disguise part.',
             "Earn Cashbot disguise suit parts as rewards for completing ToonTasks in Donald's Dreamland.",
             'Cashbots manufacture and distribute their currency, Cogbucks, in three Mints - Coin, Dollar and Bullion.',
             'Wait until the C.F.O. is dizzy to throw a safe, or he will use it as a helmet! Hit the helmet with another safe to knock it off.',
             'Earn Lawbot disguise suit parts as rewards for completing ToonTasks for Professor Flake.',
             "It pays to be puzzled: the virtual Cogs in Lawbot HQ won't reward you with Jury Notices."),
 TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!',
              'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.',
              "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.",
              'Reward your Doodle for doing tricks.',
              "If you visit a friend's estate, your Doodle will come too.",
              'Feed your Doodle a jellybean when it is hungry.',
              'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.',
              'Doodles love company. Invite your friends over to play!',
              'All Doodles have unique personalities.',
              'You can return your Doodle and adopt a new one at the Pet Shops.',
              'When a Doodle performs a trick, the Toons around it heal.',
              'Doodles become better at tricks with practice. Keep at it!',
              'More advanced Doodle tricks heal Toons faster.',
              'Experienced Doodles can perform more tricks before getting tired.',
              'You can see a list of nearby Doodles in your Friends List.',
              "Purchase furniture from Clarabelle's Cattlelog to decorate your house.",
              'The bank inside your house holds extra jellybeans.',
              'The closet inside your house holds extra clothes.',
              "Go to your friend's house and try on his clothes.",
              "Purchase better fishing rods from Clarabelle's Cattlelog.",
              'Call Clarabelle using the phone inside your house.',
              'Clarabelle sells a larger closet that holds more clothing.',
              'Make room in your closet before using a Clothing Ticket.',
              'Clarabelle sells everything you need to decorate your house.',
              'Check your mailbox for deliveries after ordering from Clarabelle.',
              "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.",
              "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.",
              "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.",
              'Store extra furniture in your attic.',
              'You will get a notice from Clarabelle when a new Cattlelog is ready.',
              'You will get a notice from Clarabelle when a Cattlelog delivery arrives.',
              'New Cattlelogs are delivered each week.',
              'Look for limited-edition holiday items in the Cattlelog.',
              'Move unwanted furniture to the trash can.',
              'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.',
              'You can invite your friends to your Estate using SpeedChat.',
              'Did you know the color of your house matches the color of your Pick-A-Toon panel?'),
 TIP_KARTING: ("Buy a Roadster, TUV, or Cruiser kart in Goofy's Auto Shop.",
               "Customize your kart with decals, rims and more in Goofy's Auto Shop.",
               'Earn tickets by kart racing at Goofy Speedway.',
               "Tickets are the only currency accepted at Goofy's Auto Shop.",
               'Tickets are required as deposits to race.',
               'A special page in the Shticker Book allows you to customize your kart.',
               'A special page in the Shticker Book allows you to view records on each track.',
               'A special page in the Shticker Book allows you to display trophies.',
               'Screwball Stadium is the easiest track at Goofy Speedway.',
               'Airborne Acres has the most hills and jumps of any track at Goofy Speedway.',
               'Blizzard Boulevard is the most challenging track at Goofy Speedway.'),
 TIP_GOLF: ('Press the Tab key to see a top view of the golf course.', 'Press the Up Arrow key to point yourself towards the golf hole.', 'Swinging the club is just like throwing a pie.')}


InteractivePropTrackBonusTerms = {0: 'Super Toon-Up!',
 1: '',
 2: '',
 3: '',
 4: 'Super Throw!',
 5: 'Super Squirt!',
 6: ''}
HYDRANTS_BUFF_BATTLES = 64
MAILBOXES_BUFF_BATTLES = 65
TRASHCANS_BUFF_BATTLES = 66
WallBitmask = BitMask32(1)
FloorBitmask = BitMask32(2)
GhostBitmask = BitMask32(2048)
FloorOffset = 0.025
ToonSpeedFactor = 1.25
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor
CEFlatPortrait = 7
CEFlatProfile = 8
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
WalkCutOff = 0.5
RunCutOff = 8.0
WakeRunDelta = 0.1
WakeWalkDelta = 0.2
GlobalDialogColor = (1,
 1,
 0.75,
 1)
RPdirectFrame = (1.75, 1, 0.75)
RPskipScale = 0.5
RPskipPos = (0, -.5)

buttonColors = ['red', 'green', 'purple', 'blue', 'pink', 'yellow']

def setDefaultDialogGeom(string):
    global defaultDialogGeom
    defaultDialogGeom = string

def getDefaultDialogGeom():
    global defaultDialogGeom
    return defaultDialogGeom

BuildingNametagShadow = None

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive

allUserToonNames = []

def setCameraBitmask(default, node_path, camera_bitmask, tag = None, tag_function = None, context = None):
    if node_path:
        show = default
        if tag_function:
            show = tag_function(default, tag, context)
        if show:
            node_path.show(camera_bitmask)
        else:
            node_path.hide(camera_bitmask)

def renderReflection(default, node_path, tag = None, tag_function = None, context = None):
    setCameraBitmask(default, node_path, BitMask32.bit(1), tag, tag_function, context)

SPRender = 2
SPDonaldsBoat = 3

mounts = [
        "phase_3.mf",
        "phase_3.5.mf",
        "phase_4.mf",
        "phase_5.mf",
        "phase_5.5.mf",
        "phase_6.mf",
        "phase_7.mf",
        "phase_8.mf",
        "phase_9.mf",
        "phase_10.mf",
        "phase_11.mf",
        "phase_12.mf",
        "phase_13.mf"
]


def importModule(dcImports, moduleName, importSymbols):
    """
    Imports the indicated moduleName and all of its symbols
    into the current namespace.  This more-or-less reimplements
    the Python import command.
    """
    module = __import__(moduleName, globals(), locals(), importSymbols)

    if importSymbols:
        # "from moduleName import symbolName, symbolName, ..."
        # Copy just the named symbols into the dictionary.
        if importSymbols == ['*']:
            # "from moduleName import *"
            if hasattr(module, "__all__"):
                importSymbols = module.__all__
            else:
                importSymbols = module.__dict__.keys()

        for symbolName in importSymbols:
            if hasattr(module, symbolName):
                dcImports[symbolName] = getattr(module, symbolName)
            else:
                raise Exception('Symbol %s not defined in module %s.' % (symbolName, moduleName))
    else:
        # "import moduleName"

        # Copy the root module name into the dictionary.

        # Follow the dotted chain down to the actual module.
        components = moduleName.split('.')
        dcImports[components[0]] = module
