"""
PDX Code Guild Full Stack Bootcamp
->Lab 02
  Make Change
Michael B
"""
coins = [
    ("One-Hundred dollar bill", 100),
    ("Fifty dollar bill", 50),
    ("Twenty dollar bill", 20),
    ("Ten dollar bill", 10),
    ("Five dollar bill", 5),
    ("One dollar bill", 1),
    ("half-dollar", 0.50),  # Who uses half-dollars anymore?
    ("quarter", 0.25),
    ("dime", 0.10),
    ("nickel", 0.05),
    ("penny", 0.01),
]

final_string = "\n"
plural = ""
number_invalid = True

while number_invalid == True:  # Try until valid number.
    try:  # Try to get valid input from user. (A float)
        total_ammount = float(
            input(
                f"""Please Enter how much money you have in dollars and cents (1.36):                                
"""
            )
        )  # Get input from user.
    except KeyboardInterrupt:  # Quit program on Ctrl+C
        print("Escaping program via KeyboardInterrupt")
        quit()
    except:  # Catch errors and help correct user and try again.
        print("Number is invalid, must be a float such as 1.36")
        number_invalid = True  # Set number_invalid to True so we try again.
    else:  # No issues.
        number_invalid = False

for coin in coins:  # Check each coin type
    if int(total_ammount // coin[1]) <= 1:  # If there is 1 or less coins.
        plural = ""
    else:  # There are multiple coins.
        plural = "s"
    if not total_ammount // coin[1] == 0:  # Print only what we have.
        final_string = (
            final_string
            + str(int(total_ammount // coin[1]))
            + " "
            + str(coin[0])
            + plural
            + " "
        )  # Create a string for output.
        total_ammount = total_ammount - coin[1] * (
            total_ammount // coin[1]
        )  # Reduce those coins before doing next coin type.

print(final_string)
