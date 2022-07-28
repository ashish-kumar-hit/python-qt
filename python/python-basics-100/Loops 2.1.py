# Print patterns using loops
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(i,i+1):
        print(i * "* ")
print('\n')
for i in range(1,num+1):
    print(i * ' * ')