from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode


class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept('event', self.method)

    def method(self, a, b):
        print a, b


w = Window()
messenger.send('event', ['string', 'otherstring'])
w.run()