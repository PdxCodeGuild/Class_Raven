# Lab 03: Average Numbers
# Version 1
"""
# I have 3 ways to get the same solution below;
numbers = [5, 0, 8, 3, 4, 1, 6]
average = sum(numbers) / len(numbers)

print(average) # average of numbers list is 3.857142857142857
"""
"""
numbers = [5, 0, 8, 3, 4, 1, 6]
sum = 0
for i in numbers:
    sum = sum + i
average = sum / len(numbers)

print(average)
"""
"""
numbers = [5, 0, 8, 3, 4, 1, 6]
for i in range(len(numbers)):

    print(numbers[i])
"""
# Lab 03: Average Numbers
# Version 2

numbers = []

def average_list(list):

        num = 0
        for integers in list:

            num += integers

        return num

while True:

    user_input = input("\nenter a number, or 'done': ") 

    if user_input == 'done':

       answer = average_list(numbers)
       average = sum(numbers) / len(numbers)

       print('you entered ',(numbers), ", the average is: ", round(average, 3),'\n')      
      
       break

    elif user_input  != 'done':
    
        user_input = int(user_input) #if not converted to an integer, error!
        numbers.append(user_input) 


#this will print only the 2 digits after decimal..  round(round(average, 2)
