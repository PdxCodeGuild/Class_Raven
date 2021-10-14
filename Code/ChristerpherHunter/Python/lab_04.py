# Christerpher Hunter
# Lab 02: Make Change 
# Formally Lab 04

# Convert input doll hairs into pennies
def make_pennies(doll_hairs: str) -> int:

    pennies = float(doll_hairs)
    pennies = pennies * 100
    return int(pennies)

# Coin vending tuple
""" coins = [
        ('Fifty Cent piece', 50)
        ('Quarter', 25)
        ('Dime', 10)
        ('Nickel', 5)
        ('Penny', 1)
    ] """

def make_change(pennies: int) -> int:

    # Make the number of Quarters
    quarters = pennies // 25

    # Make the number of Dimes
    pennies -= quarters * 25
    dimes = pennies // 10

    # Make the number of Nickels
    pennies -= dimes * 10
    nickels = pennies // 5

    # Make the number of Pennies
    pennies -= nickels * 5
    penny = pennies // 1

    return quarters, dimes, nickels, penny


def main() -> None:

    tendered = input("\nPlease input the amount tendered: ")
    tendered = make_pennies(tendered)
    quarters, dimes, nickels, pennies = make_change(tendered) # Overloading the variable pennies

    print(f"\nThe amount tendered creates:\n{quarters} Quarter(s)\n{dimes} Dime(s)\n{nickels} Nickel(s)\n{pennies} Pennie(s)")    


if __name__ == '__main__':
    main()