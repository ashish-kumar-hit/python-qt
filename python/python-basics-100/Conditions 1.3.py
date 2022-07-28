# Find minimum of three Numbers
# Option-1
a = 20
b = 5
c = 98
if a <= b and a <= c:
    print(a)
elif b <= c and b <= a:
    print(b)
else:
    print(c)

# Option-2
print(min(a,b,c))