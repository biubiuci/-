
'''USER SETTINGS'''
#linux下串口无法连接时，说明没有权限， sudo chmod 666 /dev/ttyUSB0 更该权限
COM_PORT = '/dev/ttyUSB0'      # Name of the comport connected to RS (use COM port name if on Windows)
# COM_PORT = '/dev/ttyUSB0'     # Name of the comport connected to RS (use ports in /dev/ folder for name Linux)
BAUD = 115200   # Should not need changing from 115200

import time
from serial_device import SerialDevice
from RS1_hardware import PacketID, Mode
from bplprotocol import BplSerial
import serial.tools.list_ports
import math




class Reach5Mini():
    """Reach5Mini Class: Example class used for interfacing with the Reach5Mini attached on the serial port (COM_PORT)
        Has example functionality for sending commands (eg. position, velocity, mode),
        and requesting data (eg. position, current, mode, serial number).
    """
    # 5 device IDs to allow for the 5 axis config.
    deviceIDs = [0x01, 0x02, 0x03, 0x04, 0x05]
    # create an instance of SerialDevice()
    serial_dev = SerialDevice()
    # that instance is passed as argument to BplSerial
    global_serial = BplSerial(serial_dev, len(deviceIDs))
    # If more than one serial device is required (i.e. for multiple grabbers),
    # create additional instances of SerialDevice() and BplSerial()
    # EG: serial_dev_2 = SerialDevice()
    # global_serial_2 = BplSerial(serial_dev_2)

    global_serial.deviceIDs = deviceIDs

    def connect(self):
        self.global_serial.connect(COM_PORT, BAUD)

    def usb_list(self):
        '''
        Prints a list of available serial ports.
        This is a helper function and is non-essential.
        :return: None
        '''
        comports = serial.tools.list_ports.comports()
        print('***\nCOM PORT LIST:')
        for comport in comports:
            print(comport, comport.device)
        print('***\n')

    def enable_all(self):
        '''
        Axes must be enabled before they will respond to further commands.
        :return: None
        '''
        for devid in self.deviceIDs:
            self.global_serial.send_mode(devid, Mode.STANDBY)
        print('Reach5Mini enable_all()')

    def disable_all(self):
        '''
        Disable all axes
        :return: None
        '''
        for devid in self.deviceIDs:
            self.global_serial.send_mode(devid, Mode.DISABLE)
        print('Reach5Mini disable_all()')

    def set_position(self, device_id, position):
        """Set device position: in radians for rotate, or millimetre for grabber"""
        self.global_serial.send_position(device_id, position)
        print('Reach5Mini sent position for device', device_id, ':', position)

    def set_velocity(self, device_id, velocity):
        """Set device velocity: in radians per second for rotate, or millimetres per second for grabber"""
        self.global_serial.send_velocity(device_id, velocity)
        print('Reach5Mini sent velocity for device', device_id, ':', velocity)

    def set_openloop(self, device_id, openloop):
        """Set device openloop: in radians per second for rotate, or millimetres per second for grabber -
            THIS CAN BE DANGEROUS, NOT RECOMMENDED
        """
        self.global_serial.send_openloop(device_id, openloop)
        print('Reach5Mini sent openloop for device', device_id, ':', openloop)

    def set_current(self, device_id, current):
        """Set device current: in mA - THIS CAN BE DANGEROUS, NOT RECOMMENDED"""
        self.global_serial.send_current(device_id, current)
        print('Reach5Mini sent current for device', device_id, ':', current)

    def set_mode(self, device_id, mode):
        """Set device mode: refer to MODE list in RS1_hardware.py for details"""
        self.global_serial.send_mode(device_id, mode)
        print('Reach5Mini sent mode for device', device_id, ':', mode)

    def get_voltage(self):
        '''
        See NOTES ON RECEIVING INFO FROM RS1 at top of document
        for optimisation of this and subsequent get_... functions
        :return: float
        '''
        self.global_serial.send_request_packet(self.deviceIDs[4], PacketID.SUPPLYVOLTAGE)
        time.sleep(0.1) # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(self.deviceIDs[4])
        voltage = this_motor[PacketID.SUPPLYVOLTAGE]
        print('voltage:', str(voltage))
        return voltage

    def get_mode(self, deviceID):
        self.global_serial.send_request_packet(deviceID, PacketID.MODE)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        mode = this_motor[PacketID.MODE]
        print('mode:', str(mode))
        return mode

    def get_current(self, deviceID):
        self.global_serial.send_request_packet(deviceID, PacketID.CURRENT)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        current = this_motor[PacketID.CURRENT]
        print('current:', str(current))
        return current

    def get_velocity(self, deviceID):
        self.global_serial.send_request_packet(deviceID, PacketID.VELOCITY)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        velocity = this_motor[PacketID.VELOCITY]
        print('velocity:', str(velocity))
        return velocity

    def get_position(self, deviceID):
        self.global_serial.send_request_packet(deviceID, PacketID.POSITION)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        position = this_motor[PacketID.POSITION]
        print('position:', str(position))
        return position

    def get_model_number(self):
        self.global_serial.send_request_packet(self.deviceIDs[4], PacketID.MODEL_NUMBER)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(self.deviceIDs[4])
        model_number = this_motor[PacketID.MODEL_NUMBER]
        print('model number:', str(model_number))
        return model_number

    def get_serial_number(self):
        self.global_serial.send_request_packet(self.deviceIDs[4], PacketID.SERIAL_NUMBER)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(self.deviceIDs[4])
        serial_number = this_motor[PacketID.SERIAL_NUMBER]
        print('serial number:', str(serial_number))
        return serial_number

    def get_firmware_version(self):
        self.global_serial.send_request_packet(self.deviceIDs[4], PacketID.VERSION)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(self.deviceIDs[4])
        version = this_motor[PacketID.VERSION]
        print('firmware version:', str(version))
        return version

    def set_end_effector_velocity(self, device_id, x, y, z, yaw=0, pitch=0, roll=0):
        """Move end effector in velocity mode"""
        self.global_serial.send_end_eff_vel(device_id, x, y, z, yaw, pitch, roll)
        print('Reach5Mini end effector moved to position x, y, z, yaw, pitch, roll', x, y, z, yaw, pitch, roll)
    def set_end_effector_position(self, device_id, x, y, z, yaw=0, pitch=0, roll=0):
        """Move end effector to desired position"""
        self.global_serial.send_end_eff_pos(device_id, x, y, z, yaw, pitch, roll)
        print('Reach5Mini end effector moved to position x, y, z, yaw, pitch, roll', x, y, z, yaw, pitch, roll)

