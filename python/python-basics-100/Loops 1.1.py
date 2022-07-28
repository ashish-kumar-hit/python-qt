# Print integers in Reverse Order
n = int(input("Enter value of n: "))
for i in range (n,0,-1):
    print(i)
print('\n')
for i in reversed(range(1,n+1,1)):
    print(i)