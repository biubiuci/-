from RS1_hardware import PacketID
from packetid import Packets

import time
from serial_device import SerialDevice

from bplprotocol import BplSerial
import serial.tools.list_ports
import math
COM_PORT = '/dev/ttyUSB0'      # Name of the comport connected to RS (use COM port name if on Windows)
# COM_PORT = '/dev/ttyUSB0'     # Name of the comport connected to RS (use ports in /dev/ folder for name Linux)
BAUD = 115200   # Should not need changing from 115200


class Reach5MiniROSController():
    device_ids=[0x01, 0x02, 0x03, 0x04, 0x05]
    serial_dev = SerialDevice()
    global_serial = BplSerial(serial_dev, len(device_ids))
    global_serial.device_ids = device_ids

    def get_position(self, deviceID):
        print("jj",deviceID)
        print("oo",PacketID.POSITION)
        self.global_serial.send_request_packet(deviceID, PacketID.POSITION)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        print(this_motor)
        position = this_motor[PacketID.POSITION]
        print(position)
        print('position:', str(position))
        return position
    def connect(self):
        self.global_serial.connect(COM_PORT, BAUD)

if __name__ == "__main__":
    rs = Reach5MiniROSController()
    rs.connect()
    rs.get_position(1)
    rs.get_position(3)
    rs.get_position(5)
                
    