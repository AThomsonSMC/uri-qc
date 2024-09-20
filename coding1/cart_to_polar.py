'''
author: Adam Thomson
PHY 571 Coding Assignment 1

Exercise 2.3: Write a program to perform the inverse operation to that of Example 2.2.
That is, ask the user for the Cartesian coordinates x, y of a point in two-dimensional
space, and calculate and print the corresponding polar coordinates, with the angle θ
given in degrees.
'''

import math

try:
    xinput, yinput = input("Please input Cartesian coordinates as 'x,y':").split(',')

    # Convert the input strings into numbers
    xval = float(xinput)
    yval = float(yinput)
except ValueError:
    print('Please supply exactly 2 real numbers for this conversion')
    exit()

# Compute the length
length = math.sqrt((xval)**2 + (yval)**2)

angle = None
try:
    angle = math.atan(yval/xval)
except ZeroDivisionError:
    # Determine special case based on yval
    if yval == 0:
        print('Zero vector: Length 0 and angle is N/A')
        exit()
    # Use the sign of yval to determine sign of angle
    angle = math.copysign((math.pi / 2), yval)

# Arctan only returns (-pi/2, pi/2)
# Check if xval is negative, and increase angle by pi to reflect different phase
if xval < 0:
    angle += math.pi

print("Vector in radial coordinates:")
print(f"Length: {length} - Angle: {math.degrees(angle)} degrees")
