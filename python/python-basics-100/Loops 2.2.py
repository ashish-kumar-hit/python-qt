# Print Digits in Reverse Order
# Option-1
num = int(input("Enter Digit: "))
print(int(str(num)[::-1]))

# Option-2
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10
print(reversed_num)
