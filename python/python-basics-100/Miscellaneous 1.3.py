# Compute the Area of a Triangle
side_1 = 3
side_2 = 5
side_3 = 7
side = (side_1 + side_2 + side_3) / 2
from math import sqrt
Area = sqrt((side) * (side - side_1) *  (side - side_2) * (side - side_3))
print(Area)
 # Calculate this by taking base & Height
base = float(input("Enter base: "))
height = float(input('Enter Height:'))
Area = round((base * height) / 2, 2)
print(f'Area of triangle of base {base} & height {height} is {Area} ')

