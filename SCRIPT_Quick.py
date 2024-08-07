import time
import numpy
from matplotlib import pyplot
from R12 import RobotBat

R = RobotBat.RobotBat(connect_robot=True, connect_sonar=True)

world_x = 95
world_y = 0
world_z = 300
world_pitch = 0
world_yaw = 0

xs = numpy.linspace(-200, 300, 75)
logs = []
for world_x in xs:
    R.set_position(world_x, world_y, world_z, world_yaw, world_pitch)
    measurement = R.measure(plot=True, db=False, title=world_x)
    selected = measurement[35:75]
    selected = numpy.sum(selected, axis=0)
    selected = 20 * numpy.log10(selected[0] / selected[1])
    logs.append(selected)
    time.sleep(1)
    break

pyplot.figure()
pyplot.plot(xs, logs)
pyplot.show()


