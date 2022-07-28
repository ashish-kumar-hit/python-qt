# Calculate Body Mass Index
print("Welcome to Body Mass Index")
weight = float(input('Enter the weight: '))
height = float(input('Enter height in cm: '))
height_in_m = height / 100
BMI = round((weight / (height_in_m) ** 2),2)
print("Your Result is: ",end = ' ')

if BMI <= 18.5 :
    print("Under Weight")
elif BMI > 18.5 or BMI <= 24.9:
    print("Normal")
elif BMI > 24.9 or BMI <= 29.9:
    print("Obesity")
else:
    print("Over Weight")
