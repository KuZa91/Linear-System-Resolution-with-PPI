# This program, will ask to the user for the dimension and the coefficients of a generical linear system of m equation in n variables 
# and will find the best solution for the system by using the Moore-Penrose Pseudoinverse   

import sys
import numpy as np

n = 0
m = 0

while(m < 1):

	m = input('Please insert the number of equations (>= 1): ')

while(n < 1):

	n = input('Please insert the number of variables (>= 1): ')


A = np.zeros((m, n)) # Defining a m*n zeros matrix
C = np.arange(m)     # Defining a vector of dimension m

# Reading the coefficients of the linear system

for i in range (0,m):

	for j in range (0,n):

		inputstring = "Please insert the coefficient of the {1} variable of the {0} equation :".format(i+1,j+1)
		A[i][j] = float(raw_input(inputstring))

# Reading the constant terms in the equations

for i in range (0,m):

	inputstring = "Please insert the constant term of the {0} equation :".format(i+1)
	C[i] = float(raw_input(inputstring))

# Showing the input data to the user

print("The inserted matrix of coefficients is :")

print(A)

print("The constants of the equations are :")

print(C)

# Showing the value of the Moore Penrose Pseudo-Inverse

print("The Moore-Penrose Pseudo-Inverse of the given matrix is :")

A_cross = np.linalg.pinv(A)

print(A_cross)

# Reporting the errors of the approximation A_cross * A = Identity

print("The error matrix given by the product between the pseudo-inverse and the coefficients matrix is :") 

print((A_cross.dot(A)) - np.eye(n))

# Reporting the solutions vector calculated

print("The vector of the solutions that minimize the error of the system is :")

print(A_cross.dot(C))