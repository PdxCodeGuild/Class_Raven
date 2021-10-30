'''Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

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
Valid!'''
#Ask for an input card numbers
value = input('Enter number: ')
#Establish a list for the card numbers
card_list = []
#Input is a string, need to convert it to int and append to card_list
for char in value:
    card_list.append(int(char))
#Extract the last card number and save as a variable
last_card_number =card_list[-1]
#Remove the last card number from the list
card_list.pop()
#card_list.reverse()
#Extract the odd index numbers in reverse order into a new list
odd_card_list=card_list[::-2]
#Extract the even index numbers in reverse order into another list
even_card_list=card_list[-2::-2]
#Establish a list for results of calculations
calculated_list = []
#Build a variable to store the results of the final list calculation
total=0
#Construct for loop for the odd index numbers
for x in odd_card_list:
    #Build formula to double the odd index numbers
    double = x * 2 
    #Nested if statement to identify doubled numbers above 9
    if double > 9:
        #Complete the formula for the doubled numbers above 9
        double = double - 9
    #Append the doubled numbers to the calculated_list
    calculated_list.append(double)
#Construct for loop for the even index numbers
for y in even_card_list:
    #Append the numbers to the calculated_list to complete the merge
    calculated_list.append(y)
#Construct a final for loop on the calculated_list to sum it all up
for z in calculated_list:
    total = total + z
#Modulus to pull out the last digit
last_digit = total % 10
#Compare the last digit to the last_card_number to id a match
if last_digit == last_card_number:
    #If it's a match print valid
    print("Card is valid")
else:
    #If not a match print invalid
    print("Card is invalid")
#print(last_digit)
#print(last_card_number)
#print(odd_card_list)
#print(even_card_list)
#print(calculated_list)
#print(total)




