import serial
import serial.tools.list_ports


class SerialInterface(object):
    """
    Provides connection interface to Arduino via serial communication protocols
    """
    def __init__(self):
        """
        Set default connection properties
        """
        self.current_port = None
        self.connected = False
        self.serial_connection = None
        self.connected_device = None
        self.baudrate = 115200
        self.timeout = 0

    def scan_serial(self):
        """
        Look for availalbe devices on the system. Note that this pattern matching sometimes fetches other serial devices
        and not just arduinos explicitly.
        :return: list of connect serial devices
        """
        devices = []
        try:
            for p in list(serial.tools.list_ports.comports()):
                if "USB2.0" or "COM" in p.description.upper():
                    devices.append(p.device)

            return devices

        except Exception as e:
            print(e)
            raise Exception("An error occurred when getting device list.")

    def connect_serial(self, device, baudrate=115200, timeout=0):
        """
        Establish serial connection with a device
        :param device: str indicating device to connect to
        :param baudrate: int baudrate determining serial communication speed and frequency
        :param timeout: int amount of time to wait for affirmation of received signal
        :return: status code indicating success or not
        """
        if self.serial_connection is not None:
            self.serial_connection.close()
        try:
            self.serial_connection = serial.Serial(device, baudrate=baudrate, timeout=timeout)
            self.connected_device = device
            self.baudrate = baudrate
            self.timeout = timeout

            return 0

        except Exception as e:
            print("Could not connect to " + device)
            print(e)
            return -1

    def send_data(self, data, destination):
        """
        Send data over serial communication link to a connected device
        :param data: int data value to send
        :param destination: str description tag used by control logic in arduino
        :return: None
        """
        try:
            data = (destination + str(data) + "\n").encode()
            self.serial_connection.write(data)
            # self.serial_connection.flush()
        except Exception as e:
            print(e)

    def close_serial(self):
        """
        Disconnect serial device
        :return: None
        """
        try:
            self.serial_connection.close()
        except Exception as e:
            print(e)

    def verify_current_connection(self):
        """
        Check if a serial connection is ready for transmission
        :return: bool indicating ready state
        """
        try:
            if self.serial_connection.is_open:
                return True
            else:
                return False

        except Exception as e:
            print(e)
            return False
