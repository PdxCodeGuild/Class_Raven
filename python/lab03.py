'''average a list of numbers'''


#list of numbers
nums = [5, 0, 8, 3, 4, 1, 6]

#calling function to see math
# print (average(nums))

_list = []


#i want to add the user input to the empty list
count = 0
while True:
    
    
    try:
        user_input = input("Enter a number or type done to quit: ")
        if user_input != 'done':
            user_input = float(user_input)
            _list.append(user_input)
            print(f"The numbers you entered are: {_list}")
        else:
            for num in _list:
                count += num
            average = count / len(_list)
            print(f'the average is {average}')
            break
    except ValueError:
            print("That's not a valid imput. Try again.")

