'''
author: Adam Thomson
PHY 571 Coding Assignment 1

For each of the following:
- Print in standard form: a + bi
- Print in polar form: r(cos(x) + i*sin(x))
- Print in exponential form: re^(i*x)
'''
import cmath

# Input radius and theta to print vector as polar form
def _print_polar_form(radius, theta):
    print(f'Polar: {radius}(cos({theta}) + i*sin({theta}))')

# Input radius and theta to print vector as exponential form
def _print_exp_form(radius, theta):
    print(f'Exponential: {radius}*e^(i*{theta})\n')

# Input a complex number and print the asked for results
def print_results(cnum):
    print(f'Standard: {cnum}')
    radius, theta = cmath.polar(cnum)
    _print_polar_form(radius, theta)
    _print_exp_form(radius, theta)

print('#1. (4 + 2i) + (-3 - 5i)')
c1 = (4 + 2j) + (-3 - 5j)
print_results(c1)

print('#2. (-3 + 4i) - (5 + 2i)')
c2 = (-3 + 4j) - (5 + 2j)
print_results(c2)

print('#3. (-8 - 7i) - (5 - 4i)')
c3 = (-8 - 7j) - (5 - 4j)
print_results(c3)

print('#4. (-3 + 4i) - (5 + 2i)')
c4 = (3 - 2j) * (5 + 4j)
print_results(c4)

print('#5. (3 - 4i)^2')
c5 = (-3 - 4j)**2
print_results(c5)

print('#6. (3 - 2i)(5 + 4i) - (3 - 4i)^2')
c6 = ((3 - 2j) * (5 + 4j)) - ((3 - 4j) ** 2)
print(c6)
print_results(c6)

print('#7. (3 + 7i) / (5 - 3i)')
c7 = (3 + 7j) / (5 - 3j)
print_results(c7)

print('#8. i^925')
c8 = complex(real=0, imag=1) ** (925 % 4)
print_results(c8)

print('#9. i^460')
c9 = complex(real=0, imag=1) ** (460 % 4)
print_results(c9)
