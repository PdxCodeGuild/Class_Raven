""" Linear search """

user_input = int(input('Enter the number you want the index of: '))


def linear_search(nums, value):
    match = 'No match found'
    for i in range(len(nums)):
        if nums[i] == value:
            
            match = i 
    print(match)
    return match
nums = [1, 2, 3, 4, 5, 6, 7, 8]

linear_search(nums, user_input)


""" binary search """
  




