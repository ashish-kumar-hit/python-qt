# Print Pattern Using Recursion
def pattern(n):
    if n == 1:
        print("*")
    else:
        print('*' * n)
        pattern(n-1)
n = int(input("Enter Number: "))
pattern(n)