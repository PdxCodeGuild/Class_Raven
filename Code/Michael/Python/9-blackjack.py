"""
PDX Code Guild Full Stack Bootcamp
->Lab 09
  Black Jack Advice
Michael B

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

Aces can be worth 11 if they won't put the total point value of both cards over 21. 
Remember that you can have multiple aces in a hand. 
Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. 
For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
"""


def blackjack_advice() -> list:  # Get the advice.
    card_values = [
        ("A", 1),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
    ]  # List of card values.

    def get_user_cards() -> list:  # Get the user's cards.
        cards = []
        while len(cards) < 2:
            card = input("Enter a card: ").upper()  # Get the user's card.
            if card in [
                "A",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]:  # If the card is valid.
                cards.append(card)  # Add the card to the list.
        return cards

    def evaluate_cards(cards) -> list:  # Evaluate the cards.
        total = 0
        for card in cards:
            for value in card_values:  # value is a tuple.
                if card == value[0]:
                    if (
                        card == "A" and total <= 10
                    ):  # If the total is less than or equal to 10, the ace is worth 11.
                        total += 11
                    else:  # Otherwise, the ace is worth 1.
                        total += value[1]
        return total

    total = evaluate_cards(get_user_cards())
    if total < 17:  # Hit
        advice = "Hit"
    elif (
        total >= 17 and total < 21
    ):  # If the total is greater than or equal to 17, but less than 21, stay.
        advice = "Stay"
    elif total == 21:  # If the total is exactly 21, blackjack.
        advice = "Blackjack!"
    else:  # If the total is over 21, already busted.
        advice = "Already Busted :("
    return total, advice


if __name__ == "__main__":
    print(
        "You had %d. %s." % (blackjack_advice())
    )  # Print the total and advice formatted
