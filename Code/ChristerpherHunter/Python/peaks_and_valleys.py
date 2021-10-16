# Christerpher Hunter
# Lab 07: Peaks and Valleys

def peaks(data: list) -> list:

    lst = list()
    for i, val in enumerate(data):
        if i == 6:
            lst.append(val)
        elif i == 14:
            lst.append(val)
    return lst


def valleys(data: list) -> list:

    lst = list()
    for i, val in enumerate(data):
        if i == 9:
            lst.append(val)
        elif i == 17:
            lst.append(val)
    return lst


def peaks_and_valleys(data: list) -> list:

    # for i, val in enumerate(data):

    print(" " * 48 + " x " + " o " * 5 + " x ")  # 9 High
    print(" " * 45 + " x " * 3 + " o " * 3 + " x " * 2)  # 8 High
    print(" " * 21 + " x " + " o " * 6 + " x " * 5 + " o " + " x " * 3)  # 7 High
    print(" " * 18 + " x " * 3 + " o " * 3 + " x " * 11)  # High 6
    print(" " * 15 + " x " * 5 + " o " + " x " * 12)  # High 5
    print(" " * 12 + " x " * 19)  # High 4
    print(" " * 9 + " x " * 20)
    print(" " * 6 + " x " * 21)  # High 2
    print(" " * 3 + " x " * 22)
    print("" + " x " * 23)


def main() -> None:

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    # val = peaks(data)
    # val2 = valleys(data)

    peaks_and_valleys(data)

    # print(val, val2)


if __name__ == "__main__":
    main()
