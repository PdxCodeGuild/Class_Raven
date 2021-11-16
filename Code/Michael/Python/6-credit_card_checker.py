"""
PDX Code Guild Full Stack Bootcamp
->Lab 06
  Credit Card Validation
Michael B
"""
invalid_cc_number = True
cc_number_nined = []

while invalid_cc_number:
    cc_numbers = (
        input("Please enter a cc number seperated by spaces or commas: ")
        .replace(" ", "")
        .replace(",", "")
    )  # Removes spaces and commas.
    cc_numbers = list(cc_numbers)
    if len(cc_numbers) > 16:  # CC should be less than 16 characters.
        print("Too many digits.")
    elif len(cc_numbers) < 16:  # CC should be more than 16 characters.
        print("Too few digits.")
    else:  # Valid CC number.
        invalid_cc_number = False

check_digit = cc_numbers.pop(-1)  # Remove the last digit for validation.
cc_numbers.reverse()  # Reverse the CC numbers.

for number in range(0, len(cc_numbers)):
    cc_numbers[number] = int(cc_numbers[number])  # Convert list strs to ints.

for number in range(0, len(cc_numbers), 2):
    cc_numbers[number] *= 2  # Multiply every other number by 2.


for number in cc_numbers:
    if number > 9:  # Subtract nine from numbers over nine.
        cc_number_nined.append(
            number - 9
        )  # Place into new list because I had trouble figuring out how to do it in same list.
    else:
        cc_number_nined.append(number)

summed_cc = str(
    sum(cc_number_nined)
)  # Sum the list and convert sum to string to use as list.

print("Check Digits: ", summed_cc)
print("Comparative Digit: ", summed_cc[len(summed_cc) - 1])
print("Check Digit: ", check_digit)

if (
    check_digit == summed_cc[len(summed_cc) - 1]
):  # If check digit and comparitive digit match then valid.
    print(f"Your credit card is valid.")
else:
    print("Your credit card is not valid.")
