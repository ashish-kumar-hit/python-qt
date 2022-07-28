class Person:
    country = "India"
    def __init__(self):  # constructor
        print("Initializing Person....\n")

    def takeBreath(self):
        print("I am breathing........")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()    # Method overriding
        print("Initializing Employee........\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()  # constructor of super class
        print("I am an Employee so I am luckily breathing.")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()   # constructor of super class
        print("Initializing Programmer........\n")

    def getSalary(self):
        print(f"No salary to Programmers")
    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breathing++")

#p = Person()
#p.takeBreath()  # Instance

#e = Employee()
#e.takeBreath()

pr = Programmer()
#pr.takeBreath()
