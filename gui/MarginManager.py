import random

class MarginManager:

    def __init__(self):
        self.positions = [(-1.37778, 0, -0.6),
                          (-1.37778, 0, -0.0),
                          (-1.37778, 0, 0.6),
                          (1.37778, 0, -0.6),
                          (1.37778, 0, -0.0),
                          (1.37778, 0, 0.6)]
        self.positionsInUse = []
        self.positionsNotInUse = []
        for x in self.positions:
            self.positionsNotInUse.append(x)

    def getRandomOpenPos(self):
        if not self.getIsPositionAvailable():
            choice = random.choice(self.positionsInUse)
            return choice
        else:
            choice = random.choice(self.positionsNotInUse)
            self.positionsInUse.append(choice)
            self.positionsNotInUse.remove(choice)
            return choice

    def getIsPositionAvailable(self):
        if len(self.positionsNotInUse) == 0:
            return False
        else:
            return True

    def removePosFromInUse(self, x):
        self.positionsInUse.remove(x)
        self.positionsNotInUse.append(x)

    def clearMargins(self):
        messenger.send('deleteMsgBox')
