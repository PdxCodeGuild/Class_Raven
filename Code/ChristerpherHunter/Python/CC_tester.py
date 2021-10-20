# Christerpher Hunter
# Testing of the Credit Validation class

from CC_validation import Validation
import random
from colorama import Fore as F

R = F.RESET

stop = 1_000
go = 0
correct_count = 0

while go < stop:

    cc_nums = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
    random.seed(random.randint(0, 10_000_000_000))
    random.shuffle(cc_nums)
    class_feeder = str()
    # print(f"CC #'s: {cc_nums}")

    for val in cc_nums:
        class_feeder += str(val)

    # Take in cc numbers
    real_cc = Validation(class_feeder)
    real_cc.str_to_int()

    # Take the last digit
    real_cc.check_digit()

    # Reverse the digits
    real_cc.rev_digits()

    # Double every other element
    real_cc.double_the_odds()

    # Subtract nines from numbers over nine
    real_cc.take_nines()

    # Sum all values
    real_cc.summer()

    # Take the ones digit
    real_cc.extraction()

    # Check for match
    if real_cc.checker():
        # print(f"{F.GREEN}{real_cc.checker()}{R} {go}")
        correct_count += 1

    go += 1


print(f"Correct: {F.GREEN}{correct_count / stop}%{R} of {F.CYAN}{stop}{R}")
