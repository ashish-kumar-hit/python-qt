import random

suits = ("Hearts","Diamonds","Spades","Club")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Card class
class Card:

    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]

    def __str__(self):
        return self.suits + " of " + self.ranks

# two_hearts = Card("Hearts","Two")

# Deck class
class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create the card object
                create_card = Card(suit,rank)
                self.all_cards.append(create_card)
            
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()
# print(len(new_deck.all_cards))
# print(new_deck.all_cards[0])
# print(new_deck.shuffle())
# print(new_deck.deal_one())
# mycard = new_deck.deal_one()

class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple cards
            self.add_cards.extend(new_cards)

        else:
            # Single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# new_player = Player("Ashish")
# print(new_player)
# new_player.add_cards(mycard)
# print(new_player)
# print(mycard)

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#print(len(player_one.all_cards))

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print(f'Round Number {round_number}')

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards")
        print("Player Two Won !!!!!!!!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards")
        print("Player One Won!!!!!!!!!")
        game_on = False
        break

    # Start New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_War = True
    while at_War:
        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_War = False

        elif player_one_cards[-1].values < player_two_cards[-1].values:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_War = False

        else:
            print("WAR!!!!!!!")

            if len(player_one.all_cards) < 3:
                print("Player one is unable to declear war")
                print("Player two wins")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player two is unable to declear war")
                print("Player two wins")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
