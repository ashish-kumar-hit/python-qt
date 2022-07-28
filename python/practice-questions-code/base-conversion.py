# Convert Decimal(Base 10) to Any other Bases Number

decimal_number = int(input("Enter Number: "))  # User Input
Base_number = int(input("Enter Base Number: "))  # User Input

def func(decimal_number,Base_number):
    if decimal_number == 0:
        return '0'
    else:
        return (func(decimal_number//Base_number,Base_number) + str(decimal_number % Base_number)).lstrip('0')
print(func(decimal_number,Base_number))