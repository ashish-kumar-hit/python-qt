# Challenge 2: Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# Input: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
l = input().split()
my_dict = {}
for i in sorted(l):
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
for j in my_dict:
    print(f'{j}:{my_dict[j]}')

# Step1 : Take input from Users & Split it into a list
# Step2 : Assign a empty dictionary
# Steo3 : By using for loop & Conditional Statements append all the values with it's frequency in my_dict
# Step4: Again,By using for loop print all the key: value with frequency from my_dict
