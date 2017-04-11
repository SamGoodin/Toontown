from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task.Task import Task
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator


class Window(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)

        self.activeConnections = []

        self.portAddress = 9099
        self.backlog = 1000
        self.topSocket = self.cManager.openTCPServerRendezvous(self.portAddress, self.backlog)

        self.cListener.addConnection(self.topSocket)

        self.taskMgr.add(self.tskListenerPolling, "Poll the connection listener", -39)
        self.taskMgr.add(self.tskReaderPolling, "Poll the connection reader", -40)

        self.connect()

        datagram = self.sendMessage()
        self.sendDataToAll(datagram)

    def tskListenerPolling(self, taskdata):
        if self.cListener.newConnectionAvailable():

            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()

            if self.cListener.getNewConnection(rendezvous, netAddress, newConnection):
                newConnection = newConnection.p()
                self.activeConnections.append(newConnection)  # Remember connection
                self.cReader.addConnection(newConnection)  # Begin reading connection
        return Task.cont

    def tskReaderPolling(self, taskdata):
        if self.cReader.dataAvailable():
            datagram = NetDatagram()  # catch the incoming data in this instance
            # Check the return value; if we were threaded, someone else could have
            # snagged this data before we did
            if self.cReader.getData(datagram):
                self.processData(datagram)
                pass
        return Task.cont

    def processData(self, dg):
        dgi = PyDatagramIterator(dg)
        msgID = dgi.getUint8()
        if msgID == 1:
            print dgi.getString()

    def sendDataToAll(self, data):
        for aClient in self.activeConnections:
            self.cWriter.send(data, aClient)

    def terminateAllConnections(self):
        for aClient in self.activeConnections:
            self.cReader.removeConnection(aClient)
        self.activeConnections = []
        self.cManager.closeConnection(self.topSocket)

    def sendMessage(self):
        dg = PyDatagram()
        dg.addUint8(1)
        dg.addString("Hello World")
        return dg

    def connect(self):
        port_address = 9099
        ip_address = "localhost"
        timeout = 3000
        myConnection = self.cManager.openTCPClientConnection(ip_address, port_address, timeout)
        if myConnection:
            self.cReader.addConnection(myConnection)
            self.activeConnections.append(myConnection)
            print self.activeConnections

w = Window()
w.run()