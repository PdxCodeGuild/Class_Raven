nums = [5, 0, 8, 3, 4, 1, 6]

sum = 0

for num in nums:
    sum += num
    print(sum)

list_length = len(nums)

average = sum/list_length

average = round(average, 2)

print(f'Average = {average}')




