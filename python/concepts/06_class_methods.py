class Employee:
    company = "Camel"   # class Attributes
    salary = 100        # class Attributes
    location = "Delhi"  # class Attributes

    #def changeSalary(self,sal):
    #    self.salary = sal  # Instance Attribute

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e = Employee()  # Object
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
