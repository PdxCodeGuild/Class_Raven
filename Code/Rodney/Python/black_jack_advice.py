

def acceptable_or_not(user_card, acceptable_user_values): 
    ## this function will return true if card number user enters is not valid 
    if user_card not in acceptable_user_values:
        return True 
    return False

def advise_user(first_card, second_card, third_card):
    ## this function will assign value to card user enters
    card_1_value = card_values.get(card_1)  ## using .get function to access card value library and the value attached to the key
    card_2_value = card_values.get(card_2)
    card_3_value = card_values.get(card_3)
    card_value_total = card_1_value + card_2_value + card_3_value  ## totals values up to provide user with total value of cards
    card_value_list = [card_1_value, card_2_value, card_3_value]
    for number in card_value_list:
        if card_value_total < 21:
            if number == 1:
                number = number + 9
                card_value_total = card_value_total + number
            if card_value_total > 21:
                card_value_total = card_value_total - number
                break
    print(f'\nTotal of your cards is: {card_value_total}\n') 
    outcome_list = ['Hit!', 'Stay', 'BlackJack!', 'Already Busted!']
    if card_value_total < 17: ## multiple if/elif statements that will return outcome from outcome list based on index we assign based on total card value 
        outcome = outcome_list[0]
    elif card_value_total >= 17 and card_value_total < 21:
        outcome = outcome_list[1]    
    elif card_value_total == 21:
        outcome = outcome_list[2]
    elif card_value_total > 21:
        outcome = outcome_list[3]    
    return outcome

card_values = {'A': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'Q': 10,'K': 10}
## dictionary of card values, card(key), integer(value)
while True:

    acceptable_user_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_1 = input("\nWhat's your first card?\n> ").upper()  ##asking user for card number, turning it into upper case if J Q K A
    while acceptable_or_not(card_1, acceptable_user_values) == True:  ## while user entry not in acceptable list, call acceptable or not function, pass card and acceptable values as arugments 
        card_1 = input("Invalid entry, what's your first card?\n> ").upper()
    card_2 = input("What's your second card?\n> ").upper()
    while acceptable_or_not(card_2, acceptable_user_values) == True:
        card_2 = input("Invalid entry, what's your second card?\n> ").upper()
    card_3 = input("What's your third card?\n> ").upper()
    while acceptable_or_not(card_3, acceptable_user_values) == True:
        card_3 = input("Invalid entry, hat's your third card?\n> ").upper()
    user_advice = advise_user(card_1, card_2, card_3)
    print(user_advice)
    try_again = input("\nWould you like to try again?\n> ")  ## since this is in while True loop, starts over if user enters yes when asked to try again 
    if try_again == 'yes':
        continue
    else:
        break
