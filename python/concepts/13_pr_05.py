# Write a class Train which has methods to book a ticket, get Status(no of seats) and get fare
# information of trains running under Indian Railways
class Train:
    def __init__(self,name,fare,seats): # Constructor
        self.name = name
        self.fare = fare
        self.seats = seats
    def get_status(self):  # Method
        print("*********************")
        print(f"The name of the train is {self.name}")
        print(f'The seats avilable in the train are {self.seats}')

    def get_fare(self): # Method
        print(f'The price of the ticket is : Rs. {self.fare}')

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self,seatNo):
        pass

intercity = Train("Intercity Express: 14015", 90, 2)
intercity.get_fare()
intercity.get_status()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()