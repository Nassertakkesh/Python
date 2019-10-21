
import random

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        # if name doesn't exist, use val as a string for name
        self.name = names.get(val) or str(val)

    def show(self):
        print(f"{self.name} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []

        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
        self.shuffle()

    def shuffle(self):
        pass

    def show(self):
        for card in self.cards:
            card.show()
  
   
    def randomCards(self):
        my_randoms=[]
        for i in range (5):
            john = [random.randrange(1, 14, 1)]
            my_randoms.append(john)

        print (my_randoms)


class Player():
    def __init__(self, first_name, cards):
        self.first_name = first_name
        self.hand = []

    
    def drawCard(self, deck):
        deck.cards


print()




# import random
# my_randoms=[]
# for i in range (10):
#     my_randoms.append(random.randrange(1, 101, 1))
#     print (my_randoms)
# # class Player():
#     def __init__(self, first_name):
#         self.first_name = first_name;
#         self.hand = []

#     def randomCard(self):
#         suite1: 

#         value1:
#         self.hand.append(Deck()
   

# user1 = Player("nate" )
# print(user1.hand)


# print(user1.randomCard)
# print(user1.cards1)



# we need to create a card 
# we need to create a suite
# each suite  is composed of 13 cards
# we need to differentiate each card so that 
# then we need to create a deck, which is composed of 4 different suits 

# we need to build a class that creates different users
# we need to find a way build a method that gives each user 5 random cards and also at the same time, subtracts those specific cards from the deck 




# 1. choose user
# 2. give each player 7 cards    
# 3. if player one has any similar cards, asks player two for that card 
# 4. if player two has this he gives it to player one
# 5. if he does not, he says go fish and player one get one card from the remainder of deck
# 6. if there are four of the same card in player ones deck, then he colleccts those four and puts them away.
# 7. this game goes till there are no more cards
# 8. 
# 9. 





# """
#     OOP Card Game Hackathon
# ​
#     open terminal -> cd to dir where your py file is
#     open shell by typing python or python3 on mac
#     from name_of_file import *
# ​
#     now you can execute functions / use vars from file in shell
# ​
#     Starting code:
# """
# import random


# class Card():
#     def __init__(self, suit, val):
#         self.suit = suit
#         self.val = val

#         names = {
#             1: "Ace",
#             11: "Jack",
#             12: "Queen",
#             13: "King"
#         }

#         # if name doesn't exist, use val as a string for name
#         self.name = names.get(val) or str(val)

#     def show(self):
#         print(f"{self.name} of {self.suit}")


# class Deck():
#     def __init__(self):
#         self.cards = []

#         for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
#             for val in range(1, 14):
#                 self.cards.append(Card(suit, val))
#         self.shuffle()

#     def shuffle(self):
#         pass  ​

#     def show(self):
#         for card in self.cards:
#             card.show()

# # class Player():
# #     def __init__(self, first_name, cards):
# #         self.first_name = first_name;
# #         self.cards = 

# #     def randomCard(self)
# #         random_num = random.choice() 



# print()



# 1. choose user
# 2. give each player 7 cards    
# 3. if player one has any similar cards, asks player two for that card 
# 4. if player two has this he gives it to player one
# 5. if he does not, he says go fish and player one get one card from the remainder of deck
# 6. if there are four of the same card in player ones deck, then he colleccts those four and puts them away.
# 7. this game goes till there are no more cards
# 8. 
# 9. 



"""
    OOP Card Game Hackathon
    open terminal -> cd to dir where your py file is
    open shell by typing python or python3 on mac
    from name_of_file import *
    now you can execute functions / use vars from file in shell
    Starting code:
"""