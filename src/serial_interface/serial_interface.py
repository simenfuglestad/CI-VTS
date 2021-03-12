import sys
import time
import serial
import serial.tools.list_ports
from PySide6 import QtCore
from PySide6.QtCore import *

class SerialInterface(object):
    def __init__(self):
        self.connected = False
        self.serial_connection = None
        self.connected_device = None
        self.baudrate = 2000000
        self.timeout = 0

        self.serial_devices = self.scan_serial()

    def scan_serial(self):
        devices = []
        try:
            for p in list(serial.tools.list_ports.comports()):
                if "ARDUINO" in p.description.upper():
                    devices.append(p.device)

            # print(p.device)
            # print(p.name)
            # print(p.hwid)
            # print(p.description)
            # print(p.manufacturer)
            # print(p.product)
            #
            # print("------------------------------")
            return devices

        except Exception as e:
            print(e)
            raise Exception("An error occurred when getting device list, aborting setup...")

    def connect_serial(self, device, baudrate=2000000, timeout=0):
        if self.serial_connection is not None:
            self.serial_connection.close()
        try:
            self.serial_connection = serial.Serial(device, baudrate=baudrate, timeout=timeout)
            self.connected_device = device
            self.baudrate = baudrate
            self.timeout = timeout

        except Exception as e:
            print("Could not connect to " + device)
            print(e)

    def send_data(self, data):
        try:
            data = (str(data) + "\n").encode()
            self.serial_connection.write
            self.serial_connection.write(data)
            # self.serial_connection.flush()
        except Exception as e:
            print(e)

    def close_serial(self):
        try:
            self.serial_connection.close()
        except Exception as e:
            print(e)

    def verify_current_connection(self):
        try:
            if self.serial_connection.is_open:
                return True
            else:
                return False

        except Exception as e:
            print(e)
            return False

    def verify_serial_connection(f):
        def inner_verify(self, data):
            if self.connected:
                print("Connection verified, proceeding.")
                return f(self, data)
            else:
                print("Cannot verify connection, aborting operation...")

        return inner_verify

    @verify_serial_connection
    def send_to_serial(data):
        pass
        # self.serial_connection.write(b'hello')

    @verify_serial_connection
    def read_from_serial(self, data=None):
        s = self.serial_connection.read(10)
        print(s)

# class SendDataWorker(QRunnable):
#     def __init__(self, serial_connection):
#         self.serial_connection = serial_connection
#
#     def run(self):

