from direct.stdpy import threading

from DNATesting import DNALoader

class DNABulkLoader:
    def __init__(self, storage, files):
        self.dnaStorage = storage
        self.dnaFiles = files

    def loadDNAFiles(self):
        print 'Reading DNA file...', self.dnaFiles
        loadDNABulk(self.dnaStorage, self.dnaFiles)
        messenger.send('tick')
        del self.dnaStorage
        del self.dnaFiles

def loadDNABulk(dnaStorage, kill):
    dnaLoader = DNALoader(base)
    if __debug__:
        file = kill
    else:
        file = kill
    dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()

def loadDNAFile(dnaStorage, file):
    print 'Reading DNA file...', file
    dnaLoader = DNALoader(base)
    if __debug__:
        file = file
    else:
        file = file
    node = dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()
    if node.node().getNumChildren() > 0:
        return node.node()
    return None

def loadDNAFileAI(dnaStorage, file):
    dnaLoader = DNALoader()
    if __debug__:
        file = file
    else:
        file = file
    data = dnaLoader.loadDNAFileAI(dnaStorage, file)
    dnaLoader.destroy()
    return data
