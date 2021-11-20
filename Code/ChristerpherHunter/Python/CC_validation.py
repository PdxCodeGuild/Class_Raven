# Christerpher Hunter
# Lab 06... again: Credit Card Validation

from colorama import Fore as F

R = F.RESET


class Validation:

    def __init__(self, credit_card_nums: str) -> None:

        # Security in mind for initialization variables
        self.valid_cc = bool()
        self.__init_check_digit = int()  # Private variable for the check digit
        self.__pulled_check_digit = int()  # The final digit to check against
        self.__credit_card_nums_str = credit_card_nums  # The CC numbers str
        self.__credit_card_nums = list()  # The credit card nums as an int list

    # Take in the CC numbers as a string and return list of ints
    def str_to_int(self) -> list:

        # Remove all spaces in entry
        temp = self.__credit_card_nums_str.replace(" ", "")

        # Make list of ints
        for i in temp:
            self.__credit_card_nums.append(int(i))

    # Conserve the check digit
    def check_digit(self) -> int:

        self.__pulled_check_digit = self.__credit_card_nums[-1]

        # Remove the last index of the list
        self.__credit_card_nums.pop(-1)

    # Reverse the digits
    def rev_digits(self) -> list:

        self.__credit_card_nums.reverse()

    # Double every other element in the reversed list
    def double_the_odds(self) -> list:

        temp = []
        for element in range(len(self.__credit_card_nums)):
            if element % 2 != 0:
                temp.append(self.__credit_card_nums[element])
            else:
                temp.append(self.__credit_card_nums[element] * 2)

        self.__credit_card_nums = temp.copy()

    # Subtract nine from elements over 9
    def take_nines(self) -> list:

        temp = list()
        for element in self.__credit_card_nums:
            if element > 9:
                temp.append(element - 9)
            else:
                temp.append(element)

        self.__credit_card_nums = temp[:]

    # Sum all elements of the list
    def summer(self) -> int:

        for element in self.__credit_card_nums:
            self.__init_check_digit += element

    # Extract the second digit of the integer
    def extraction(self) -> int:

        # Modulate
        self.__init_check_digit = self.__init_check_digit % 10

    # Checker
    def checker(self) -> bool:

        self.valid_cc = self.__pulled_check_digit == self.__init_check_digit
        return self.valid_cc

    def __str__(self) -> str:

        return str(self.valid_cc)


def main() -> None:

    # Validation and testing

    # Take in cc numbers
    cc_nums = input("\nPlease enter the full CC number: ")
    real_cc = Validation(cc_nums)
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
    print(f"\nThe credit card enter is valid:\
 {F.YELLOW}{real_cc.checker()}{R}")


if __name__ == '__main__':
    main()
