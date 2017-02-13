from direct.showbase.ShowBase import ShowBase

class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.method()

    def method(self):
        obj = self.loader.loadModel('Resources/phase_3/models/char/bear-heads-1000.bam')
        obj.setColor(0.726562, 0.472656, 0.859375, 1.0)
        obj.reparentTo(self.render)

w = Window()
w.run()