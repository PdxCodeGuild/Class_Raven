# initialze a list to hold user input
nums = []

while True:
    
    # get input from user
    value = input("enter a number, or 'done':")
    
    if value == 'done':
        
        # initialize a variable to hold the 'running sum'
        total = 0

        # iterate through the list keeping a 'running sum'
        for num in nums:
            total = total + num

        # get the average
        average = total / len(nums)

        # print average rounded
        print("Average:", round(average))
        
        break
        
    else:
        # change input from string to int
        value = int(value)
        
        # add input to running total
        nums.append(value)