# Write a python script that acts as an activity tracker.
# The user should be able to log activities and check their previously logged activities.
# Store the data in a JSON file.
# Use a class structure for your code. Each user and each activity should be an object.
# They should have a many-to-many relationship.

class Activity: # class

    def __init__(self): # constructor

        self.name = input("Enter name of the User: ")
        self.run = int(input(f"How much time(In minutes) {self.name} had been run: "))
        self.cycle = int(input(f"How much time(In minutes) {self.name} had been cycle: "))
        self.walk = int(input(f"How much time(In minutes) {self.name} had been walk: "))
        self.cardio = int(input(f"How much time(In minutes) {self.name} had been cardio: "))

class User(Activity):  # Inheritated class

    def runTime(self): # Methods
        return (self.run)

    def cyclelingTime(self): # Methods
        return (self.cycle)

    def walkingTime(self): # Methods
        return (self.walk)

    def cardioTime(self): # Methods
        return (self.cardio)

obj = User() # Objects of User class
print("********* Your choices are Following *********")
print("1.Running\n2.Cycling\n3.Walking\n4.Cardio\n5.exit()")

import json
my_dict = {}
f = open('My Record.json','w')

for i in range(5):
    User_input = int(input("Which data you want to Access(Kindly type a integer value): "))
    if User_input == 1:
        print(obj.runTime())
        my_dict["Running"] = obj.runTime()
        j = json.dumps(my_dict)

    elif User_input == 2:
        print(obj.cyclelingTime())
        my_dict["Cycling"] = obj.cyclelingTime()
        j = json.dumps(my_dict)

    elif User_input == 3:
        print(obj.walkingTime())
        my_dict['Walking'] = obj.walkingTime()
        j = json.dumps(my_dict)

    elif User_input ==4:
        print(obj.cardioTime())
        my_dict['Cardio'] = obj.cardioTime()
        j = json.dumps(my_dict)

    else:
        f.write(j)
        f.close()
        break