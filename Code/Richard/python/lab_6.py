print("Credit Card Validation")
def card_check(card):
    #int(card)
    card_list = []
    card_L = list(card)
    card_list = [int(i) for i in card_L] # learned method in search for "list of str to int"
    check_digit = card_list.pop()
    card_list.reverse()
    double_list = []
    double_list2 = []
    for num in card_list:
        num += num
        double_list.append(num)   
    for i in double_list:
        if i > 9:
            i -= 9
            double_list2.append(i)
        else:
            double_list2.append(i)
    Sum = str(sum(double_list2)) # search for how to use sum function with lists.
    Sum_list = list(Sum)
    if int(Sum_list[1]) == check_digit:
        return True
    else:
        return False

test= input("input credit card number to be validated\n>")
if card_check(test) == True:
    print("True")
elif card_check(test) == False:
    print("False")