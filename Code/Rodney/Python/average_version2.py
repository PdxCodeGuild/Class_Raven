

done = True  ## making done equal to boolean True to allow user to break out of while loop
nums = [] ##empty list of numbers that we can append user numbers to
sum = 0  ## 0 value for sum so we can continue to add numbers that user inputs

while done == True:  ## until user breaks loop by entering done (which causes boolean to be false), this loop will continue
    user_number = input("Please enter a number or 'done'\n> ")
    if user_number == 'done':
        done = False
    elif user_number != 'done':
        user_number = int(user_number) #type casting user entry into integer
        nums.append(user_number)  #appending user numbers to empty list 

length = len(nums) #obtaining length of list nums using len function 

for num in nums: ## for loop adding up numbers in nums list 
    sum += num

average = sum / length ## taking up sum of all numbers in list divided by length of the list

average = round(average) ## rounding average to nearest whole integer 

print(f'List of numbers: {nums}, sum of numbers: {sum}, average of numbers: {average}')



