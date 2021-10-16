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

    print(" " * 14 + "x" + " " * 5 + "x")  # 9 High
    print(" " * 13 + "x" * 3 + " " * 3 + "x" * 2)  # 8 High
    print(" " * 5 + "x" + " " * 6 + "x" * 5 + " " + "x" * 3)  # 7 High
    print(" " * 5 + "x" * 3)  # High 6


def main() -> None:

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    # val = peaks(data)
    # val2 = valleys(data)

    peaks_and_valleys(data)

    # print(val, val2)


if __name__ == "__main__":
    main()
