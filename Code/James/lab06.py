""" credit card validation """

def credit_card_validation():
     #user input divided by spaces
     user_input = list(int(num) for num in input("Enter your numbers seperated by space: \n>>> ").strip().split())
     user_input2 = ' '.join(str(n) for n in user_input)
     print(user_input2)
     #storing the check digit with the pop method.
     check_digit = user_input.pop(-1)
     #adding back the check digit because .pop returns new list
     add_back = user_input.append(check_digit)

     #print(check_digit)



     #slicing off that last digit and storing in sliced list
     sliced_list = user_input[:-1] # need to store the sliced digit in a variable
     user_input2 = ' '.join(str(n) for n in sliced_list)
     print(user_input2)
     #print(user_input[:-1])

     sliced_list.reverse()
     #print(sliced_list)


     #doubling every 2nd iterable in the list
     doubled_list = [n * 2 if index % 2 == 0 else n for index, n in enumerate(sliced_list)]
     user_input2 = ' '.join(str(n) for n in doubled_list)
     print(user_input2)

     #trying to subtract 9 from a every number above 9
     subtract_list = [n - 9 if n > 9 else n for n in doubled_list]
     user_input2 = ' '.join(str(n) for n in subtract_list)
     print(user_input2)

     total_list = sum(subtract_list)
     print(total_list)

     #converting to str so I can call the value of the 2nd position in the integer
     second_digit = str(total_list)
     print(second_digit[1])

     #converting back to an integer
     back_int = int(second_digit[1])

     # confirming the credit card.
     if back_int == check_digit:
          print('Valid!')
     else:
          print('Not Valid!')
credit_card_validation()

