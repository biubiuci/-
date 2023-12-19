import rospy
import threading
import time

from blueprintlab_reachsystem_ros_messages.msg import *
#from pynput.keyboard import Listener, KeyCode
from RS1_hardware import PacketID
from packetid import Packets
import concurrent.futures
import matplotlib.pyplot as plt
from serial_device import SerialDevice
from pynput.keyboard import Listener, KeyCode
import numpy as np
import pickle
from bplprotocol import BplSerial
import serial.tools.list_ports
import math
import serial.tools.list_ports
import time
COM_PORT = '/dev/ttyUSB0'      # Name of the comport connected to RS (use COM port name if on Windows)
# COM_PORT = '/dev/ttyUSB0'     # Name of the comport connected to RS (use ports in /dev/ folder for name Linux)
BAUD = 115200   # Should not need changing from 115200
class control:
    device_ids=[0x01, 0x02, 0x03, 0x04, 0x05]
    serial_dev = SerialDevice()
    global_serial = BplSerial(serial_dev, len(device_ids))
    global_serial.device_ids = device_ids
    #def  connect_ROS(self):
    def __init__(self):
        self.start = True
        self.end = False
        self.listener = Listener(on_press=self._on_press)
        self.listener.start()
        self.cir_dataids=[]
        self.cir_dataid=[]
        self.cir_datavalue=[]
        self.cir_datavalues=[]
        self.cir_datas=single_int()
        device_ids=[0x01, 0x02, 0x03, 0x04, 0x05]
        serial_dev = SerialDevice()
        global_serial = BplSerial(serial_dev, len(device_ids))
        global_serial.device_ids = device_ids
    def  connect_ROS(self):
        self.cir_csub=rospy.Subscriber('r5m_1/cir',single_int,self.cir_back)
        self.cir_sub=rospy.Subscriber('r5m_0/cir',single_int,self.cir1_callback)
        #self.ab_sub=rospy.Subscriber()
    def cir1_callback(self,message):
         self.cir_id=message.device_id
         self.cir_value=message.value
         self.cir_dataid.append(self.cir_id)
         self.cir_datavalue.append(self.cir_value)
         print(self.cir_dataid)
         print(self.cir_datavalue)
         #print(self.cir_dataid)

    def cir_back(self,message):
        self.cir_datas.device_id=message.device_id
        self.cir_dataids.append(self.cir_datas.device_id)
        self.cir_datas.value=message.value
        self.cir_datavalues.append(self.cir_datas.value)
        print(self.cir_dataids)
        print(self.cir_datavalues)
        #print(self.cir_dataids)
    def value_ca(self):
          
        while not self.end:
            self.cir_dataids=self.cir_dataids
            self.cir_datavalues=self.cir_datavalues
        #return self.cir_dataids,self.cir_datas.requests
		# a=self.cir_dataids
		# b=self.cir_datas.requests
		# if not self.end:
        def back(a):
            rs=control()
            print(self.cir_dataids)
            print(self.cir_datavalues)
            rs.set_position(self.cir_dataids[a],self.cir_datavalues[a])
            time.sleep(3)
            while not self.cir_datavalues[a]==self.cir_datavalue[a]:
                 time.sleep(1)
                 print(self.cir_datavalues[a])
                 print(self.cir_datavalue[a])
                 rs.set_position(self.cir_dataid[a],self.cir_datavalue[a])
                 self.cir_datavalues[a]=int(rs.get_position(self.cir_dataids[a]))
        lock = threading.Lock()
        for item in range(len(self.cir_dataids)):
    # 启动一个线程执行机械臂转动函数
            thread = threading.Thread(target=back, args=(item,))
            thread.start()

    # 等待线程执行完成
            thread.join()
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    # # 提交任务，并获取Future对象列表
    #         futures = [executor.submit(back, item) for item in len(self.cir_dataids)]

    # # 等待所有任务完成
    #         concurrent.futures.wait(futures)

    # # 获取任务的结果
    #         results = [future.result() for future in futures]
    

# 打印结果
            # print(results)
    def get_position(self, deviceID):
       # print("jj",deviceID)
       # print("oo",PacketID.POSITION)
        self.global_serial.send_request_packet(deviceID, PacketID.POSITION)
        time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
        self.global_serial.updateMotor(1)
        this_motor = self.global_serial.get_motor_by_device_id(deviceID)
        #print(this_motor)
        position = this_motor[PacketID.POSITION]
        #print(position)
        print('position:', int(position))
        return position
    def connect(self):
        self.global_serial.connect(COM_PORT, BAUD)
    def set_position(self, device_id, position):
        """Set device position: in radians for rotate, or millimetre for grabber"""
        self.global_serial.send_position(device_id, position)
        print('Reach5Mini sent position for device', device_id, ':', position)
    def _on_press(self, key):
        # This function runs on the background and checks if a keyboard key was pressed
        if key == KeyCode.from_char('i'):
            self.end = True    
    def Set_Init_Position(selfwww):
        gps=control()
        gps.set_position(5, 0)
        time.sleep(2)
        gps.set_position(4, 90)
        time.sleep(2)
        gps.set_position(3, 0)
        time.sleep(2)
#
        gps.set_position(1, 500)

        time.sleep(2)

if __name__ == '__main__':
    rospy.init_node('gp_trajectory_tracker1', anonymous=True)
    gps=control()
    
    #gps.connect_ROS()
    
    
    try:
        #ps.connect()
       # gps.Set_Init_Position()
       # tracker = GPSTracker()
        gps.connect_ROS()
        gps.connect()
        #gps.get_position(3)
        #gps.train_GP()
        gps.value_ca()
        print("1")
        #gps.connect(COM_PORT,BAUD)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
