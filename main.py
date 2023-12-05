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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # initisl aaignment of deck


def card_nos(a):
    for i in range(1, 3):

        n = random.randint(0, 12)
        if n == 0:
            if sum(a) <= 10:
                a.append(cards[n])

            else:
                n = 1
                a.append(cards[n])
        else:
            a.append(cards[n])
    return a


def card_add(a):  # additional card addition

    n = random.randint(0, 12)
    if n == 0:
        if sum(a) <= 10:
            a.append(cards[n])

        else:
            n = 1
            a.append(cards[n])
    else:
        a.append(cards[n])
    return a


def dealer_card(a):  # additonal card for dealer

    c = random.randint(0, 1)
    while c == 1:
        n = random.randint(0, 11)
        if n == 0:
            if sum(a) <= 10:
                a.append(cards[n])

            else:
                n = 1
                a.append(cards[n])
        else:
            a.append(cards[n])

        if sum(a) > 21:
            break
        if sum(a) in range(17, 22):
            break
    return a


def card_compare(a, b): #comparing cards
    if sum(a) > sum(b):
        print("You win 😁")

    elif sum(b) > 21:
        print("Opponent went over. You win 😁")
    elif sum(b) > sum(a):
        print("You lose 😤")
    else:
        print("Draw 🙃")


play = input("Do you want to play blackjack, if yes then press y else press n")
print(art.logo)
while play == "y":
    f = 0
    user = []
    dealer = []
    user = card_nos(user)
    dealer = card_nos(dealer)
    print("Your cards:", user, "current score:", sum(user))
    print("Computer's first card:", dealer[0])
    card = input("Type 'y' to get another card, type 'n' to pass:")
    while card == "y":
        user = card_add(user)
        print("Users current hand:", user, "Current Total", sum(user))
        print("Computer's first card:", dealer[0])
        if sum(user) > 21:
            print("You went over. You lose 😭")
            f = 1
            break
        card = input("Type 'y' to get another card, type 'n' to pass:")

    else:
        print("Your final hand:", user, "Your Final score :", sum(user))

    dealer = dealer_card(dealer)
    if f == 0:
        print("Dealer's final hand:", dealer, "Current Total", sum(dealer))
        card_compare(user, dealer)
    play = input("Do you want to play blackjack, if yes then press y else press n")
else:
    print("Game Session Finished")
