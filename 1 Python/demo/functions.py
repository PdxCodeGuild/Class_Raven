

# Built in functions
# print("Some message")
# input("Some prompt")
# int("4")
# float()
# str()
# list()
# sum(4, 5, 6)



# def speak_message(note):
#     print(note)



# speak_message("Happy Monday!")
# speak_message("Coding is fun")
# speak_message("Funfun functions")



# def get_unit_length(message):
#     while True:
#         unit = input(message)
#         try:
#             unit = int(unit)
#             break
#         except ValueError:
#             print("invalid input")

#     return unit

# lower_char = get_unit_length("Enter the lower characters: ")

# upper_char = get_unit_length("Enter the upper characters: ")

# digits = get_unit_length("Enter the digits: ")

# special_char = get_unit_length("Enter the special characters: ")

# print(lower_char, upper_char, digits, special_char)



# def add(num1=1, num2=1):
#     result = num1 + num2
#     return result


# print(add(num2=4, num1=8))




def greeting(message="Hello World", number=1):
    # repeat given message n number of times
    print(message * number)

    return True


print(greeting())