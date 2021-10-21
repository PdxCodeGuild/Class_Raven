'''average a list of numbers'''

#making function to add the list
# def average(number):
#     count = 0
#     for num in nums:
#         count += num
#     return count

#list of numbers
nums = [5, 0, 8, 3, 4, 1, 6]

#calling function to see math
# print (average(nums))




#iterate through the list
""" for num in nums:
    count = 0
    for num in nums:
        count += num """
#this works properly

""" print(count)

#now divide by the number of elements in list
average = count / len(nums)
#this prints the result of that math
print(average) """

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
            print(average)
            break
    except ValueError:
            print("That's not a valid imput. Try again.")

