"""
Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
 First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
 Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
 At this point, assume aces are worth 1. Use the following rules to determine the advice:

    Less than 17, advise to "Hit"
    Greater than or equal to 17, but less than 21, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both cards over 21. 
Remember that you can have multiple aces in a hand. 
 ** YOU CAN HAVE ONE ACE = 11 AND THE OTHER ACE = 1 **

Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace.
For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.



"""
from time import sleep
card_values = {

    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9

}
#Version 1
"""def blackjack():
    points = 0
    user_cards = []
    print("Please give me your 3 cards, (Your only options are 2-9 and A,K,Q, and J.)") # did it this way to match the lab example
    user_cards.append(input("Please enter your first card: ").upper())
    user_cards.append(input("Please enter your 2nd card: ").upper())
    user_cards.append(input("Please enter your 3rd card: ").upper())
    
    for i in user_cards:
            if i in card_values:
                points += card_values[i] # this loop is just going to add the value of card_values[i] to points for each card the user gives us.
            else:
                print("You entered a Invalid Card, Game will now end") # this is just input validation, Since BlackJack has the same cards everytime, We can just check if the user entered an actual card
                exit()
    return points

def advice(points):
    sleep(1) # just wanted to try this out
    if points < 17:
        print("\nHit")
    elif points >= 17:
        print("\nStay")
    elif points == 21:
        print("\nBlackJack!")
    elif points > 21:
        print("\nAlready busted")
    

while True: # made this into a REPL to flesh out the program a bit
    advice(blackjack())
    answer = input("Do you want to play again? Please type 'yes' or 'no: ")
    if answer == 'no':
        print("Thanks for playing")
        break"""

#Version 2

def blackjack():
    points = 0
    user_cards = []
    aces = 0
    print("Please give me your 3 cards, (Your only options are 2-9 and A,K,Q, and J.)")
    user_cards.append(input("Please enter your first card: ").upper())
    user_cards.append(input("Please enter your 2nd card: ").upper())
    user_cards.append(input("Please enter your 3rd card: ").upper())
    
    for i in user_cards:
        if i == 'A':
            user_cards.remove('A') # using remove because it only remove the first instance of 'A'
            break # Put a break because if the user has more than 1 ace it will loop and remove it again
    for i in user_cards: # If the user does not have any Aces, this is the loop that will run.
        if i in card_values:
            points += card_values[i]
        else:
            print("You entered a Invalid Card, Game will now end")
            exit()
    if points <= 10 and len(user_cards) == 2: # Added the second argument because the 11 or 1 was getting added even if the user had no aces.
        points += 11 # this is making the ace we remove earlier into the value 11
    elif points > 10 and len(user_cards) == 2:
        points += 1
    return points

def advice(points):
    sleep(1)
    print(points)
    if points < 17:
        print("\nHit")
    elif points >= 17 and points < 21:
        print("\nStay")
    elif points == 21:
        print("\nBlackJack!")
    elif points > 21:
        print("\nAlready busted")
    

while True:
    advice(blackjack())
    answer = input("Do you want to play again? Please type 'yes' or 'no: ")
    if answer == 'no':
        print("Thanks for playing")
        break
