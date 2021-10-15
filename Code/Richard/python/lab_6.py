print("Credit Card Validation")
def card_check(card):
    int(card)
    card_list = []
    card_l = list(card)
    for i in card_l:
        int(i)
        card_list.append(i)

    print(card_list)
    check_digit = card_list.pop()
    print(f"check digit is{check_digit}")
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
    Sum = sum(double_list2)
    Sum_list = list(Sum)
    if Sum_list[1] == check_digit:
        return True
    else:
         return False

test= "9875467834"
int(test)
card_check(test)