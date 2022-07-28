# Solve Quadratic Equation
a = 1
b = -5
c = 6
D = (b**2 - 4*a*c)**0.5
x1 = (-b - D)/2*a
x2 = (-b + D)/2*a
if D > 0:
    print("Two roots are {} and {}".format(x1,x2))
elif D < 0:
    print("Complex roots are {} and {}".format(x1,x2))
else:
    print("Equal Roots are {} ".format(x1))