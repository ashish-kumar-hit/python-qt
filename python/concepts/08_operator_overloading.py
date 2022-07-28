class Number:
    def __init__(self,num): # dunder method
        self.num = num

    def __add__(self, num2):  # dunder method
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, other): # dunder methods
        print("Let's Multiply")
        return self.num * other.num
n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)