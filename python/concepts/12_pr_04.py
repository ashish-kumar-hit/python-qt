# Add a static method in problem 2 to greet the user with hello
class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"The value of {self.num} square is {self.num **2}")
    def squareRoot(self):
        print(f"The value of {self.num} square is {self.num ** 0.5}")
    def cube(self):
        print(f"The value of {self.num} square is {self.num ** 3}")

    @staticmethod
    def greet():
        print(f'*********** Hello there welcome to the best calculator of the world***********')
a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
