# Calculate Factorial
n = int(input("ENTER NUMBER WHOSE FACTORIAL YOU WANT TO CALCULATE: "))
fact = 1
for i in range(2,n+1):
    fact = fact * i # fact = 1 * 2 = 2 *3 = 6 * 4 = 24 *5 = 120
print(fact)

#import math
#print(math.factorial(n))