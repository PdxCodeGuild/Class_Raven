



def card_checker():
    card_number = input('Please enter your credit card number : ')
    #remove spaces
    card_number = card_number.replace(" ", "")
    #convert to a list of ints
    card_num_list= list(card_number)
    for i in range(0, len(card_num_list)):
        card_num_list[i] = int(card_num_list[i])
    #print(type(card_num_list[1])) works!
    # print(card_num_list) #verify full list 
    #slice of last digit = check digit
    check_digit = card_num_list.pop()
    # print(type(check_digit)) int
    check_digit = str(check_digit)
    print(check_digit)
    #print(type(check_digit)) fixed
    print(card_num_list)

    #print(check_digit) works!
    #print(card_num_list) verify last digit gone
    #reverse the digits
    card_num_list.reverse()
    print(card_num_list) #works
    doubled_card_num_list = []
    #double (as in num * 2) every other element in the reversed list
    for i in card_num_list:
        if i % 2 == 1:
            doubled_card_num_list.append(i * 2)
        else:
            doubled_card_num_list.append(i)
    print(f' this is the doubled card num list : {doubled_card_num_list}')
    #subtract 9 from all numbers over 9 
    sub_9_list = []
    for i in doubled_card_num_list:
        if i >9:
            sub_9_list.append(i-9)
        else:
            sub_9_list.append(i)

    print(f'this is the sub 9 list{sub_9_list}') #works!
    #sum all values
    the_sum = sum(sub_9_list)
    print(f'this is the sum: {the_sum}')
    #print(type(the_sum)) #adds up!
    the_sum = str(the_sum)
    print(the_sum[1])
    print(check_digit)
    #check that the second digit of that sum matches the check digit. 
    #get the second digit out 
    if (the_sum[1]) == (check_digit):
        print("the card is valid!")
    else:
        print('The card is not valid')
card_checker()
