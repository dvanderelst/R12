# Runs

Left and right are defined as looking from the computer to the back wall

## exploration01
+ exploration01: left side dense 1x felt, right side sparse no felt

## exploration02

+ exploration02: left side dense 1x felt, right side sparse no felt

+ message: left: dense, single felt, right: sparse, no felt
```
pitch = 0
repeats = 5
x_positions = np.linspace(-200, 400, 20)
y_positions = np.asarray([-100, -75, -50, -25, 0, 25, 50, 75, 100])
z_position = 300
```

## exploration03
+ exploration03: same but 10 repeats instead of 5

## Single01

Single felt, dense poles at left side.

```
pitch = 0
repeats = 10
x_positions = np.linspace(-200, 600, 32)
y_positions = np.asarray([-100, -75, -50, -25, 0, 25, 50, 75, 100])
z_position = 300
yaw_positions = np.asarray([0])
```