# ATM Machine

class Account:  # class

    def __init__(self,balance=0):  # Constructor & Attributes

        self.balance = balance

    def deposit(self, dep_amt):  # Methods

        self.balance = self.balance + dep_amt
        return  self.balance

    def withdrawal(self, wd_amt):  # Methods

        # Conditional Statements
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            return self.balance

        else:
            return (f"Your Withdrawal amount must be less than {self.balance} ")

    def balance_enquiry(self):
        return self.balance

a = Account(500)
my_dict = {}
print("************* Welcome TO ATM MACHINE ****************\n")

import datetime

for i in range(1,20):
    print("Kindly enter a Number")
    User_input = int(input("1.deposit()\n2.withdrawal()\n3.Balance Enquiry\n4.exit()\n"))

    if User_input == 1:
        deposit_amount = int(input("Enter How much amount you want to Deposit: "))
        curr_time = datetime.datetime.now()
        my_dict[(curr_time).strftime('%y-%m-%d  %H:%M:%S') ] = a.deposit(deposit_amount)

    elif User_input == 2:
        withdrawal_amount = int(input("Enter How much amount you want to Withdraw: "))
        curr_time = datetime.datetime.now()
        my_dict[(curr_time).strftime('%y-%m-%d  %H:%M:%S')] = a.withdrawal(withdrawal_amount)

    elif User_input == 3:

        curr_time = datetime.datetime.now()
        my_dict[(curr_time).strftime('%y-%m-%d  %H:%M:%S')] = a.balance_enquiry()

    else:
        break

print(my_dict)

# Step1: Define a class & make constructor
# Step2: Define methods for deposit,withdrawal & balance enquiry
# Step3: In withdrawals check cuurent balance with the help of conditional statements
# Step4: Make a object to access the methods of given class
# Step5: Take a empty dictionary to put user activity & update the dictionary
# Step6: import datetime module to track user activity date & time
# Step7: Print the data
