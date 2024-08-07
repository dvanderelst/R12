from R12 import RobotBat

R = RobotBat.RobotBat(connect_robot=True, connect_sonar=True)

world_x = 95
world_y = 0
world_z = 300
world_pitch = 0
world_yaw = 0

R.set_position(world_x, world_y, world_z, world_yaw, world_pitch)
measurement = R.measure(plot=True, db=True)



