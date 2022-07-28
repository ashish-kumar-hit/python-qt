# Challenge 3: We have a group of birds and dogs.
# Take two numbers as input, first number gives the total number of heads and second number
# gives a total number of legs. Write a program to identify all the combinations of how many birds and dogs
# we have in the group for the two numbers given.

import numpy as np
x = np.array([[1,1],[4,2]])
y = np.array([int(i) for i in input('Kindly Enter Total number of Heads & '
                                    'Total number of Legs Seperated with a space\n').split()])
l = np.linalg.solve(x,y)
print("Number of Dogs are {}\nNumber of Birds are {}".format(l[0],l[1]))

# In this question we have to solve two linear equation with the help of numpy library
# Let us consider total number of dogs be x & total number of birds be y
# Equation1: x + y = Total number of Heads & Equation2: 4x + 2y = Total number of legs
# with the help of numpy library, solve these two equation & print the Output result