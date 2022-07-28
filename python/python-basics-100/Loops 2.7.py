# Diamond made by Astricks
height = int(input("Enter Number of Rows: "))
if height % 2 == 0:
    print("Please enter odd values for Number of Rows")
else:
    middle_row = (height + 2)// 2
    # Upper Portion
    for i in range(middle_row):
        print(" " * (middle_row-i),"*" * (i*2 + 1))
    # Lower Portion
    for i in range(middle_row-2,-1,-1):
        print(" " * (middle_row-i),"*" * (i*2 +1))
