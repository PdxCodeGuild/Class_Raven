def ccValidation(credit_card):
    credit_card_numbers = [int(i) for i in credit_card]   # Using a list comprehension, we can convert the strings into integers, and puts it into a list by declaring the type using brackets
    print(f"1. {credit_card_numbers}") 

    check_digit = str(credit_card_numbers[-1])    # Storing the check digit somewhere else to use later
    del credit_card_numbers[-1]    # Deleting the check digit from the list
    print(f"2. {credit_card_numbers}")

    credit_card_numbers.reverse()    # Reverse the digits, updating the list and returning None
    print(f"3. {credit_card_numbers}")
    
    credit_card_numbers[0::2] = [i*2 for i in credit_card_numbers[0::2]]    # Every other integer in the list gets updated using slice (beggining, end, skip), grabs the specific amount to multiply using slice too.
    print(f"4. {credit_card_numbers}")

    for i in range(len(credit_card_numbers)):    # Iterates over all indices
        if credit_card_numbers[i] > 9:    # If the current index is higher than 9, subtract 9 from it
            credit_card_numbers[i] -= 9
    print(f"5. {credit_card_numbers}")

    sum_of_numbers = list(str(sum(credit_card_numbers)))   # Sum all numbers, convert to string, store into list, take second digit to compare to check_digit
    print(sum_of_numbers)
    if sum_of_numbers[1] == check_digit:
        return True
    else:
        return False




credit_card = input("Enter the credit card number: ")
credit_card.replace(" ", "")  # Remove spaces in case of any

if ccValidation(credit_card) == True:
    print("Valid! ")
else:
    print("Not a valid credit card. ")