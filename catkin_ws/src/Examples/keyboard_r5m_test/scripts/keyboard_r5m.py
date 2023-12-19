#!/usr/bin/env python3

import os, sys, time
import rospy
import serial
import re
import struct
import threading
from blueprintlab_reachsystem_ros_messages.msg import *
from pynput.keyboard import Key
from pynput.keyboard import Listener

import time
# from arm_control.serial_device import SerialDevice
# from arm_control.RS1_hardware import PacketID, Mode
# from arm_control.bplprotocol import BplSerial
# import serial.tools.list_ports
# import math
cmd_velocity_pub = rospy.Publisher('r5m_0/cmd_velocity', single_float, queue_size=10)
cmd_velocity_message = single_float()
# cartpose_pose=rospy.init_node('arm_pose_publisher')
# pose_pub = rospy.Publisher('/cartesian_pose', PoseStamped, queue_size=10)
# pose_msg = PoseStamped()
cmd_velocity1_pub = rospy.Publisher('r5m_2/cmd_velocity', single_float, queue_size=10)
cmd_velocity2_pub = rospy.Publisher('r5m_8/cmd_velocity', single_float, queue_size=10)
key_press_times = []
es=single_float()
bs=single_float()
def keyboard_press(key):
    try:
        key_pressed = key.char
    except:
        return
    if key.char == 'w':        
        cmd_velocity_message.device_id = 3
        cmd_velocity_message.value = 0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        #print("w:",cmd_velocity_message)
        #print(type(cmd_velocity_message))
        print('w pressed')
        current_time = time.time()
        key_press_times.append( current_time) 
        # self.global_serial.send_request_packet(deviceID, PacketID.POSITION)
    elif key.char == 's':        
        cmd_velocity_message.device_id = 3
        cmd_velocity_message.value = -0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time) 
        print('s pressed')
    elif key.char == 'a':        
        cmd_velocity_message.device_id = 5
        cmd_velocity_message.value = 0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
        print('a pressed')
    elif key.char == 'd':    
        cmd_velocity_message.device_id = 5
        cmd_velocity_message.value = -0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
        print('d pressed')        
    elif key.char == 'z':    
        cmd_velocity_message.device_id = 1
        cmd_velocity_message.value = 0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        print(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
    elif key.char == 'x':    
        cmd_velocity_message.device_id = 1
        cmd_velocity_message.value =-0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        print(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
        print('d pressed')        
    elif key.char == 'c':    
        cmd_velocity_message.device_id = 4
        cmd_velocity_message.value = 0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
    elif key.char == 'v':    
        cmd_velocity_message.device_id = 4
        cmd_velocity_message.value =- 0.5
        cmd_velocity_pub.publish(cmd_velocity_message)
        current_time = time.time()
        key_press_times.append( current_time)
def keyboard_release(key):    
    if key == Key.esc:
        return False
    try:
        key_released = key.char
    except:
        return
    if key.char == 'w':        
        cmd_velocity_message.device_id = 3
        cmd_velocity_message.value = 0
        
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=3
        bs.value=0.5
        cmd_velocity2_pub.publish(bs)
        print('w pressed')
        current_time = time.time()
        global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key} was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
           # key_press_times=[]
    elif key.char == 's':        
        cmd_velocity_message.device_id = 3
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=3
        bs.value=-0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('s pressed')
    elif key.char == 'a':        
        cmd_velocity_message.device_id = 5
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=5
        bs.value=0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('a pressed')
    elif key.char == 'd':        
        cmd_velocity_message.device_id = 5
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=5
        bs.value=-0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
    elif key.char == 'z':        
        cmd_velocity_message.device_id = 1
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=1
        bs.value=0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('z pressed')     
    elif key.char == 'x':        
        cmd_velocity_message.device_id = 1
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=1
        bs.value=-0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('x pressed')     
    elif key.char == 'c':        
        cmd_velocity_message.device_id = 4
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=4
        bs.value=0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('c pressed')     
    elif key.char == 'v':        
        cmd_velocity_message.device_id = 4
        cmd_velocity_message.value = 0
        cmd_velocity_pub.publish(cmd_velocity_message)
        bs.device_id=4
        bs.value=-0.5
        cmd_velocity2_pub.publish(bs)
        current_time = time.time()
        #global key_press_times
        key_down_time = key_press_times[0]
        if key_down_time is not None:
            key_usage_time = current_time - key_down_time
           
            print(f"Key {key}s was pressed for {key_usage_time} seconds")
        
        es.device_id=cmd_velocity_message.device_id
        es.value=key_usage_time
        key_press_times = []
        print(es)
        cmd_velocity1_pub.publish(es)
        print('v pressed')     
     


def keyboard_r5m_main():

    if not rospy.is_shutdown():
        with Listener(
                    on_press=keyboard_press,
                    on_release=keyboard_release
                    ) as listener:
            listener.join()
        


        
        #cmd_velocity_message.device_id = 3
        #cmd_velocity_message.value = 0.5
        #cmd_velocity_pub.publish(cmd_velocity_message)
        #time.sleep(3.0)
        #cmd_velocity_message.device_id = 3
        #cmd_velocity_message.value = -0.5
        #cmd_velocity_pub.publish(cmd_velocity_message)
        #time.sleep(3.0)

# def publish_joint_states():
#     rospy.init_node('joint_states_publisher')
#     pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
#     rate = rospy.Rate(10)  # 设置发布频率为10Hz

#     while not rospy.is_shutdown():
#         joint_state = JointState()
        # 在这里设置关节状态信息，例如位置、速度等
        # joint_state.position = [0.1, 0.2, 0.3]  # 示例位置
        # joint_state.velocity = [0.01, 0.02, 0.03]  # 示例速度
        # ...

        # pub.publish(joint_state)
        # rate.sleep()
# def get_position(self, deviceID):
#         self.global_serial.send_request_packet(deviceID, PacketID.POSITION)
#         time.sleep(0.1)     # give the serial protocol 0.1 seconds to receive the message
#         self.global_serial.updateMotor(1)
#         this_motor = self.global_serial.get_motor_by_device_id(deviceID)
#         position = this_motor[PacketID.POSITION]
#         print('position:', str(position))
#         return position

if __name__ == "__main__":
    rospy.init_node("keyboard_r5m")
    keyboard_r5m_main()
    