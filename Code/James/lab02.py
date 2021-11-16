#Value exception error.
while True:
    try:
        dollar_amount = float(input("Enter a dollar amount: "))
    except ValueError:
        print ("That's not a valid number. Try again.")
    else:
        break


#setting all the variables for the coins
quarters = .25
dimes = .1
nickels = .05
pennies = .01

#converting the dollar amount into coins with floor division. 
#then storing the result in remaining balance for the next floor division
convert_quarter = dollar_amount // quarters 
convert_quarter = int(convert_quarter)
remaining_balance = dollar_amount - (convert_quarter * quarters)

convert_dime = remaining_balance // dimes
convert_dime = int(convert_dime)
remaining_balance = remaining_balance - (convert_dime * dimes)

convert_nickel = remaining_balance // nickels
convert_nickel = int(convert_nickel)
remaining_balance = remaining_balance - (convert_nickel * nickels)

convert_pennies = remaining_balance // pennies
convert_pennies = int(convert_pennies)
remaining_balance = remaining_balance -(convert_pennies * pennies)

#was checking the math
'''print("convert quarter",convert_quarter)
print("convert dime",convert_dime)
print("convert nickels", convert_nickel)
print("convert pennies", convert_pennies)
print("remaining", remaining_balance)'''

#print result to terminal.
print(f"{convert_quarter} quarters, {convert_dime} dimes, {convert_nickel} nickels, {convert_pennies} pennies.")


