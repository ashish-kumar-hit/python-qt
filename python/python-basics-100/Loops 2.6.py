# Triangular Letter Pattern
num = int(input("Enter Number: "))
Num = 65
for i in range(1,num+1):
    for j in range(i,i+1):
        print(i * chr(Num),end= '')
        Num +=1
    print("")

# Option-2
for i in range(0,num):
    print(chr(65 + i) * (i+1))