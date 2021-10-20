"""

Lab 6: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list.
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
    5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
    1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    85
    5
    Valid!


"""


def card_valid():
    #This While loop is just to check if the user entered an even number
    #Can still add something to make sure the number is not less than a certain number
    while True:
        user_card = input("Please enter your card number: ")
        
        user_card = list(user_card)
        elements = len(user_card)
        if elements % 2 != 0:
            #if the above line returns 1, then the number is not even.
            print("Too little or to many characters were entered, please try again\n")
            continue # this is just to keep looping the user through until they enter a even number
        else:
            break

    for i in range(elements):
        user_card[i] = int(user_card[i]) # this loop is just to convert the values of user_card into integers
        
    check = user_card[-1]
    user_card.pop() # could not figure out a way to use the slice method to grab the last value in a list so I just did what made sense and stored it first then popped it out
    user_card.reverse()
    elements = len(user_card) # have to reset the value of elements now that the original list is one element shorter
    x = 0 #this variable is going to be used to double every other value in the list
    total = 0 #this variable will be used later on to get the total sum of all values in the list

    while x < elements: # used this logic so that I dont get the idex not in range error
        user_card[x] = user_card[x] * 2
        x += 2 # this is how I am doubling every other value

    for i in range(elements):
        if user_card[i] > 9: #this is subtracting 9 from any values that are over 9 as a result of being doubled
            user_card[i] = user_card[i] - 9
        total += user_card[i]

    total = str(total) # this line and the line below is because Im lazy and did not feel like converting the total into a string then using a loop to type cast the values into a integer
    check = str(check)

    if total[1] == check: # this statement is just to compare the check number we stored earlier on with the total of all values in the list
        print("You entered a Valid card number")
    else: 
        print("You did not enter a Valid card number, sorry. ")
    
card_valid()