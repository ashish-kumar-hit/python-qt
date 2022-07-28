# Create a class programmer for storing information of few programmers working at QualigyTech
class Programmer:
    company = "QualigyTech" # class Attributes
    def __init__(self, name, product):  # Constructor
        self.name = name
        self.product = product
    def getInfo(self):
        print(f'The name of the company is {self.company} programmer is {self.name} and the product is {self.product}')
ashish = Programmer("Ashish","AWS")
aarush = Programmer("Aarush","Github")
ashish.getInfo()
aarush.getInfo()

