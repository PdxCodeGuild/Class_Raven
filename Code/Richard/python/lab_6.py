print("Credit Card Validation")
def card_check(card):
    #int(card)
    card_list = []
    card_L = list(card)
    card_list = [int(i) for i in card_L] # learned method in search for "list of str to int"
    '''for i in card_L:
        int(i)
        card_list.append(i)'''
    print(card_list)
    check_digit = card_list.pop()
    print(check_digit)
    print(card_list)
    card_list.reverse()
    print(card_list)
    double_list = []
    double_list2 = []
    for num in card_list:
        num += num
        double_list.append(num)
    print(double_list)    
    for i in double_list:
        if i > 9:
            i -= 9
            double_list2.append(i)
        else:
            double_list2.append(i)
    print(double_list2)
    Sum = str(sum(double_list2)) # search for how to use sum function with lists.
    print(Sum)
    Sum_list = list(Sum)
    print(Sum_list)
    if int(Sum_list[1]) == check_digit:
        print(True)
        return True
    else:
        print(False)
        return False

test= input("input credit card number to be validated\n>")
if card_check(test) == True:
    print("True")
elif card_check(test) == False:
    print("False")