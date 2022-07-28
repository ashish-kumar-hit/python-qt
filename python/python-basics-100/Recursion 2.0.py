# Find GCD
l = []
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter First Number = "))
b = int(input("Enter Second Number = "))
print(gcd(a,b))

# Option-2
# import math
# math.gcd(a,b)