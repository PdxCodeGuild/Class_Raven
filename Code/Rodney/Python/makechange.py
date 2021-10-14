dollar_amount = input("please enter a dollar amount: ") #input function to obtain dollar amount from user

dollar_amount = float(dollar_amount) #turning that string into a float

quarter = 25.0  ## assigning values to various forms of currency
nickel = 5.0
penny = .01
dime = 10.0

total_pennies = dollar_amount/penny # obtaining total number of pennies (note that assigned .01 to penny vs whole numbers for other currencies to be able to compare whole numbers going fwd)

#print(total_pennies)

total_quarters = total_pennies//quarter  ## using floor division to obtain total times 25 goes into total pennies as a whole number

total_left_after_quarters = total_pennies - (quarter * total_quarters) ## taking that whole number * value of quarter and subtracting from total pennies to have remaining total pennies

total_dimes = total_left_after_quarters//dime  ## repeating the above two steps for dimes > nickels > and remaining is your pennies left over 

total_left_after_dimes = total_left_after_quarters - (10 * total_dimes)

total_nickels = total_left_after_dimes//nickel

total_pennies_output = total_left_after_dimes - (5 * total_nickels)


if total_quarters >= 1:            ## using if statement to avoid printing out currency if we don't need to 
    print(f'{total_quarters} quarter(s)')

#print(total_left_after_quarters)

if total_dimes >= 1:
    print(f'{total_dimes} dime(s)')

#print(total_left_after_dimes)

if total_nickels >= 1:
    print(f'{total_nickels} nickel(s)')

if total_pennies_output >= 1:
    print(f'{total_pennies_output} pennie(s)')
