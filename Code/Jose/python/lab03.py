number_list = []

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

while True:
    number = input("Enter a number or 'done' to quit: ")
    number_list.append(number)

    if number == 'done':
        del number_list[-1]
        for i in range(0, len(number_list)):
            number_list[i] = int(number_list[i])
        break

print(f"You entered {number_list}")

sum_numbers = sum(number_list)
print(f"The sum of the numbers is: {sum_numbers}")

amount_of_characters = len(number_list)
average = sum_numbers / amount_of_characters
print(f"Average: {average}")