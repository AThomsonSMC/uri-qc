#!/usr/bin/env python3
'''
author: Adam Thomson
PHY 571 Coding Assignment 2
'''
import numpy

mat1a1 = numpy.array([[5,-1,2], [6,1,1]])
mat1a2 = numpy.array([[2,1,4], [3,0,5]])
print(f'1.8a) {(mat1a1+mat1a2).tolist()}')

mat1b = numpy.array([[2, -1, -1], [1, 2, 3]])
print(f'1.8b) {(6 * mat1b).tolist()}')

mat1c = numpy.array([[2,1], [0,3]])
print(f'1.8c) {(mat1c + mat1c).tolist()}')

mat1d1 = numpy.array([[1,2], [3,-1]])
mat1d2 = numpy.array([[-1,4], [-2,1]])
print(f'1.8d) {((4*mat1d1) + (5*mat1d2)).tolist()}')

mat1e1 = numpy.array([[2,1], [0,3]])
mat1e2 = numpy.array([[1,1,4], [3,0,5]])
try:
  print(f'1.8e) {((3*mat1e1) + (2*mat1e2)).tolist()}') 
except ValueError:
  print('1.8e) Invalid operation, unable to add matrices of different dimensions!')

print('######')

mat2a1 = numpy.array([[3,1], [-4, 2]])
mat2a2 = numpy.array([[0,5], [0, 0.5]])
print(f'2.14a) {(numpy.dot(mat2a1,mat2a2).tolist())}')

mat2b1 = numpy.array([[1,1,-1], [4,0,3]])
mat2b2 = numpy.array([[2,-1,-1], [3,1,1], [3,1,1]])
print(f'2.14b) {(numpy.dot(mat2b1, mat2b2)).tolist()}')

mat2c1 = numpy.array([[2,-7],[7,4]])
mat2c2 = numpy.array([[1,0, 5],[-1,1,1], [3,8,4]])
try:
  print(f'2.14c) {(numpy.dot(mat2c1, mat2c2)).tolist()}')
except ValueError:
  print('2.14c) Invalid operation, number of rows in second matrix does not match number of columns in first matrix!')

mat2d1 = numpy.array([[5,2], [3,1]])
mat2d2 = numpy.array([[-1,2], [3,-5]])
print(f'2.14d) {(numpy.dot(mat2d1, mat2d2)).tolist()}')

print('######')

mat3a = numpy.array([[5,6], [7,8]])
mat3b = numpy.array([[6,5], [4,3]])
mat3c = numpy.array([[1,2], [8,9]])
print(f'For 2.26, consider the following matrices:')
print(f'A := {mat3a.tolist()}')
print(f'B := {mat3b.tolist()}')
print(f'C := {mat3c.tolist()}')

print('Does r*(AB) = (r*A)B (where r is a real number)?')
print('Take r=5 as an example...')
print(f'r*(AB) = {(5*(numpy.dot(mat3a, mat3b))).tolist()}')
print(f'(r*A)B = {(numpy.dot((5*mat3a), mat3b)).tolist()}')
print('Confirmed!')

print('------')

print('Does A(r*B + s*C) = r*(AB) + s*(AC) (where r, s are real numbers)?')
print('Take r=3, s=7 as an example...')
print(f'A(r*B + s*C) = {numpy.dot(mat3a, (3*mat3b + 7*mat3c)).tolist()}')
print(f'r*(AB) + s*(AC) = {((3*numpy.dot(mat3a, mat3b)) + (7*numpy.dot(mat3a, mat3c))).tolist()}')
print('Confirmed!')

print('######')
print('For 3.29, consider θ = π/6 (30 degrees)')
mat4a = numpy.array([[numpy.cos(numpy.pi/6), -numpy.sin(numpy.pi/6)],
                     [numpy.sin(numpy.pi/6), numpy.cos(numpy.pi/6)]])
mat4b = numpy.array([[numpy.cos(numpy.pi/6), numpy.sin(numpy.pi/6)],
                     [-numpy.sin(numpy.pi/6), numpy.cos(numpy.pi/6)]])
print(f'[[cosθ, -sinθ], [sinθ, cosθ]] = {mat4a.tolist()}')
print(f'[[cosθ, sinθ], [-sinθ, cosθ]] = {mat4b.tolist()}')
print(f'{numpy.dot(mat4a, mat4b).tolist()} would be [[1,0],[0,1]] without approximations')

print('######')

mat5a = numpy.array([[3,1],[0,2]])
print(f'4.13a) {numpy.linalg.inv(mat5a).tolist()}')
mat5b = numpy.array([[0,4],[1,-3]])
print(f'4.13b) {numpy.linalg.inv(mat5b).tolist()}')
mat5c = numpy.array([[2,-3], [-4, 6]])
try:
  print(f'4.13c) {numpy.linalg.inv(mat5c).tolist()}')
except numpy.linalg.LinAlgError:
  print('4.13c) Unable to perform inverse, determinate is 0!')

print('######')

print('Determine the eigenstuff of the pauli matrices')

matpx = numpy.array([[0, 1], [1, 0]])
matpy = numpy.array([[0, complex('0-j')], [complex('0+j'), 0]])
matpz = numpy.array([[1,0], [0,-1]])

eigx = numpy.linalg.eig(matpx)
eigy = numpy.linalg.eig(matpy)
eigz = numpy.linalg.eig(matpz)

print(f'Eigenvalues for σx: {eigx[0].tolist()}')
print(f'Eigenvectors for σx: {eigx[1].tolist()}')
print(f'Eigenvalues for σy: {eigy[0].tolist()}')
print(f'Eigenvectors for σy: {eigy[1].tolist()}')
print(f'Eigenvalues for σz: {eigz[0].tolist()}')
print(f'Eigenvectors for σz: {eigz[1].tolist()}')
print('The eigenvalues of σy are truly (-1, 1) without approximations')

