print("Averaging Numbers") 
'''
nums = [5, 0, 8, 3, 4, 1, 6]
denom =len(nums)
total = 0
for num in nums:
    total += num
    print(total)

average = total/denom
print(f"The average is {average}.")
'''

def av(nums):
    total = 0
    for num in nums:
        total += num
    denom = len(nums)
    return total / denom

try_again = True
denom = 0
nums = []
user = 0
while True:
    user = input("enter number or 'done' to quit:\n>" )
    if user == 'done':
        print(f"The average is {av(nums)}.")
        break
    else:
        user = int(user)
        nums.append(user)
        print(nums)
