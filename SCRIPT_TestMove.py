import time
import numpy
from R12 import RobotBat

R = RobotBat.RobotBat(connect_robot=True, connect_sonar=False)

world_x = 250
world_y = 0
world_z = 300
world_pitch = 0
world_yaw = 0

R.set_position(world_x, world_y, world_z, world_yaw, world_pitch)


