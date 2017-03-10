from direct.showbase.DirectObject import DirectObject
import os, json
import Globals

class LocalData(DirectObject):

    def __init__(self):
        DirectObject.__init__(self)
        if os.path.isfile('data/ToonData.json'):
            self.dataExists = True
        else:
            self.dataExists = False
        self.allUserToonNames = []
        self.accept('setLocalData', self.setLocalData)
        self.accept('deleteToon', self.deleteToon)
        self.accept('getData', self.getData)

    def setLocalData(self, species, headStyle, bodyType, legsType, headColor, torsoColor, legColor, name, shirtChoice,
                     shortsChoice):
        with open('data/ToonData.json') as jsonFile:
            data = json.load(jsonFile)
        toonData = {}
        for color in Globals.buttonColors:
            toonData[color] = {}
            if base.buttonPressed == color:
                toonData[color].update({
                    'species': species,
                    'head': headStyle,
                    'torso': bodyType,
                    'legs': legsType,
                    'headColor': headColor,
                    'torsoColor': torsoColor,
                    'legColor': legColor,
                    'name': name,
                    'lastPlayground': Globals.TTCZone,
                    'shirt': shirtChoice,
                    'shorts': shortsChoice
                })
            elif data[color].get('head'):
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

    def getData(self, buttonName):
        base.buttonPressed = buttonName
        with open('data/ToonData.json') as jsonFile:
            data = json.load(jsonFile)
            headStyle = data[buttonName].get('head')
            headColor = data[buttonName].get('headColor')
            species = data[buttonName].get('species')
            legs = data[buttonName].get('legs')
            legColor = data[buttonName].get('legColor')
            torso = data[buttonName].get('torso')
            torsoColor = data[buttonName].get('torsoColor')
            shirt = data[buttonName].get('shirt')
            bottom = data[buttonName].get('shorts')
            name = data[buttonName].get('name')
        messenger.send('finalizeEnter', [species, headStyle, torso, legs, headColor, torsoColor, legColor, shirt,
                                         bottom, name])

    def updateAllUserToonNames(self, names):
        if self.allUserToonNames:
            del self.allUserToonNames[:]
        else:
            self.allUserToonNames = []
        for name in names:
            self.allUserToonNames.append(name)

    def deleteToon(self, buttonPressed):
        with open('data/ToonData.json') as jsonFile:
            data = json.load(jsonFile)
        toonData = {}
        for color in Globals.buttonColors:
            toonData[color] = {}
            if buttonPressed == color:
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
            elif data[color].get('head'):
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
