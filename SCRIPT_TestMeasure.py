from R12 import RobotBat
import random
import time
R = RobotBat.RobotBat(connect_robot=False, connect_sonar=True)
R.measure(plot=True)
# for i in range(3):
#     if i%100 == 0:
#         R.measure(plot=True)
#     else:
#         R.measure(plot=False)
#     time.sleep(random.random())
