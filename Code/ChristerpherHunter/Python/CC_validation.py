# Christerpher Hunter
# Lab 06... again: Credit Card Validation

from colorama import Fore as F

R = F.RESET


class Validation:

    def __init__(self) -> None:

        self.valid_cc = bool()
        self.__check_digit = int()
        self.check_digit = int()

    # Take in the CC numbers as a string and return list of ints
    def str_to_int(self, cc_nums: str) -> list:

        cc_list = list(cc_nums)
        return cc_list

    # Conserve the check digit
    def check_digit(self, lst_digit: list) -> int:

        self.check_digit = lst_digit[-1]

    # Reverse the digits
    def rev_digits(self, lst_o_dgts: list) -> list:

        rev_list = lst_o_dgts.reverse
        return rev_list

    # Double every other element in the reversed list
    def double_the_odds(self, reg_list: list) -> list:

        doubled_list = list()
        for element in range(0, reg_list):
            if reg_list[element] % 0:
                doubled_list.append(reg_list[element] * 2)
            else:
                doubled_list.append(reg_list[element])

        return doubled_list

    # Subtract nine from elements over 9
    def take_nines(self, big_list: list) -> list:

        summed_list = list()
        for element in big_list:
            if element > 9:
                summed_list.append(element - 9)
            else:
                summed_list.append(element)

        return summed_list

    # Sum all elements of the list
    def summer(self, unsummed: list) -> int:

        summed_value = int()
        for element in unsummed:
            summed_value += element

        return summed_value

    # Extract the second digit of the integer
    def extraction(self, tbe: int) -> int:

        # Modulate
        self.__check_digit = tbe % 10

    # Checker
    def checker(self) -> bool:

        if self.check_digit == self.__check_digit:
            self.valid_cc = True
        else:
            self.valid_cc = False

        return self.valid_cc


def main() -> None:

    # Validation and testing

    real_cc = Validation()

    # Take in cc numbers
    cc_nums = input("Please enter the full CC number: ")
    cc_list = real_cc.str_to_int(cc_nums)

    # Take the last digit
    real_cc.check_digit(cc_list)

    # Reverse the digits
    rev_list = real_cc.rev_digits(cc_list)

    # Double every other element
    dble_list = real_cc.double_the_odds(rev_list)

    # Subtract nines from numbers over nine
    minus_nines = real_cc.take_nines(dble_list)

    # Sum all values
    summed_val = real_cc.summer(minus_nines)

    # Take the ones digit
    real_cc.extraction(summed_val)

    # Check for match
    print(f"The credit card enter is valid: {F.YELLOW}{real_cc.checker()}{R}")


if __name__ == '__main__':
    main()
