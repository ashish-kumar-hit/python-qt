class Employee:
    company = "Visa"

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company)