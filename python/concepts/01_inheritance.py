class Employee:    # Parent class or Base class
    company = "Google"  # class Attribute

    def showDetails(self):   # Method
        print("This is an employee")

class Programmer(Employee):  # Child class or Derived class
    language = "Python"
    company = "YouTube"
    def getLanguage(self):
        print(f'The language is {self.language}')

    def showDetails(self):
        print("This is an programmer")

e = Employee()   # Object
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
