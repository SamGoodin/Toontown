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

TipDict = {"TIP_NONE": ('',),
 "TIP_GENERAL": ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "Control" key to jump.',
               'Press the "F9" key to take a screenshot, which will be saved in your Toontown Infinite folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without a clothing ticket.',
               'Rewards for some ToonTasks allow you to carry more gags and Jellybeans.',
               'You can have up to 50 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The Toontown Infinite servers continually save all the necessary information.',
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
               'Stronger fishing rods catch heavier fish but cost more Jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'Heavier fish are worth more Jellybeans to the Pet Shop.',
               'Rare fish are worth more Jellybeans to the Pet Shop.',
               'You can sometimes find bags of Jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more Jellybeans.',
               'Adopt a Doodle at the Pet Shop!',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               "Show off your stylin' ride and turbo-boost your Laff limit at Goofy Speedway.",
               'Enter Goofy Speedway through the tire-shaped tunnel in Toontown Central Playground.',
               'Earn Laff points at Goofy Speedway.',
               'Goofy Speedway has six different race tracks. ')}

WelcomeValleyToken = 0
WelcomeValleyBegin = 22000
WelcomeValleyEnd = 61000
DonaldsDock = 1000
ToontownCentral = 2000
TheBrrrgh = 3000
MinniesMelodyland = 4000
DaisyGardens = 5000
OutdoorZone = 6000
FunnyFarm = 7000
GoofySpeedway = 8000
DonaldsDreamland = 9000
BossbotHQ = 10000
SellbotHQ = 11000
CashbotHQ = 12000
LawbotHQ = 13000
GolfZone = 17000
EstateZone = "Estate"
TTCZone = "Toontown Central"
DDZone = "Donald's Dock"
DDLZone = "Donald's Dreamland"
MMZone = "Minnie's Melodyland"
BRZone = "Brrrgh"
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
        DonaldsDock: 'dd',
        ToontownCentral: 'tt',
        TheBrrrgh: 'br',
        MinniesMelodyland: 'mm',
        DaisyGardens: 'dg',
        OutdoorZone: 'oz',
        GoofySpeedway: 'gs',
        DonaldsDreamland: 'dl',
        BossbotHQ: 'bosshq',
        SellbotHQ: 'sellhq',
        CashbotHQ: 'cashhq',
        LawbotHQ: 'lawhq',
        GolfZone: 'gz'
    }
HoodsForTeleportAll = (DDZone,
                       TTCZone,
                       BRZone,
                       MMZone,
                       DGZone,
                       OZZone,
                       GSZone,
                       DDLZone,
                       BBHQ,
                       SBHQ,
                       CBHQ,
                       LBHQ,
                       GZone
                       )
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