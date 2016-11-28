from direct.stdpy import threading

import DNATesting as DNALoader

class DNABulkLoader:
    def __init__(self, storage, files):
        self.dnaStorage = storage
        self.dnaFiles = files

    def loadDNAFiles(self):
        for file in self.dnaFiles:
            print 'Reading DNA file...', file
            loadDNABulk(self.dnaStorage, file)
        del self.dnaStorage
        del self.dnaFiles

def loadDNABulk(dnaStorage, file):
    dnaLoader = DNALoader.DNALoader()
    if __debug__:
        file = '../resources/' + file
    else:
        file = '/' + file
    dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()

def loadDNAFile(dnaStorage, file):
    print 'Reading DNA file...', file
    dnaLoader = DNALoader.DNALoader()
    if __debug__:
        file = '../resources/' + file
    else:
        file = '/' + file
    node = dnaLoader.loadDNAFile(dnaStorage, file)
    dnaLoader.destroy()
    if node.node().getNumChildren() > 0:
        return node.node()
    return None

def loadDNAFileAI(dnaStorage, file):
    dnaLoader = DNALoader.DNALoader()
    if __debug__:
        file = '../resources/' + file
    else:
        file = '/' + file
    data = dnaLoader.loadDNAFileAI(dnaStorage, file)
    dnaLoader.destroy()
    return data
