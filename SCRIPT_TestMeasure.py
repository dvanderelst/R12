from R12 import RobotBat
import random
import time
R = RobotBat.RobotBat(connect_robot=False, connect_sonar=True)

for i in range(1000):
    R.measure(plot=False)
    time.sleep(0.1)
