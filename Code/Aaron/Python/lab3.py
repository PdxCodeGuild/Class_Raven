nums = [5, 0, 8, 3, 4, 1, 6]

# initialize a variable to hold the 'running sum'
total = 0

# iterate through the list keeping a 'running sum'
for num in nums:
    total = total + num

# get the average
average = total / len(nums)

# print average rounded to two decimal places
print("Average:", round(average))