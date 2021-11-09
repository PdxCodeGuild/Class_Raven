# Blackjack advice. Should you stay or hit? 

card = 0
hand = []
deck = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q']
card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10}
while card < 3:
    user_card = input("what card did you draw? ")
    if user_card not in deck:
        print('Not a valid card')
        break
    hand.append(user_card)
    card +=1
print(hand)
sum = 0
card_value = {'A':0, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10}
for card in hand:  
    value = card_value.get(card)
    sum = sum + value
    
if "A" in card_value: 
    if sum <= 10:
        sum = sum + 11
else:
    sum = sum + 1 
if sum < 17:
    print(f" Your sum is {sum} - Hit")
elif sum >= 17 and sum <21:
    print(f" Your sum is {sum} - Stay")
elif sum == 21:
    print(f" Your sum is {sum} - Blackjack!")
elif sum > 21:
    print(f" Your sum is {sum} - Already Busted!")