def Set_arm_position(rs, x, y, z):
    rs.set_end_effector_velocity(5, 0, 0, 0, 0, 0, 0)
    time.sleep(1)       # give it 2 seconds to allow device to move. This is for demonstration purposes only. Not essential.
    flag = True
    while flag is True:
        m1=rs.get_position(1)
        m2 = rs.get_position(2)
        m3 = rs.get_position(3)
        m4 = rs.get_position(4)
        m5 = rs.get_position(5)
        rs.set_end_effector_position(5, x, y, z)
        time.sleep(2)
        n2 = rs.get_position(2)
        n3 = rs.get_position(3)
        n4 = rs.get_position(4)
        n5 = rs.get_position(5)
        dif = (m2-n2)*(m2-n2)+(m3-n3)*(m3-n3)+(m4-n4)*(m4-n4)+(m5-n5)*(m5-n5)
        if dif<10:
            flag = False
    rs.enable_all()  

def IsReachalbe(x, y, z):
    bRet = True
    if math.pow(math.sqrt(x*x+y*y)-20,2)+math.pow(z-46.2, 2)>math.pow(150.71+math.sqrt(180*180+20*20), 2):
        bRet = False
    
    if math.pow(math.sqrt(x*x+y*y)-20,2)+math.pow(z-46.2, 2)<4796.8936:
        bRet = False

    if math.pow(math.sqrt(x*x+y*y)-20,2)+math.pow(z-46.2+145.3, 2)<32400:
        bRet = False
    return bRet

def Set_Init_Position(rs):
    rs.set_position(5, 0)
    time.sleep(2)
    rs.set_position(4, 90)
    time.sleep(2)
    rs.set_position(3, 0)
    time.sleep(2)
    rs.set_position(2, 120)
    time.sleep(2)
    rs.set_position(1, 500)

    time.sleep(2)

