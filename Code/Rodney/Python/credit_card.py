def multiplier(list_to_be_doubled):
    ## this function will take a list of numbers and double every other number
    for n in range(len(list_to_be_doubled)):
        if n % 2 == 0: ## if index value / 2 == 0, it's an even number and we will double that number
            list_to_be_doubled[n] = list_to_be_doubled[n]*2  #replacing original value in n index position with new value * 2
    return list_to_be_doubled  #returns the new list 

def subtract_nine(nines_list):
    ##  this function will look at every number in list over 9 and subtract 9 from that number 
    for idx, val in enumerate(nines_list): ## for the index and value of every number in the list, we will look at the value for each index 
        if val > 9: ## if statement to see if value is over 9
           nines_list[idx] = nines_list[idx] - 9  ## since we are still in for loop and at the same index as the number we are checking is over nine
    return nines_list                               ## we can replace that number at that index position with its value - 9

credit_card_num = input("Please enter your 16 digit credit card number:\n> ") ## input asking for credit card number
credit_card_num = credit_card_num.replace(' ', '') # removing spaces 
while len(credit_card_num) != 16:  ## if number user entered is not exactly 16, they will be asked to try again using while statement 
    credit_card_num = input("Invalid! Please enter 16 digit number:\n> ")
    credit_card_num = credit_card_num.replace(' ', '') 

credit_card_list = list(credit_card_num) # type casting user entered string into list of strings
new_credit_card_num_list = []
for number in credit_card_list:  ## now we can loop through that list and convert each string into an integer 
    number = int(number)
    new_credit_card_num_list.append(number)
check_digit = (new_credit_card_num_list)[15::] ## slicing using 15(start index), :(end index), :(increment...default is 1) to slice last number which is our check digit now 
new_credit_card_num_list = new_credit_card_num_list[:15:] ## using same method ## using same method to remove that last number from list 
new_credit_card_num_list.reverse() ## reversing the list 

doubled_list = multiplier(new_credit_card_num_list)  ## calling multiplier function to double every other number in list 
list_of_nines = subtract_nine(doubled_list) ## calling subtract_nine function to subtract each number over 9 by 9

sum = 0  ## setting sum at 0 so we can add up all numbers in list 
for number in list_of_nines:
    sum += number
sum = str(sum) # sum type casted into string, and then into list, so we can remove second digit with pop function 
sum = list(sum)
second_digit = sum.pop(1)

check_digit = check_digit.pop(0) ## using pop function again to quickly convert check digit (which is now a list) to a integer 
second_digit = int(second_digit) ## type casting to convert second digit to integer 

if check_digit == second_digit: ## if true that check_digit equals second_digit, print valid, if false, print invalid 
    print("Valid!")
else:
    print("Invalid!")
    