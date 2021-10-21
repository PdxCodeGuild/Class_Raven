import string

# # Version 1
# origin = input("Please enter the text you want to code//decode: ")
# origin = origin.lower()
# # print(origin)

# letter_string = string.ascii_lowercase
# cipher_list = list(letter_string)
# # print(cipher_list)
# for i in origin:
#     if i  in cipher_list:
#         start = cipher_list.index(i)
#         shift = start + 13
#         if shift > 25:
#             shift = shift - 26
#         new_char = cipher_list[shift]
#         print(new_char)
       
#     else:
#         print("Try again only using letters of the alphabet")

# version 2

origin = input("Please enter the text you want to code//decode: ")
rotation = input("choose the amount of rotation you would like using a one or two digit number: ")
rotation = int(rotation)
origin = origin.lower()
# print(origin)

letter_string = string.ascii_lowercase
cipher_list = list(letter_string)
# print(cipher_list)
for i in origin:
    if i  in cipher_list:
        start = cipher_list.index(i)
        shift = start + rotation
        if shift > 25:
            shift = shift - 26
        new_char = cipher_list[shift]
        print(new_char)
       
    else:
        print("Try again only using letters of the alphabet")