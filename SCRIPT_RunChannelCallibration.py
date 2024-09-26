from R12 import RobotBat
import time
import numpy as np
from matplotlib import pyplot as plt
R = RobotBat.RobotBat(connect_robot=True, connect_sonar=True)

world_x = 0
world_y = 0
world_z = 300
world_pitch = 0
world_yaw = 0
repeats = 50

timegate = (75, 110)

R.set_position(world_x, world_y, world_z, world_yaw, world_pitch)

all_data = []
plot = False
for i in range(repeats):
    if i == repeats - 1: plot = True
    measurement = R.measure(plot=False, db=False)
    all_data.append(measurement)
    time.sleep(0.1)

all_data = np.array(all_data)
all_data = np.mean(all_data, axis=0)

#%%

zero = all_data[:, 0]
one = all_data[:, 1]

selected0 = zero[timegate[0]:timegate[1]]
selected1 = one[timegate[0]:timegate[1]]

max0 = np.max(selected0)
max1 = np.max(selected1)
max0i = np.argmax(selected0) + timegate[0]
max1i = np.argmax(selected1) + timegate[0]

gain_correction = max1/max0
time_correction = max1i - max0i

corrected = zero * gain_correction
corrected = np.roll(corrected, time_correction)


print(max0, max1, gain_correction, time_correction)

title = f"mx0: {max0}, mx0: {max1}\nmx0i: {max0i}, mx1i: {max1i}\ngain_correction: {gain_correction}\ntime_correction: {time_correction}"

plt.figure()
plt.subplot(2,1,1)
plt.plot(zero, label='zero', color='blue')
plt.plot(one, label='one', color='red')
plt.axvline(timegate[0], color='r', linestyle='--')
plt.axvline(timegate[1], color='r', linestyle='--')
plt.plot(max0i, max0, color='blue', marker='o')
plt.plot(max1i, max1, color='red', marker='o')
plt.legend()
plt.subplot(2,1,2)
plt.plot(corrected, label='zero', color='blue')
plt.plot(one, label='one', color='red')
plt.title(title)
plt.tight_layout()
plt.show()




# zero = measurement[:, 0] * 1.20
# one = measurement[:, 1]
# plt.figure()
# plt.plot(zero, label='zero')
# plt.plot(one, label='one')
# plt.legend()
# plt.show()
#


