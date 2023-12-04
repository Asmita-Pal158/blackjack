# Our Blackjack House Rules #####################

# The deck is unlimited in size. # There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:y

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
import random
import art


def card_nos(a):
    for i in range(1, 3):
        n = random.randint(0, 11)
        if n == 0:
            if sum(a) <= 10:
                n = 1
            else:
                n = 11
            a.append(n)
        else:
            a.append(n)
    return a
def card_add(a):
 n = random.randint(0, 11)
 if n == 0:
     if sum(a) <= 10:
         n = 1
     else:
        n = 11
        a.append(n)
 else:
        a.append(n)
 return a
def dealer_card(a):
    c = random.randint(0,1)
    while c == 1:
        n = random.randint(0, 11)
        if n == 0:
         if sum(a) <= 10:
          n = 1
         else:
          n = 11
          a.append(n)
        else:
          a.append(n)
        if sum(a)>21:
            break
    return a   
def card_compare(a,b) :
    if sum(a)>sum(b):
        print
        
        
play = input("Do you want to play blackjack, if yes then press y else press n")
while play == "y":
    f=0
    print(art.logo)
    user = []
    dealer = []
    card_nos(user)
    card_nos(dealer)
    print("Your cards:", user, "current score:", sum(user))
    print("Your cards:", dealer, "current score:", sum(dealer))
    card= input("Type 'y' to get another card, type 'n' to pass:")
    while card=="y":
        user= card_add(user)
        print("Users current hand:",user,"Current Total",sum(user))
        if sum(user)>21:
            print("You went over. You lose 😤")
            f=1
            break
        card= input("Type 'y' to get another card, type 'n' to pass:")
        
    else:
        print("Your final hand:",user,"Your Final score :",sum(user))
        
    dealer=dealer_card(dealer) 
    if f==0:
        card_compare(user,dealer) 
        
      