def Grab(rs, size):
    rs.set_position(2, 120)  #旋转夹钳 
    time.sleep(2)
    rs.set_position(1, size)
    

if __name__ == '__main__':
    '''MAIN function/
    The following sequence provides an example of how to use the Reach5Mini class.
    It may be edited to allow for experimentation with the unit.
    '''
    # Setup Reach5Mini and connect to serial port
    rs = Reach5Mini()           # create an instance of the Reach5Mini class
    rs.usb_list()               # list all usb ports. Can be handy if you're not sure which port the RS1 is connected to.
    rs.connect()                # connect to the serial port listed in the COM_PORT var above
    rs.enable_all()             # Make sure all devices are ready to do stuff
    grabber_device_id = rs.deviceIDs[0]         # Device ID of grabber
    base_device_id = rs.deviceIDs[4]            # Device ID of main I/O device on the Reach5Mini (device_id = 5)
    rs.get_mode(base_device_id)

    # Get model number, serial number, firmware version, and voltage of base device - all other devices have the same details
    rs.get_model_number()
    rs.get_serial_number()
    rs.get_firmware_version()
    rs.get_voltage()
    time.sleep(0.1)

    x=216
    y=200
    z=126
    
    #夹钳向下抓取
    a0=20;a1=150.71; a2=20; d0=46.2; d3=-180
    l1=a1
    l2=math.sqrt(a2*a2+d3*d3)
    r = math.sqrt(x*x+y*y)
    l3 = math.sqrt(math.pow(r+a0,2)+math.pow(z-d0,2))
    deg0=math.atan2(y,x)*180/math.pi
    deg2 = math.acos((l1*l1+l2*l2-l3*l3)/(2*l1*l2))-math.asin(2*a2/l1)-\
        math.asin(a2/l2)
    deg2 = deg2*180/math.pi
    deg1 = math.pi*3/2 - math.atan2((z-d0),(r+a0))-math.acos((l1*l1+l3*l3-l2*l2)/(2*l1*l3)) \
        -math.asin(2*a2/l1)
    deg1 = deg1*180/math.pi
    rs.set_position(1, 600)
    time.sleep(2)
    rs.set_position(5, 0)
    time.sleep(3)
    rs.set_position(4, 120)
    time.sleep(3)
    rs.set_position(3, 30)
    time.sleep(3)
    rs.set_position(1, 230)
    time.sleep(3)
    Set_arm_position(rs,x,y,z)
    
    #Set_Init_Position(rs)
    
    # rs.set_position(4, 90)
    # time.sleep(3)
    # rs.set_position(3, 0)
    # time.sleep(3)
    # rs.set_position(5, 90)
    # time.sleep(3)
    # rs.set_position(1, 600)
    # time.sleep(30)
    # rs.set_position(5, 0)
    # time.sleep(4)
    # rs.set_position(4, 180)
    # time.sleep(4)
    # rs.set_position(3, 60)
    # time.sleep(4)
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(4, 90)
    # time.sleep(4)
    # rs.set_position(3, 0)
    # time.sleep(4)
    # rs.set_position(5, 90)
    # time.sleep(4)

    #11
    # rs.set_position(5, 180)
    # time.sleep(2)
    # rs.set_position(3, 270)
    # time.sleep(8)
    # rs.set_position(1, 600)
    # time.sleep(4)
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(3, 0)
    # time.sleep(10)
    # rs.set_position(1, 700)
    # time.sleep(2)
    # rs.set_position(3, 270)
    # time.sleep(12)
    # rs.set_position(1, 600)
    # time.sleep(10)
  
    # rs.set_position(1, 230)
    # time.sleep(6)

    # rs.set_position(3, 0)
    # time.sleep(18)
    # rs.set_position(1, 600)
    # time.sleep(2)
    # rs.set_position(3, 270)
    # time.sleep(8)


    # rs.set_position(1, 250)
    # time.sleep(2)
    
    # rs.set_position(3, 0)
    # time.sleep(2)
    # rs.set_position(1, 220)
    # time.sleep(2)
    
    # rs.set_position(3, 180)
    # time.sleep(4)
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(5,0)
    # time.sleep(4)
    # rs.set_position(3, 50)
    # time.sleep(6)
   
    # rs.set_position(1, 600)
    # time.sleep(2)
    # rs.set_position(3, 180)
    # time.sleep(2)
    #111

    
    #
    # rs.set_position(3, 130)
    # time.sleep(4)
    
    
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(3, 150)
    # time.sleep(4)
    # rs.set_position(5,190)
    # time.sleep(4)
    # rs.set_position(3, 160)
    # time.sleep(2)
    # rs.set_position(2, 150)
    # time.sleep(2)
    # rs.set_position(1, 600)
    # time.sleep(4)
   
    # rs.set_position(3, 130)
    # time.sleep(2)
    # rs.set_position(2, 120)
    # time.sleep(2)
    # rs.set_position(5,90)
    # time.sleep(4)
    # rs.set_position(3, 130)
    # time.sleep(4)
    #
    
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(3, 150)
    # time.sleep(4)
    # rs.set_position(5,160)
    # time.sleep(4)
    # rs.set_position(3, 180)
    # time.sleep(4)
    # rs.set_position(2, 150)
    # time.sleep(2)
    # rs.set_position(1, 600)
    # time.sleep(4)
   
    # rs.set_position(3, 130)
    # time.sleep(2)
    # rs.set_position(2, 120)
    # time.sleep(2)
    # rs.set_position(5,90)
    # time.sleep(4)


    
    # rs.set_position(4, 210)
    # time.sleep(2)
    # rs.set_position(5,90)
    # time.sleep(4)
    # rs.set_position(3, 120)
    # time.sleep(2)
    # # rs.set_position(3, 300)
    # # time.sleep(2)
    
    
    
    
    
    # rs.set_position(4, 210)
    # time.sleep(2)
    # rs.set_position(3, 60)
    # time.sleep(2)
    # rs.set_position(5,120)
    # time.sleep(4)

    
    # rs.set_position(3, 350)
    # time.sleep(2)
    # rs.set_position(1, 230)
    # time.sleep(4)
    # rs.set_position(3, 450)
    # time.sleep(2)
    # rs.set_position(5, 120)
    # time.sleep(2)
    
    # rs.set_position(1, 700)
    # time.sleep(2)
    # rs.set_position(3, 80)
    # time.sleep(2)
    # rs.set_position(5,90)
    # time.sleep(7)
    # rs.set_position(3, 60)
    # time.sleep(2)
    # rs.set_position(2, 120)
    # time.sleep(2)
    # rs.set_position(1, 300)
    # time.sleep(2)
    # rs.set_position(3, 80)
    # time.sleep(2)
    # rs.set_position(4, 210)
    # time.sleep(2)
    
    
    # rs.set_position(5, 135)
    # time.sleep(5)
    # rs.set_position(3, 420)
    # time.sleep(2)
    # rs.set_position(1, 600)
    # time.sleep(2)
    # rs.set_position(5,60)
    # time.sleep(7)
    # rs.set_position(3, 60)
    # time.sleep(2)
    # rs.set_position(1, 260)
    # time.sleep(2)
    # rs.set_position(3, 80)
    # time.sleep(2)
    # rs.set_position(4, 210)
    # time.sleep(2)
    # rs.set_position(2, 120)
    # time.sleep(2)
    # rs.set_position(1, 260)
    # time.sleep(2)
    # rs.set_position(5, 135)
    # time.sleep(5)
    
    
    # rs.set_position(1, 600)
    # time.sleep(2)

    # rs.set_position(5,30)
    # time.sleep(7)
    # rs.set_position(3, 60)
    # time.sleep(2)
    # rs.set_position(1, 260)
    # time.sleep(2)
    # rs.set_position(3, 80)
    # time.sleep(2)
    # rs.set_position(4, 210)
    # time.sleep(2)
    # rs.set_position(2, 120)
    # time.sleep(2)
    # rs.set_position(1, 260)
    # time.sleep(2)
    # rs.set_position(5, 105)
    # time.sleep(5)
    
    
    # rs.set_position(1, 600)
    # time.sleep(2)