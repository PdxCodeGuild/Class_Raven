"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Lab 9
"""


def blackjack_score(user_card):
    """takes in user score and returns integer of the card's value"""
    user_card = user_card.upper()
    if user_card in all_cards:
        return all_cards[user_card]

def blackjack_advice(total):
    """Takes in total score and advices if user is bust, has blackjack, should stay, or should hit"""
    if total > 21:
        print(f"Your total is {total} - You're busted!\n")
    elif total == 21:
        print(f"Your total is {total} - Blackjack!\n")
    elif total >= 17 < 21:
        print(f"Your total is {total} - You should stay\n")
    elif total < 17:
        print(f"Your total is {total} - You should hit\n")
    return

def low_or_high(aces_low, aces_high):
    """Work in progress - this function will consider the aces high and aces low scores and return the ideal option for the user"""
    if aces_low or aces_high == 21:
        print('\nYour total is 21 - Blackjack!')
        return
    return

####################### INTERFACE ##############################################################
complete = False
while not complete:

  # Select Option 1-Blackjack Advice, 2-Exit, 3+ Try Again
  start = int(input(f'\nPlease select from the following options:\n 1. Blackjack Advice \n 2. Exit Program \n\n Enter the number of your choice: \n'))
  all_cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
  
  ace_high_score = 0

  ################### DIRECTORY ################################################################
  # Allow user to escape
  if start == 2:
    print(f"\nClosing application.\n")
    complete = True
    break

  if start > 2:
    print(f'\n Try again:\n')
    continue
  
  # Direct user to appropriate function: Select Option 1-Blackjack
  if start == 1:
    ace_counter = False
    ace_high_score = 0

    score_one = blackjack_score(input("Enter your first card: "))
    if score_one == 1:
        ace_high_score = 10
        ace_counter = True        

    score_two = blackjack_score(input("Enter your second card: "))
    if ace_counter == False:
        if score_two == 1:
            ace_high_score = 10
            ace_counter = True

    score_three = blackjack_score(input("Enter your third card: "))
    if ace_counter == False:
        if score_three == 1:
            ace_high_score = 10
            ace_counter = True

    print("\nIf you consider aces only low:")
    aces_low = blackjack_advice(score_one + score_two + score_three)

    print("If you one or more aces, those can be considered as an 11 score. This is your ace high score:")
    aces_high = blackjack_advice(score_one + score_two + score_three + ace_high_score)







    


