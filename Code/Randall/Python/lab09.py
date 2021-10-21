# Blackjack Advice

card_dic = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
first_card = input('What is your first card? > ').upper()
second_card = input('What is your second card? > ').upper()
third_card = input('What is your third card? > ').upper()

def dr_facilier(first_card,second_card,third_card):

    list_cards = [first_card,second_card,third_card]

    card_sum = card_dic[first_card] + card_dic[second_card] + card_dic[third_card]

    while card_sum > 21 and 'A' in list_cards:
        print('A reduce to 1')
        card_sum = card_sum - 10

    print(card_sum)

    def check_hand(card_sum):
        if card_sum < 17:
            advice = 'Hit! Else, game over'
            return advice
        elif card_sum >= 17 and card_sum < 21:
            advice = 'Stay'
            return advice
        elif card_sum == 21:
            advice = "Blackjack!"
            return advice
        elif card_sum > 21:
            advice = "Busted!"
            return advice
        else:
            print("somethin went wrong")

    advice = check_hand(card_sum)
    return advice

print(dr_facilier(first_card,second_card,third_card))