#!/usr/bin/env python3
'''
author: Adam Thomson
PHY 571 Coding Quiz 1

Write a code in Python that asks for inputs of 2
complex numbers, z1 and z2 and outputs the result
z1z2 and z1/z2.
'''

try:
    input1 = input("Please input first complex number 'a+bj':")
    input2 = input("Please input second complex number 'a+bj':")

    # Convert the input strings into numbers
    z1 = complex(input1)
    z2 = complex(input2)
except ValueError:
    print('Please supply complex numbers exactly as "a+bj" with no spaces')
    exit()

try:
    print(f'z1 * z2: {(z1 * z2)}')
    print(f'z1 / z2: {(z1 / z2)}')
except ZeroDivisionError:
    print("Cannot divide a complex number by 0")
