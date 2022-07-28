# Rock,Paper,Scissors
print("=======Welcome to the game=======")
import random
options = ('Rock','Paper','Scissors')
computer = options[random.randint(0,2)]
player = input("Please enter Rock,Paper,Scissors below\n")
if player == computer:
    print("It's a tie! Try Again!")
elif player == 'Rock':
    if computer == 'Paper':
        print("your Opponent chooses paper! you Losse!")
    else:
        print("Your Oppenent chooses scissors! You WIN!")
elif player == 'Paper':
    if computer == 'Scissors':
        print("YOU LOOSE! Your Opponent choose Scissors")
    else:
        print("YOU WIN! Your opponent choose Rock")
elif player == 'Scissors':
    if computer == 'Paper':
        print("YOU WIN! Your opponent choose paper")
    else:
        print("YOU LOOSE! Your opponent choose Rock")
else:
    print("Please enter valid Input")