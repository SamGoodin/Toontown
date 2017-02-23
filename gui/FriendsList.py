from pandac.PandaModules import *
from direct.gui.DirectGui import *

globalFriendsList = None
def showFriendsList():
    global globalFriendsList
    if globalFriendsList == None:
        globalFriendsList = FriendsList()
    globalFriendsList.enter()
    return

def hideFriendsList():
    if globalFriendsList != None:
        globalFriendsList.exit()
    return

class FriendsList(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, relief=None)
        self.initialiseoptions(FriendsList)
        self.isLoaded = 0
        self.isEntered = 0

    def load(self):
        if self.isLoaded == 1:
            return None
        self.isLoaded = 1
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        auxGui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
        self.title = DirectLabel(parent=self, relief=None, text='', text_scale=0.04,
                                 text_fg=(0, 0.1, 0.4, 1), pos=(0.007, 0.0, 0.2))
        background_image = gui.find('**/FriendsBox_Open')
        self['image'] = background_image
        self.reparentTo(base.a2dTopRight)
        self.setPos(-0.233, 0, -0.46)
        self.scrollList = DirectScrolledList(parent=self, relief=None, incButton_image=(gui.find('**/FndsLst_ScrollUp'),
                                                                                        gui.find('**/FndsLst_ScrollDN'),
                                                                                        gui.find(
                                                                                            '**/FndsLst_ScrollUp_Rllvr'),
                                                                                        gui.find(
                                                                                            '**/FndsLst_ScrollUp')),
                                             incButton_relief=None, incButton_pos=(0.0, 0.0, -0.316),
                                             incButton_image3_color=Vec4(0.6, 0.6, 0.6, 0.6),
                                             incButton_scale=(1.0, 1.0, -1.0),
                                             decButton_image=(gui.find('**/FndsLst_ScrollUp'),
                                                              gui.find('**/FndsLst_ScrollDN'),
                                                              gui.find('**/FndsLst_ScrollUp_Rllvr'),
                                                              gui.find('**/FndsLst_ScrollUp')), decButton_relief=None,
                                             decButton_pos=(0.0, 0.0, 0.117),
                                             decButton_image3_color=Vec4(0.6, 0.6, 0.6, 0.6),
                                             itemFrame_pos=(-0.17, 0.0, 0.06), itemFrame_relief=None, numItemsVisible=8,
                                             items=[])
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.2, 0, 0)))
        clipNP = self.scrollList.attachNewNode(clipper)
        self.scrollList.setClipPlane(clipNP)
        self.close = DirectButton(parent=self, relief=None, image=(
        auxGui.find('**/CloseBtn_UP'), auxGui.find('**/CloseBtn_DN'), auxGui.find('**/CloseBtn_Rllvr')),
                                  pos=(0.01, 0, -0.38), command=self.__close)
        self.left = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
                                                                  gui.find('**/Horiz_Arrow_DN'),
                                                                  gui.find('**/Horiz_Arrow_Rllvr'),
                                                                  gui.find('**/Horiz_Arrow_UP')),
                                 image3_color=Vec4(0.6, 0.6, 0.6, 0.6), pos=(-0.15, 0.0, -0.38), scale=(-1.0, 1.0, 1.0),
                                 command=self.__left)
        self.right = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
                                                                   gui.find('**/Horiz_Arrow_DN'),
                                                                   gui.find('**/Horiz_Arrow_Rllvr'),
                                                                   gui.find('**/Horiz_Arrow_UP')),
                                  image3_color=Vec4(0.6, 0.6, 0.6, 0.6), pos=(0.17, 0, -0.38), command=self.__right)
        self.newFriend = DirectButton(parent=self, relief=None, pos=(-0.14, 0.0, 0.14), image=(
        auxGui.find('**/Frnds_Btn_UP'), auxGui.find('**/Frnds_Btn_DN'), auxGui.find('**/Frnds_Btn_RLVR')), text=(
        '', 'New Friend', 'New Friend'),
                                      text_scale=0.045, text_fg=(0, 0, 0, 1), text_bg=(1, 1, 1, 1),
                                      text_pos=(0.1, -0.085), textMayChange=0, command=self.__newFriend)
        self.secrets = DirectButton(parent=self, relief=None, pos=(0.152, 0.0, 0.14), image=(
        auxGui.find('**/ChtBx_ChtBtn_UP'), auxGui.find('**/ChtBx_ChtBtn_DN'), auxGui.find('**/ChtBx_ChtBtn_RLVR')),
                                    text=('',
                                          'True Friend',
                                          'True Friend',
                                          ''), text_scale=0.045, text_fg=(0, 0, 0, 1),
                                    text_bg=(1, 1, 1, 1), text_pos=(-0.04, -0.085), textMayChange=0,
                                    command=self.__secrets)
        gui.removeNode()
        auxGui.removeNode()
        return

    def enter(self):
        if self.isEntered == 1:
            return None
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        self.show()
        return

    def exit(self):
        if self.isEntered == 0:
            return None
        self.isEntered = 0
        self.hide()
        return None

    def __close(self):
        self.exit()
        messenger.send('closeFriendsList')

    def __secrets(self):
        pass

    def __newFriend(self):
        pass

    def __right(self):
        pass

    def __left(self):
        pass