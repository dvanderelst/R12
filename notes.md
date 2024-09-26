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
repeats = 5
x_positions = np.linspace(-250, 250, 21)
y_positions = np.asarray([-100, -75, -50, -25, 0, 25, 50, 75, 100])
z_position = 300
yaw_positions = np.asarray([0])
```

After this one, I scrambled the left and the right poles

## Single02

Same settings as single 01.
After this one, I scrambled the poles at both sided

## Single03

Same settings as single 01.
After this one, I scrambled the poles at both sided. 
I also played around with writing a new wifi connection function for the 
head. And swapping to batnet_mobile.

## Single04

Same settings as single 01.
After this one, I scrambled the poles at both sided.

## Single05

Same settings as single 01.
After this one, I scrambled the poles at both sided. 

## Created folder old01

## Single01

Single felt, dense poles at left side.

```
pitch = 0
repeats = 10
x_positions = np.linspace(-200, 600, 33)
y_positions = np.asarray([-100, -75, -50, -25, 0, 25, 50, 75, 100])
z_position = 300
yaw_positions = np.asarray([0])
```
Scrambled poles upon completion

## Single02
Same settings as Single01
Single felt, dense poles at left side.

-----------------------------------------
## Noticed issue

One double felted pole was among those I thought were single felted. 
So, I am redoing the previous measurements. 

## Single01

```
pitch = 0
repeats = 10
x_positions = np.linspace(-200, 500, 35)
y_positions = np.asarray([-100, -75, -50, -25, 0, 25, 50, 75, 100])
z_position = 300
yaw_positions = np.asarray([0])
file_name = 'Single02'
description = 'left single felt'
```

Scrambled poles


## Single02
Same. Scrambled poles. And straightened them

## Single03
Same. Scrambled poles. And straightened them

## Single04
Same. Scrambled poles. And straightened them

## Single05
Same. Replaced the left poles with double felted ones.

## Double01
Same settings but left double felt.
Scrambled poles after completing

## Double02
Same settings but left double felt.
Scrambled poles after completing

## Double03
Same settings but left double felt.
Scrambled poles after completing

## Double04
Same settings but left double felt.
Scrambled poles after completing

## Double05
Same settings but left double felt.
removed poles

## Control01
Removed poles at the left side. Kept blank sparse poles on right.

## Control01
Removed poles at the left side. Kept only a single blank pole (furthest) at right side