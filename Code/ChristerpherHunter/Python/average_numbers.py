# Christerpher Hunter
# Lab 03... again: Average Numbers

def average(nums: list) -> float:
    """Take in an integer list and return the average value of the elements"""

    sum = int()
    for i in nums:
        sum += i
    
    ave = sum / len(nums)

    return ave

def ave_ver2() -> float:

    user_num = str(0)
    num_list = list()
    while user_num.isnumeric():

        user_num = input("Please enter a number, or 'done': ")
        if user_num.isnumeric():
            num_list.append(int(user_num))
        else:
            val = int()
            for i in num_list:
                val += i
            ave = val / len(num_list)      
            return ave  


def main() -> None:

    nums = [5, 0, 8, 3, 4, 1, 6]

    print(average(nums))

    print(ave_ver2())

if __name__ == "__main__":
    main()
