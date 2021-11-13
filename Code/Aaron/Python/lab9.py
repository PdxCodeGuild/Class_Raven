# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!


card_1 = input("What's your first card?: ").upper()

total = 0

if card_1 == "2":
    total += 2
elif card_1 == "3":
    total += 3
elif card_1 == "4":
    total += 4
elif card_1 == "5":
    total += 5
elif card_1 == "6":
    total += 6
elif card_1 == "7":
    total += 7
elif card_1 == "8":
    total += 8
elif card_1 == "9":
    total += 9
elif card_1 == "10":
    total += 10
elif card_1 == "J":
    total += 10
elif card_1 == "Q":
    total += 10
elif card_1 == "K":
    total += 10
elif card_1 == "A":
    total += 1

card_2 = input("What's your second card?: ").upper()


if card_2 == "2":
    total += 2
elif card_2 == "3":
    total += 3
elif card_2 == "4":
    total += 4
elif card_2 == "5":
    total += 5
elif card_2 == "6":
    total += 6
elif card_2 == "7":
    total += 7
elif card_2 == "8":
    total += 8
elif card_2 == "9":
    total += 9
elif card_2 == "10":
    total += 10
    if card_1 == "A":
        total = 21
elif card_2 == "J":
    total += 10
    if card_1 == "A":
        total = 21
elif card_2 == "Q":
    total += 10
    if card_1 == "A":
        total = 21
elif card_2 == "K":
    total += 10
    if card_1 == "A":
        total = 21
elif card_2 == "A":
    if card_1 == "A":
        total += 1
    else:
        total += 11


if total == 21:
    print("21 Blackjack")
    exit()
elif total >= 17:
    print(f"{total} Stay!")
    exit()
elif total <= 16:
    print(f"{total} Hit!")


card_3 = input("What's your third card?: ").upper()

if card_3 == "2":
    total += 2
elif card_3 == "3":
    total += 3
elif card_3 == "4":
    total += 4
elif card_3 == "5":
    total += 5
elif card_3 == "6":
    total += 6
elif card_3 == "7":
    total += 7
elif card_3 == "8":
    total += 8
elif card_3 == "9":
    total += 9
elif card_3 == "10":
    total += 10
elif card_3 == "K":
    total += 10
elif card_3 == "Q":
    total += 10
elif card_3 == "J":
    total += 10
elif card_3 == "A":
    if total <= 10:
        total += 11
    else:
        total += 1


if total == 21:
    print("21 Blackjack")
    exit()
elif total == range(17, 22):
    print(f"{total} Stay!")
    exit()
elif total <= 16:
    print(f"{total} Hit!")
else:
    print(f"{total} Already Busted")

# print(total)
