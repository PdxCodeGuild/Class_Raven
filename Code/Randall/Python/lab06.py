#Lab 6: Credit Card Validation

def card_validator(cc_num):
    while True:
        try:
            card_int = int(cc_num)
            break
        except ValueError:
            return 'Invalid card number'

    card_list = list(cc_num)
    num_list = []

    for n in card_list:
        num_list.append(int(n))

    check_dig = num_list[-1]
    print(check_dig)
    num_list.pop()
    num_list.reverse()
    list_doubled = [num_list[n] * 2 if n % 2 == 0 else num_list[n] for n in range(len(num_list))]
    list_sub_nine = [n - 9 if n > 9 else n for n in list_doubled]
    sum_list = sum(list_sub_nine)
    list_sum_list = list(str(sum_list))

    if int(list_sum_list[1]) == check_dig:

        return 'Valid Card Number'
    else:
        return 'Invalid Card Number'

print(card_validator('123456987541511'))

   
