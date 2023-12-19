#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 其他代码...

import rospy
from scipy.optimize import minimize

from blueprintlab_reachsystem_ros_messages.msg import *
#from pynput.keyboard import Listener, KeyCode

import matplotlib.pyplot as plt

from pynput.keyboard import Listener, KeyCode
import numpy as np
import pickle
from ILoSA.gaussian_process import *
from ILoSA.panda import *
from ILoSA.utils import *
from ILoSA.data_prep import *
import csv
class GPSTracker:
    def __init__(self):
        self.gp = None
        self.control_freq=100 # [Hz]
        self.cart_data=[]
        self.start = True
        self.end = False
        self.cir_dataid=[]
        self.cir_datavalue=[]
        self.listener = Listener(on_press=self._on_press)
        self.listener.start()
        self.es_id=[]
        self.es_value=[]
        self.sub3_ids=[]
        self.sub3_values=[]
        self.cart_data1=[]
        self.params = {"l": 0.5, "sigma_f": 0.2}
   
     
        # r=rospy.Rate(self.control_freq)
    def  connect_ROS(self):
           
            
            self.path_pub = rospy.Publisher('r5m_1/cmd_velocity', single_float, queue_size=10)
            self.path_sub = rospy.Subscriber('r5m_8/cmd_velocity', single_float, self.path_callback)
            self.cir_sub=rospy.Subscriber('r5m_0/cir',single_int,self.cir_callback)
            self.cir_pub = rospy.Publisher('r5m_1/cir', single_int, queue_size=10)
            # Start keyboard listener
            self.cir_SUB1=rospy.Subscriber('r5m_2/cmd_velocity',single_float,self.cir_callback2)
           # self.cir_sub3=rospy.Subscriber('r5m_3/cir',single_int,self.cir_callback3)
            #self,cir_sub31=single_int()
    # def cir_callback3(self,message):
    #      self.sub3_id=message.device_id
    #      self.sub3_value=message.value
         #print("sub3",self.sub3_id)
    def cir_callback2(self,message):
         self.ese_id=message.device_id
         self.ese_value=message.value
         self.es_id.append(self.ese_id)
         self.es_value.append(self.ese_value)
         print("id",self.es_id)
    def cir_callback(self,message):
         print("11")
         self.cir_id=message.device_id
         self.cir_value=message.value
      #
         #print(message)
        #  print(  self.cir_id)
         self.cir_dataid.append(self.cir_id)
         self.cir_datavalue.append(self.cir_value)
        #  print( self.cir_id)
        #  print( self.cir_value)
       
    # def _on_press(self, key):
    #     # This function runs on the background and checks if a keyboard key was pressed
    #     if key == KeyCode.from_char('e'):
    #         self.end = True    
    # def path_th(self):
    #     save_demo = input("Do you want to keep this demonstration? [y/n] \n")
    #     if save_demo.lower()=='y':
    #         self.train_GP(self.cart_data)
    def path_callback(self, cmd_velocity_message):
        
            # Extract x, y coordinates from the received path message
            self.cart_pos =  cmd_velocity_message.device_id
            self.cart_pos1=cmd_velocity_message.value
            
            self.cart_data.append(self.cart_pos)
            self.cart_data1.append(self.cart_pos1)
            print(self.cart_data)
            print(self.cart_data1)   
            #print(self.cart_data)
           
        # Convert x, y to numpy array for GP regression
        # x1 = np.array(self.cart_data)

    def record_path(self):
        
        #print(self.cart_data)
        print("Recording started. Press e to stop.")
        # self.cart_data.append(self.cart_pos)
        # print(self.cart_data)
        print("ll",self.cart_data1)
        print(self.cart_data)
        print(self.cir_datavalue)
        print(self.cir_dataid)
        while not self.end:
             self.es_id=self.es_id
             self.es_value=self.es_value
             self.cir_dataid=self.cir_dataid
             self.cir_datavalue=self.cir_datavalue
             self.cart_data=self.cart_data
             self.cart_data1=self.cart_data1
             #print(self.cart_data)
        return self.cir_dataid,self.cir_datavalue,self.es_id,self.es_value,self.cart_data,self.cart_data1
             #print(self.cir_dataid)
    def _on_press(self, key):
        # This function runs on the background and checks if a keyboard key was pressed
        if key == KeyCode.from_char('e'):
            self.end = True
    # Create GP model with RBF kernelre
    def train_GP(self):
        # gps=GPSTracker()
        # gps.record_path()
        #ad=[]
        cc=[3,0,0]
        csd=[3,0,0]
        a1=[1,0,0]
        av1=[1,500,500]
        a4=[4,0,0]
        av4=[4,90,90]
        a5=[5,0,0]
        av5=[5,0,0]
        abv=[]
        abf=[]
        bs={}
        bs1=[]
        b3=[]
        b4=[]
        b5=[]
        for i in range(len(self.cir_dataid)):
             if self.cir_dataid[i]==1 and av1 in abv:
                  #abv.append(a1)zxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                  asd=[self.cir_dataid[i],abv[-1][2],self.cir_datavalue[i]]
                  abv.append(asd)
                  bs[i]=asd

                  #abv[i]=abv[i+1]
                  #abv.remove(abv[i+1])

                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
             if  self.cir_dataid[i]==1 and av1 not in abv:
                  abv.append(av1)
                  #bs[i]=av1

                  asd=[self.cir_dataid[i],abv[-1][2],self.cir_datavalue[i]]
                  abv.append(asd)
                  bs[i]=asd
                  #abv[i]=abv[i+1]
                 # abv.remove(abv[i+1])
                 # abf.append(a1)
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
           
             if self.cir_dataid[i]==3 and cc in b3:
                  #abv.append(csd)
                  asd3=[self.cir_dataid[i],b3[-1][2],self.cir_datavalue[i]]
                  b3.append(asd3)
                  bs[i]=asd3
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
                #   adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[2*i]]
                #   abf.append(adds)
             if self.cir_dataid[i]==3 and cc not in b3:
                  b3.append(cc)
                  asd3=[self.cir_dataid[i],b3[-1][2],self.cir_datavalue[i]]
                  bs[i]=asd3
                  b3.append(asd3)
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
             if self.cir_dataid[i]==4 and av4 in b4:
                  #abv.append(a4)
                  asd4=[self.cir_dataid[i],b4[-1][2],self.cir_datavalue[i]]
                  b4.append(asd4)
                  bs[i]=asd4
                #   abv.remove(abv[i+1])
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
             if self.cir_dataid[i]==4 and av4 not in b4:
                  b4.append(av4)
                  asd4=[self.cir_dataid[i],b4[-1][2],self.cir_datavalue[i]]
                  bs[i]=asd4
                  b4.append(asd4)
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
             if self.cir_dataid[i]==5 and av5  in b5:
                  
                  asd5=[self.cir_dataid[i],b5[-1][2],self.cir_datavalue[i]]
                  b5.append(asd5)
                  bs[i]=asd5
                  
               
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
             if self.cir_dataid[i]==5 and av5 not in b5:
                  b5.append(av5)
                  asd5=[self.cir_dataid[i],b5[-1][2],self.cir_datavalue[i]]
                  b5.append(asd5)
                  bs[i]=asd5
                  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[i]]
                  abf.append(adds)
            
                          #csd.append(asd)
            #  csd[i+1][0]=self.cir_dataid[i]
            #  csd[i+1][1]=csd[i][2]
            #  csd[i+1][2]=self.cir_datavalue[i]
            #  adds=[self.cir_dataid[i],self.es_value[i],self.cart_data1[2*i]]
            #  cc.append(adds)
        sorted_keys = sorted(bs.keys())
        sorted_values = [bs[key] for key in sorted_keys]
     #    abf=np.array(abf)
     #    sorted_values=np.array(sorted_values)
     #    abf=abf.reshape(-1, 1)
     #    sorted_values=sorted_values.reshape(-1,1)
        print(sorted_values)
        print(abf)
        csv_file_path = 'joint-time-v.csv'
        csv_file_path1='joint-p-p.csv'
        with open(csv_file_path, mode='w', newline='') as file:
          writer = csv.writer(file)
    # 写入数据
          writer.writerows(abf)
        with open(csv_file_path1, mode='w', newline='') as file:
               writer = csv.writer(file)
    # 写入数据
               writer.writerows(sorted_values)
        print(f'Data has been successfully written to {csv_file_path}.')
       # print(abv)   
        #      cc[i+1][0]=self.cir_dataid[i]ssssssssssssssssssssssssssssssssssssssssssssssssssssss
        #      cc[i+1][1]=self.es_valuss[i]
        #      cc[i+1][2]=self.cart_data1[2*i]
       #vaddddddddddddddddddddddddddddddss
        # a=np.array(cc)
        # b=np.array(csd)
        # a=a.reshape(-1, 1)
        # b=b.reshape(-1, 1)wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwe
        kernel = 1.0 * RBF(length_scale=1.0)
        self.gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
        self.gp.fit(abf, sorted_values)
        y_pred, cov= self.gp.predict(abf, return_std=True)
        uncertainty = 1.96 * np.sqrt(np.diag(cov))
        
        print(y_pred)
        ab=single_int()
        for  i in range (len(y_pred)):
             ab.device_id=round(y_pred[i][0])
             ab.value=round(y_pred[i][2])
             self.cir_pub.publish(ab)
             print(ab)
     #    plt.figure(figsize=(8, 6))
     #    plt.scatter(abf, sorted_values, c='r', marker='x', label='Training Data')
     #    plt.plot(abf, sorted_values, 'k--', label='True Function')
     #    plt.plot(abf, y_pred, 'b', label='Predicted Mean')
     #    plt.fill_between(abf.ravel(), y_pred , y_pred + cov, alpha=0.2, color='blue', label='Uncertainty')
     #    plt.xlabel('Input')
     #    plt.ylabel('Output')
     #    plt.title('Gaussian Process Regression')
     #    plt.legend()
     #    plt.show()
        # Publish the GP trajectory
        #print(y_pred)
       
        # kernel = 1.0 * RBF(length_scale=1.0)
        # self.gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
        # self.gp.fit(a, b)

            # Generate a new path using GP model
        #  x_pred = np.linspace(min(x1), max(x1), 1000).reshape(-1,1)
       # y_pred, _ = self.gp.predict(self.cir_dataid, return_std=True)

        # Publish the GP trajectory
       # print(y_pred)
       
        # for i in range(len(y_pred)):
        #     pose =single_float()
        #     pose.stamp.secs =  round(y_pred[i][0])
        #     pose.stamp.nsecs = round( y_pred[i][1])
        #     pose.device_id= round(y_pred[i][2])
        #     pose.value= y_pred[i][3]
        #     print(pose)
        #     self.path_pub.publish(pose)
        #     time.sleep(1)
if __name__ == '__main__':
    rospy.init_node('gp_trajectory_tracker', anonymous=True)
    gps=GPSTracker()
    
    try:
        # tracker = GPSTracker()
        gps.connect_ROS()
        
        gps.record_path()
        gps.train_GP()
        
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
