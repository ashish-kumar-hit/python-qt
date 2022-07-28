# Maximum among three numbers
# Option-1
a = 2
b = 5
c = 7
if a > b > c: # (a >= b) and (a >= c):
    print(a)
elif b > a > c: # (b >= a) and (b >=c):
    print(b)
else:
    print(c)

# Option-2
print(max(a,b,c))