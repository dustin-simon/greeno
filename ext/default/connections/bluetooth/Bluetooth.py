from modules.connection.Connection import Connection
from core.application.Application import Application
from modules.action.Action import Action
import os.path
import bluetooth
import time
import _thread
import json

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

        self.clientSocket = None
        self.remoteAddress = None

        print("bluetooth connection opened")
        self._startConnectionListening()


    def close(self):
        print("bluetooth connection closed!")

    def read(self, channel):
        if channel != None:
            data = channel.recv(1024)
            response = str(data, "UTF-8")
            print("bluetooth received: ", response)

            return response

        return None

    def write(self, data, channel):
        try:
            if channel != None:
                channel.send(data)
            else:
                raise ValueError("No socket to send data")
        except Exception as e:
            self._startConnectionListening()

    def _startConnectionListening(self):

        if self.clientSocket != None:
            self.clientSocket.close()
        
        self.clientSocket = None
        self.remoteAddress = None

        _thread.start_new_thread(self._listenConnection, ())
        print("Bluetooth listens for incoming connections")

    def _listenConnection(self):
        self.clientSocket, self.remoteAddress = self.socket.accept()
        print("incoming bluetooth connection from: ", self.remoteAddress)
        self._startMessageListening()

    def _listen(self):
        try:

            while True:
                data = self.read(self.clientSocket)

                if data == None:
                    raise ValueError("no data received!")

                print("RECEIVED: ", data)

                jsonData = json.loads(data)
                action = jsonData["action"].upper()

                handler = Action.getHandler(action)
                response = handler.handleAction(jsonData)

                self.write(response, self.clientSocket)

        except Exception as e:
            print(e)
            self._startConnectionListening()

    def _startMessageListening(self):
        _thread.start_new_thread(self._listen, ())
        print("Bluetooth listens for incoming messages!")
