# LAB 02: Make Change 
# Version 1
# Rafael Medina



while True:
    user_input = float(input("Enter a dollar amount: "))
    if user_input >= 0:
        user_input = user_input * 100 # input dollar to pennies
        quarter = int(user_input // 25)  # // floor division with float input and int output
        user_input = user_input % 25
        dime = int(user_input // 10)
        user_input = user_input % 10
        nickel = int(user_input // 5)
        user_input = user_input % 5
        pennies = int(user_input // 1)
        user_input = user_input % 1
    if user_input >= 0:    # breaks the while loop when all the change is eliminated
        break


print('\n', quarter, "quarters", dime, "dimes", nickel, "nickels", pennies, "pennies\n" )


