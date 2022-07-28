# Convert Decimal to Binary using Recursion
decimal_number = int(input("Enter Number: "))
def convert_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'
    else:
        return (convert_to_binary(decimal_number//2) + str(decimal_number % 2)).lstrip('0')
print(convert_to_binary(decimal_number))