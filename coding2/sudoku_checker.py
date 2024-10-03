#!/usr/bin/env python3
'''
author: Adam Thomson
Sudoku Checker
'''

import numpy

# Input sudoku board here
board = numpy.array([
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,1],
    [3,4,5,6,7,8,9,1,2],
    [4,5,6,7,8,9,1,2,3],
    [5,6,7,8,9,1,2,3,4],
    [6,7,8,9,1,2,3,4,5],
    [7,8,9,1,2,3,4,5,6],
    [8,9,1,2,3,4,5,6,7],
    [9,1,2,3,4,5,6,7,8],
])

totals_x = numpy.cumulative_sum(board, axis=0)
# Check that each entry in last row is 45
print(numpy.all(totals_x[-1] == 45))

totals_y = numpy.cumulative_sum(board, axis=1)
print(numpy.all(totals_y[:,-1] == 45))
