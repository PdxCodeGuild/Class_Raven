print("Averaging Numbers") 

nums = [5, 0, 8, 3, 4, 1, 6]
denom =len(nums)
total = 0
for num in nums:
    total += num
    print(total)

average =total/denom
print(f"The average is {average}.")