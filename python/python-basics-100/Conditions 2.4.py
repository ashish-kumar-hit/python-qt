# Interactive Calculator
print('Welcome To Interactive Calculator')
a = int(input("Please enter Ist Number: "))
b = int(input("Please enter 2nd Number: "))
print('Great! Now enter the Operation')
print('1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Integer Division\n6 - Modulo')
op = int(input())
if op == 1:
    print(f'Addition of two numbers {a} and {b} is {a+b}')
elif op == 2:
    print(f'Subtraction of two numbers {a} and {b} is {a - b}')
elif op == 3:
    print(f'Multiplication of two numbers {a} and {b} is {a * b}')
elif op == 4:
    if b ==0:
        print("Division by Zero. Please enter another value of b")
    else:
        print(f'Division of two numbers {a} and {b} is {a / b}')
elif op == 5:
    if b == 0:
        print("Division by Zero. Please enter another value of b")
    else:
        print(f'Integer Division of two numbers {a} and {b} is {a // b}')
elif op == 6:
    if b == 0:
        print("Division by Zero. Please enter another value of b")
    else:
        print(f'Modulo of two numbers {a} and {b} is {a % b}')
else:
    exit()
