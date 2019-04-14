from modules.connection.Connection import Connection
from core.application.Application import Application
import os.path
import bluetooth
import time

class Bluetooth(Connection):

    def open(self):
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket.bind(("", bluetooth.PORT_ANY))
        self.socket.listen(1)

        bluetooth.advertise_service(self.socket,
                                self.config.get("serviceName"),
                                service_id=self.config.get("uuid"),
                                service_classes=[self.config.get("uuid"), bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])

        print("bluetooth opened!")
        
        self.clientSocket, self.remoteAddress = self.socket.accept()
        print("connected with: " + self.clientSocket.getsockname())


    def close(self):
        pass

    def write(self, data, channel):
        pass

    def read(self, channel):
        pass