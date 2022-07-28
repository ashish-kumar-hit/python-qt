class Employee:
    company = "Google"
    salary = "50K"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
harry = Employee()  # Created new object
harry.salary = 100000
harry.getSalary()  # Employee.getSalary(harry)
ram = Employee()
ram.getSalary()
