from pandac.PandaModules import *
from direct.gui.DirectGui import *
import random
import Globals
from direct.gui import OnscreenText
import Messenger


class NameShop:

    def __init__(self):
        self.pickANameGUIElements = []
        self.typeANameGUIElements = []
        self.allTitles = []
        self.allFirsts = []
        self.allPrefixes = []
        self.allSuffixes = []
        self.addedGenderSpecific = 0
        self.titleActive = 0
        self.firstActive = 0
        self.lastActive = 0
        self.names = ['',
                      '',
                      '',
                      '']
        self.nameIndices = [-1,
                            -1,
                            -1,
                            -1]

    def enter(self, toon, usedNames, warp):
        self.newwarp = warp
        self.avExists = warp
        if self.avExists:
            for g in self.avList:
                if g.position == self.index:
                    self.avId = g.id
        self.toon = toon
        self.boy = 1
        self.girl = 0
        self.usedNames = usedNames
        if not self.addedGenderSpecific or self.oldBoy != self.boy:
            if not self.addedGenderSpecific:
                nameShopGui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
                self.namePanel = DirectFrame(parent=aspect2d, image=None, relief='flat', state='disabled',
                                             pos=(-0.42, 0, -0.15), image_pos=(0, 0, 0.025), frameColor=(1, 1, 1, 0.3))
                panel = nameShopGui.find('**/tt_t_gui_mat_namePanel')
                self.panelFrame = DirectFrame(image=panel, scale=(0.75, 0.7, 0.7), relief='flat',
                                              frameColor=(1, 1, 1, 0), pos=(-0.0163, 0, 0.1199))
                self.panelFrame.reparentTo(self.namePanel, sort=1)
                self.pickANameGUIElements.append(self.namePanel)
                self.pickANameGUIElements.append(self.panelFrame)
                self.nameResult.reparentTo(self.namePanel, sort=2)
                self.circle = nameShopGui.find('**/tt_t_gui_mat_namePanelCircle')
                self.titleCheck = self.makeCheckBox((-0.615, 0, 0.371), 'Title', (0, 0.25, 0.5, 1),
                                                    self.titleToggle)
                self.firstCheck = self.makeCheckBox((-0.2193, 0, 0.371), 'First', (0, 0.25, 0.5, 1),
                                                    self.firstToggle)
                self.lastCheck = self.makeCheckBox((0.3886, 0, 0.371), 'Last', (0, 0.25, 0.5, 1),
                                                   self.lastToggle)
                del self.circle
                self.pickANameGUIElements.append(self.titleCheck)
                self.pickANameGUIElements.append(self.firstCheck)
                self.pickANameGUIElements.append(self.lastCheck)
                self.titleCheck.reparentTo(self.namePanel, sort=2)
                self.firstCheck.reparentTo(self.namePanel, sort=2)
                self.lastCheck.reparentTo(self.namePanel, sort=2)
                nameShopGui.removeNode()
                self.lastprefixScrollList.reparentTo(self.namePanel)
                self.lastprefixScrollList.decButton.wrtReparentTo(self.namePanel, sort=2)
                self.lastprefixScrollList.incButton.wrtReparentTo(self.namePanel, sort=2)
                self.lastsuffixScrollList.reparentTo(self.namePanel)
                self.lastsuffixScrollList.decButton.wrtReparentTo(self.namePanel, sort=2)
                self.lastsuffixScrollList.incButton.wrtReparentTo(self.namePanel, sort=2)
                self.titleHigh.reparentTo(self.namePanel)
                self.prefixHigh.reparentTo(self.namePanel)
                self.firstHigh.reparentTo(self.namePanel)
                self.suffixHigh.reparentTo(self.namePanel)
                self.randomButton.reparentTo(self.namePanel, sort=2)
                self.typeANameButton.reparentTo(self.namePanel, sort=2)
            self.pickANameGUIElements.remove(self.titleScrollList)
            self.pickANameGUIElements.remove(self.firstnameScrollList)
            self.titleScrollList.destroy()
            self.firstnameScrollList.destroy()
            self.titleScrollList = self.makeScrollList(None, (-0.6, 0, 0.202), (1, 0.8, 0.8, 1), self.allTitles,
                                                       self.makeLabel, [TextNode.ACenter, 'title'])
            self.firstnameScrollList = self.makeScrollList(None, (-0.2, 0, 0.202), (0.8, 1, 0.8, 1), self.allFirsts,
                                                           self.makeLabel, [TextNode.ACenter, 'first'])
            self.pickANameGUIElements.append(self.titleScrollList)
            self.pickANameGUIElements.append(self.firstnameScrollList)
            self.titleScrollList.reparentTo(self.namePanel, sort=-1)
            self.titleScrollList.decButton.wrtReparentTo(self.namePanel, sort=2)
            self.titleScrollList.incButton.wrtReparentTo(self.namePanel, sort=2)
            self.firstnameScrollList.reparentTo(self.namePanel, sort=-1)
            self.firstnameScrollList.decButton.wrtReparentTo(self.namePanel, sort=2)
            self.firstnameScrollList.incButton.wrtReparentTo(self.namePanel, sort=2)
            self.listsLoaded = 1
            self.addedGenderSpecific = 1
        self.typeANameButton['text'] = 'Type-A-Name'
        self.__listsChanged()
        self.namePanel.hide()

    def exit(self):
        pass

    def unload(self):
        cleanupDialog('globalDialog')
        self.uberdestroy(self.pickANameGUIElements)
        self.uberdestroy(self.typeANameGUIElements)
        self.approvalDialog.cleanup()
        del self.approvalDialog
        self.isLoaded = 0
        self.makeAToon = None

    def uberdestroy(self, guiObjectsToDestroy):
        for x in guiObjectsToDestroy:
            try:
                x.destroy()
                del x
            except:
                print 'NameShop: Tried to destroy already removed object'

    def load(self):
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        self.arrowUp = gui.find('**/tt_t_gui_mat_namePanelArrowUp')
        self.arrowDown = gui.find('**/tt_t_gui_mat_namePanelArrowDown')
        self.arrowHover = gui.find('**/tt_t_gui_mat_namePanelArrowHover')
        self.squareUp = gui.find('**/tt_t_gui_mat_namePanelSquareUp')
        self.squareDown = gui.find('**/tt_t_gui_mat_namePanelSquareDown')
        self.squareHover = gui.find('**/tt_t_gui_mat_namePanelSquareHover')
        typePanel = gui.find('**/tt_t_gui_mat_typeNamePanel')
        self.typeNamePanel = DirectFrame(parent=aspect2d, image=None, relief='flat', scale=(0.75, 0.7, 0.7),
                                         state='disabled', pos=(-0.0163333, 0, 0.075), image_pos=(0, 0, 0.025),
                                         frameColor=(1, 1, 1, 0))
        self.typePanelFrame = DirectFrame(image=typePanel, relief='flat', frameColor=(1, 1, 1, 0),
                                          pos=(-0.008, 0, 0.019))
        self.typePanelFrame.reparentTo(self.typeNamePanel, sort=1)
        self.typeANameGUIElements.append(self.typeNamePanel)
        self.typeANameGUIElements.append(self.typePanelFrame)
        self.nameLabel = OnscreenText.OnscreenText("Please Type Your Name:", parent=aspect2d,
                                                   style=OnscreenText.ScreenPrompt, scale=0.1,
                                                   pos=(-0.0163333, 0.53))
        self.nameLabel.wrtReparentTo(self.typeNamePanel, sort=2)
        self.typeANameGUIElements.append(self.nameLabel)
        self.nameEntry = DirectEntry(parent=aspect2d, relief=None, scale=0.08,
                                     entryFont=Globals.getInterfaceFont(), width=8.0, numLines=2, focus=0, cursorKeys=1,
                                     pos=(0.0, 0.0, 0.39), text_align=TextNode.ACenter,
                                     autoCapitalize=1)
        self.nameEntry.wrtReparentTo(self.typeNamePanel, sort=2)
        self.typeANameGUIElements.append(self.nameEntry)
        self.submitButton = DirectButton(parent=aspect2d, relief=None, image=(self.squareUp,
                                                                              self.squareDown,
                                                                              self.squareHover,
                                                                              self.squareUp), image_scale=(1.2, 0, 1.1),
                                         pos=(-0.01, 0, -0.25), text='Submit', text_scale=0.06,
                                         text_pos=(0, -0.02), command=self.nameTyped)
        self.submitButton.wrtReparentTo(self.typeNamePanel, sort=2)
        self.typeNamePanel.setPos(-0.42, 0, -0.078)
        self.typeANameGUIElements.append(self.submitButton)
        self.randomButton = DirectButton(parent=aspect2d, relief=None, image=(self.squareUp,
                                                                              self.squareDown,
                                                                              self.squareHover,
                                                                              self.squareUp),
                                         image_scale=(1.15, 1.1, 1.1), scale=(1.05, 1, 1), pos=(0, 0, -0.25),
                                         text="Shuffle", text_scale=0.06, text_pos=(0, -0.02))
        self.pickANameGUIElements.append(self.randomButton)
        self.typeANameButton = DirectButton(parent=aspect2d, relief=None, image=(self.squareUp,
                                                                                 self.squareDown,
                                                                                 self.squareHover,
                                                                                 self.squareUp),
                                            image_scale=(1, 1.1, 0.9), pos=(0.0033, 0, -.38833), scale=(1.2, 1, 1.2),
                                            text='Type-A-Name', text_scale=0.06,
                                            text_pos=(0, -0.02))
        self.pickANameGUIElements.append(self.typeANameButton)
        self.nameResult = DirectLabel(parent=aspect2d, relief=None, scale=(0.09, 0.084, 0.084),
                                      pos=(0.005, 0, 0.585), text=' \n ', text_scale=0.8, text_align=TextNode.ACenter,
                                      text_wordwrap=8.0)
        self.pickANameGUIElements.append(self.nameResult)
        self.allPrefixes.sort()
        self.allSuffixes.sort()
        self.allPrefixes = [' '] + [' '] + self.allPrefixes + [' '] + [' ']
        self.allSuffixes = [' '] + [' '] + self.allSuffixes + [' '] + [' ']
        self.titleScrollList = self.makeScrollList(gui, (-0.6, 0, 0.202), (1, 0.8, 0.8, 1), self.allTitles,
                                                   self.makeLabel, [TextNode.ACenter, 'title'])
        self.firstnameScrollList = self.makeScrollList(gui, (-0.2, 0, 0.202), (0.8, 1, 0.8, 1), self.allFirsts,
                                                       self.makeLabel, [TextNode.ACenter, 'first'])
        self.lastprefixScrollList = self.makeScrollList(gui, (0.2, 0, 0.202), (0.8, 0.8, 1, 1), self.allPrefixes,
                                                        self.makeLabel, [TextNode.ARight, 'prefix'])
        self.lastsuffixScrollList = self.makeScrollList(gui, (0.55, 0, 0.202), (0.8, 0.8, 1, 1), self.allSuffixes,
                                                        self.makeLabel, [TextNode.ALeft, 'suffix'])
        gui.removeNode()
        self.pickANameGUIElements.append(self.lastprefixScrollList)
        self.pickANameGUIElements.append(self.lastsuffixScrollList)
        self.pickANameGUIElements.append(self.titleScrollList)
        self.pickANameGUIElements.append(self.firstnameScrollList)
        self.titleHigh = self.makeHighlight((-0.710367, 0.0, 0.122967))
        self.firstHigh = self.makeHighlight((-0.310367, 0.0, 0.122967))
        self.pickANameGUIElements.append(self.titleHigh)
        self.pickANameGUIElements.append(self.firstHigh)
        self.prefixHigh = self.makeHighlight((0.09, 0.0, 0.122967))
        self.suffixHigh = self.makeHighlight((0.44, 0.0, 0.122967))
        self.pickANameGUIElements.append(self.prefixHigh)
        self.pickANameGUIElements.append(self.suffixHigh)
        nameBalloon.removeNode()
        imageList = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        buttonImage = [imageList, imageList]
        buttonText = ['Subscribe', 'Free Trial']
        buttonText = ["Continue Submission", "Choose Another Name"]
        self.approvalDialog = DirectDialog(dialogName='approvalstate', topPad=0, fadeScreen=0.2, pos=(0, 0.1, 0.1),
                                           button_relief=None, image_color=(1, 1, 1, 1),
                                           text_align=TextNode.ACenter, text='The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n ',
                                           buttonTextList=buttonText, buttonImageList=buttonImage,
                                           buttonValueList=[1, 0])
        self.approvalDialog.buttonList[0].setPos(0, 0, -.3)
        self.approvalDialog.buttonList[1].setPos(0, 0, -.43)
        self.approvalDialog['image_scale'] = (0.8, 1, 0.77)
        for x in xrange(0, 2):
            self.approvalDialog.buttonList[x]['text_pos'] = (0, -.01)
            self.approvalDialog.buttonList[x]['text_scale'] = (0.04, 0.05999)
            self.approvalDialog.buttonList[x].setScale(1.2, 1, 1)

        self.approvalDialog.hide()
        guiButton.removeNode()

    def makeLabel(self, te, index, others):
        alig = others[0]
        listName = others[1]
        if alig == TextNode.ARight:
            newpos = (0.44, 0, 0)
        elif alig == TextNode.ALeft:
            newpos = (0, 0, 0)
        else:
            newpos = (0.2, 0, 0)
        df = DirectFrame(state='normal', relief=None, text=te, text_scale=0.1, text_pos=newpos,
                         text_align=alig, textMayChange=0)
        df.bind(DGG.B1PRESS, lambda x, df=df: self.nameClickedOn(listName, index))
        return df

    def nameClickedOn(self, listType, index):
        if listType == 'title':
            self.titleIndex = index
        elif listType == 'first':
            self.firstIndex = index
        elif listType == 'prefix':
            self.prefixIndex = index
        else:
            self.suffixIndex = index
        self.updateLists()
        self.__listsChanged()

    def updateLists(self):
        oldindex = [self.titleIndex,
                    self.firstIndex,
                    self.prefixIndex,
                    self.suffixIndex]
        self.titleScrollList.scrollTo(self.titleIndex - 2)
        self.restoreIndexes(oldindex)
        self.firstnameScrollList.scrollTo(self.firstIndex - 2)
        self.restoreIndexes(oldindex)
        self.lastprefixScrollList.scrollTo(self.prefixIndex - 2)
        self.restoreIndexes(oldindex)
        self.lastsuffixScrollList.scrollTo(self.suffixIndex - 2)
        self.restoreIndexes(oldindex)

    def makeScrollList(self, gui, ipos, mcolor, nitems, nitemMakeFunction, nitemMakeExtraArgs):
        it = nitems[:]
        ds = DirectScrolledList(items=it, itemMakeFunction=nitemMakeFunction, itemMakeExtraArgs=nitemMakeExtraArgs,
                                parent=aspect2d, relief=None, pos=ipos, scale=0.6,
                                incButton_image=(self.arrowUp,
                                                 self.arrowDown,
                                                 self.arrowHover,
                                                 self.arrowUp), incButton_relief=None, incButton_scale=(1.2, 1.2, -1.2),
                                incButton_pos=(0.0189, 0, -0.5335), incButton_image0_color=mcolor,
                                incButton_image1_color=mcolor, incButton_image2_color=mcolor,
                                incButton_image3_color=Vec4(1, 1, 1, 0), decButton_image=(self.arrowUp,
                                                                                          self.arrowDown,
                                                                                          self.arrowHover,
                                                                                          self.arrowUp),
                                decButton_relief=None, decButton_scale=(1.2, 1.2, 1.2),
                                decButton_pos=(0.0195, 0, 0.1779), decButton_image0_color=mcolor,
                                decButton_image1_color=mcolor, decButton_image2_color=mcolor,
                                decButton_image3_color=Vec4(1, 1, 1, 0), itemFrame_pos=(-.2, 0, 0.028),
                                itemFrame_scale=1.0, itemFrame_relief=DGG.RAISED, itemFrame_frameSize=(-0.07,
                                                                                                       0.5,
                                                                                                       -0.52,
                                                                                                       0.12),
                                itemFrame_frameColor=mcolor, itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=5,
                                forceHeight=0.1)
        return ds

    def makeHighlight(self, npos):
        return DirectFrame(parent=aspect2d, relief='flat', scale=(0.552, 0, 0.11), state='disabled', frameSize=(-0.07,
                                                                                                                0.52,
                                                                                                                -0.5,
                                                                                                                0.1),
                           borderWidth=(0.01, 0.01), pos=npos, frameColor=(1, 0, 1, 0.4))

    def restoreIndexes(self, oi):
        self.titleIndex = oi[0]
        self.firstIndex = oi[1]
        self.prefixIndex = oi[2]
        self.suffixIndex = oi[3]

    def makeCheckBox(self, npos, ntex, ntexcolor, comm):
        return DirectCheckButton(parent=aspect2d, relief=None, scale=0.1, boxBorder=0.08, boxImage=self.circle,
                                 boxImageScale=4, boxImageColor=VBase4(0, 0.25, 0.5, 1), boxRelief=None, pos=npos,
                                 text=ntex, text_fg=ntexcolor, text_scale=0.8, text_pos=(0.2, 0),
                                 indicator_pos=(-0.566667, 0, -0.045), indicator_image_pos=(-0.26, 0, 0.075),
                                 command=comm, text_align=TextNode.ALeft)

    def __listsChanged(self):
        newname = ''
        if self.listsLoaded:
            if self.titleActive:
                self.showList(self.titleScrollList)
                self.titleHigh.show()
                newtitle = self.titleScrollList['items'][self.titleScrollList.index + 2]['text']
                self.nameIndices[0] = self.nameGen.returnUniqueID(newtitle, 0)
                newname += newtitle + ' '
            else:
                self.nameIndices[0] = -1
                self.stealth(self.titleScrollList)
                self.titleHigh.hide()
            if self.firstActive:
                self.showList(self.firstnameScrollList)
                self.firstHigh.show()
                newfirst = self.firstnameScrollList['items'][self.firstnameScrollList.index + 2]['text']
                if newfirst == 'von':
                    nt = 'Von'
                else:
                    nt = newfirst
                self.nameIndices[1] = self.nameGen.returnUniqueID(nt, 1)
                if not self.titleActive and newfirst == 'von':
                    newfirst = 'Von'
                    newname += newfirst
                else:
                    newname += newfirst
                if newfirst == 'von':
                    self.nameFlags[1] = 0
                else:
                    self.nameFlags[1] = 1
                if self.lastActive:
                    newname += ' '
            else:
                self.firstHigh.hide()
                self.stealth(self.firstnameScrollList)
                self.nameIndices[1] = -1
            if self.lastActive:
                self.showList(self.lastprefixScrollList)
                self.showList(self.lastsuffixScrollList)
                self.prefixHigh.show()
                self.suffixHigh.show()
                lp = self.lastprefixScrollList['items'][self.lastprefixScrollList.index + 2]['text']
                ls = self.lastsuffixScrollList['items'][self.lastsuffixScrollList.index + 2]['text']
                self.nameIndices[2] = self.nameGen.returnUniqueID(lp, 2)
                self.nameIndices[3] = self.nameGen.returnUniqueID(ls, 3)
                newname += lp
                if lp in self.nameGen.capPrefixes:
                    ls = ls.capitalize()
                    self.nameFlags[3] = 1
                else:
                    self.nameFlags[3] = 0
                newname += ls
            else:
                self.stealth(self.lastprefixScrollList)
                self.stealth(self.lastsuffixScrollList)
                self.prefixHigh.hide()
                self.suffixHigh.hide()
                self.nameIndices[2] = -1
                self.nameIndices[3] = -1
            self.titleIndex = self.titleScrollList.index + 2
            self.firstIndex = self.firstnameScrollList.index + 2
            self.prefixIndex = self.lastprefixScrollList.index + 2
            self.suffixIndex = self.lastsuffixScrollList.index + 2
            self.nameResult['text'] = newname
            self.names[0] = newname

    def stealth(self, listToDo):
        listToDo.decButton['state'] = 'disabled'
        listToDo.incButton['state'] = 'disabled'
        for item in listToDo['items']:
            if item.__class__.__name__ != 'str':
                item.hide()

    def showList(self, listToDo):
        listToDo.show()
        listToDo.decButton['state'] = 'normal'
        listToDo.incButton['state'] = 'normal'

    def titleToggle(self, value):
        self.titleActive = self.titleCheck['indicatorValue']
        if not (self.titleActive or self.firstActive or self.lastActive):
            self.titleActive = 1
        self.__listsChanged()
        if self.titleActive:
            self.titleScrollList.refresh()
        self.updateCheckBoxes()

    def firstToggle(self, value):
        self.firstActive = self.firstCheck['indicatorValue']
        if self.chastise == 2:
            self.chastise = 0
        if not self.firstActive and not self.lastActive:
            self.firstActive = 1
            self.chastise = 1
        self.__listsChanged()
        if self.firstActive:
            self.firstnameScrollList.refresh()
        self.updateCheckBoxes()

    def lastToggle(self, value):
        self.lastActive = self.lastCheck['indicatorValue']
        if self.chastise == 1:
            self.chastise = 0
        if not self.firstActive and not self.lastActive:
            self.lastActive = 1
            self.chastise = 2
        self.__listsChanged()
        if self.lastActive:
            self.lastprefixScrollList.refresh()
            self.lastsuffixScrollList.refresh()
        self.updateCheckBoxes()

    def updateCheckBoxes(self):
        self.titleCheck['indicatorValue'] = self.titleActive
        self.titleCheck.setIndicatorValue()
        self.firstCheck['indicatorValue'] = self.firstActive
        self.firstCheck.setIndicatorValue()
        self.lastCheck['indicatorValue'] = self.lastActive
        self.lastCheck.setIndicatorValue()

    def nameTyped(self, *args):
        self.nameEntry['focus'] = 0
        name = self.nameEntry.get()
        name = TextEncoder().decodeText(name)
        name = name.strip()
        name = TextEncoder().encodeWtext(name)
        self.nameEntry.enterText(name)
        self.toon.setName(name)
        self.enterGame()

    def getToonName(self):
        return self.nameEntry.get()

    def enterGame(self):
        messenger.send('exitMakeAToon')


