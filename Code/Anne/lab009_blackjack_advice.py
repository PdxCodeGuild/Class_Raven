# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
card = 0
hand = []
while card < 3:
    user_card = input("what card did you draw? ")
    hand.append(user_card)
    card +=1
print(hand)
sum = 0
# Then, figure out the point value of each card individually
card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10}
# use a dictionary
for card in hand:
    value = card_value.get(card)
    sum = sum + value
if sum < 17:
    print(f" Your sum is {sum} - Hit")
elif sum <= 17 and sum <21:
    print(f" Your sum is {sum} - Stay")
elif sum == 21:
    print(f" Your sum is {sum} - Blackjack!")
elif sum > 21:
    print(f" Your sum is {sum} - Already Busted!")
# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
