from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode

class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.method()

    def method(self):
        self.house = self.loader.loadModel('Resources/phase_5.5/models/estate/houseA.bam')
        self.house.reparentTo(self.render)
        nameText = TextNode('nameText')
        nameText.setAlign(nameText.ACenter)
        nameText.setFont(self.loader.loadFont('Resources/phase_3/models/fonts/MickeyFont.bam'))
        nameText.setShadowColor(0, 0, 0, 1)
        nameText.setBin('fixed')
        nameText.setWordwrap(16.0)
        xScale = 1.0
        numLines = 0
        nameText.setText("Someone's House")
        self.nameText = nameText
        textHeight = nameText.getHeight() - 2
        textWidth = nameText.getWidth()
        xScale = 1.0
        if textWidth > 16:
            xScale = 16.0 / textWidth
        sign_origin = self.house.find('**/sign_origin')
        pos = sign_origin.getPos()
        sign_origin.setPosHpr(pos[0], pos[1], pos[2] + 0.15 * textHeight, 90, 0, 0)
        self.namePlate = sign_origin.attachNewNode(self.nameText)
        self.namePlate.setDepthWrite(0)
        self.namePlate.setPos(0, -0.05, 0)
        self.namePlate.setScale(xScale)

w = Window()
w.run()