from gp import *
import time
if __name__ == '__main__':
    gps=GPSTracker()
    gps.connect_ROS()
    time.sleep(1)
    gps.record_path()
    time.sleep(2)
    #gps.train_GP()