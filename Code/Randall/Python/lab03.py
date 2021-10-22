"""
numbers = [5, 0, 8, 3, 4, 1, 6]
length = len(numbers)
total = 0
sumtot = 0
for i in numbers:
    total += numbers[sumtot]
    sumtot += 1
average = total / sumtot
print(f"Average for the list of numbers provided is: {average}")
"""
#==========
#Version 2:
#==========

numbers = []

while True:
    user_num = input("Enter multiple numbers then type 'done' when finished: ")
    
    if user_num != 'done':
        numbers.append(int(user_num))
    else:
        add_num = len(numbers)
        
        total = 0
         
        start_val = 0

        for i in numbers:
            total += numbers[start_val]
            
            start_val += 1
        
        average = total/add_num
        print(f"Average for the numbers provided is: {average}")