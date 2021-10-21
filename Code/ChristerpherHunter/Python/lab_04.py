# Christerpher Hunter
# Lab 02: Make Change 
# Formally Lab 04

# Convert input doll hairs into pennies
def make_pennies(doll_hairs: str) -> int:

    pennies = float(doll_hairs)
    pennies = pennies * 100
    
    return int(pennies)

# Coin vending tuple
coins = [
        ('Fifty Cent piece', 50),
        ('Quarter', 25),
        ('Dime', 10),
        ('Nickel', 5),
        ('Pennie', 1)
    ] 

def make_change(pennies: int) -> int:

    # Make the number of Quarters
    quarters = pennies // coins[1][1]

    # Make the number of Dimes
    pennies -= quarters * coins[1][1]
    dimes = pennies // coins[2][1]

    # Make the number of Nickels
    pennies -= dimes * coins[2][1]
    nickels = pennies // coins[3][1]

    # Make the number of Pennies
    pennies -= nickels * coins[3][1]
    penny = pennies // coins[4][1]

    return quarters, dimes, nickels, penny


def main() -> None:

    tendered = input("\nPlease input the amount tendered: ")
    tendered = make_pennies(tendered)
    quarters, dimes, nickels, pennies = make_change(tendered) # Overloading the variable pennies

    print(f"\nThe amount tendered creates:\n\
{quarters} {coins[1][0]}(s)\n\
{dimes} {coins[2][0]}(s)\n\
{nickels} {coins[3][0]}(s)\n\
{pennies} {coins[4][0]}(s)")    


if __name__ == '__main__':
    main()