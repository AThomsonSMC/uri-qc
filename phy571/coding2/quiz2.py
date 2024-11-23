#!/usr/bin/env python3
'''
author: Adam Thomson
PHY 571 Quiz 2

Write a code in Python that asks for the inputs for the 4 values
of a 2x2 matrix and finds the eigenvalues and eigenvectors using
NumPy's linear algebra package.
'''

import numpy

try:
    mat_input = input("Please input your matrix as 4 values separated by commas:").split(',')
    num_input = [complex(i) for i in mat_input]
    if len(num_input) != 4:
        print('Please supply 4 values to fill a 2x2 matrix!')
        exit()
    input_matrix = numpy.array([num_input[:2], num_input[2:]])
    eigval, eigvec = numpy.linalg.eig(input_matrix)
    print(f'Eigenvalues: {eigval}')
    print(f'Eigenvectors: {eigvec.tolist()}')
except ValueError:
    print('Please supply numbers (real or complex) for this calculation')
    exit()