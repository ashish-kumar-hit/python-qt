# Print Half Pyramid using loops
num_rows = int(input("Enter Number: "))
k = (num_rows * 2)-2
for i in range(0,num_rows):
    # Spaces
    for j in range(0,k):
        print(' ',end='')
    k = k-2
    # Astriks
    for j in range(0,i+1):
        print("*",end=' ')
    print("")