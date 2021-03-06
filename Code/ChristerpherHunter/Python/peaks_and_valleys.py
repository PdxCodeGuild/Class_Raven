# Christerpher Hunter
# Lab 07: Peaks and Valleys

def peaks(data: list) -> list:

    lst = list()
    for i, val in enumerate(data):
        if i in [6, 14]:
            lst.append(val)
    return lst


def valleys(data: list) -> list:

    lst = list()
    for i, val in enumerate(data):
        if i in [9, 17]:
            lst.append(val)
    return lst


def peaks_and_valleys_water(data: list) -> list:

    # for i, val in enumerate(data):

    print(" " * 48 + " x " + " o " * 5 + " x ")  # 9 High
    print(" " * 45 + " x " * 3 + " o " * 3 + " x " * 2)  # 8 High
    print(" " * 21 + " x " + " o " * 6 + " x " * 5
          + " o " + " x " * 3)  # 7 High
    print(" " * 18 + " x " * 3 + " o " * 3 + " x " * 11)  # High 6
    print(" " * 15 + " x " * 5 + " o " + " x " * 12)  # High 5
    print(" " * 12 + " x " * 19)  # High 4
    print(" " * 9 + " x " * 20)
    print(" " * 6 + " x " * 21)  # High 2
    print(" " * 3 + " x " * 22)
    print("" + " x " * 23)


def peaks_and_valleys(data: list) -> list:

    # for i, val in enumerate(data):

    print(" " * 48 + " x " + "   " * 5 + " x ")  # 9 High
    print(" " * 45 + " x " * 3 + "   " * 3 + " x " * 2)  # 8 High
    print(" " * 21 + " x " + "   " * 6 + " x " * 5
          + "   " + " x " * 3)  # 7 High
    print(" " * 18 + " x " * 3 + "   " * 3 + " x " * 11)  # High 6
    print(" " * 15 + " x " * 5 + "   " + " x " * 12)  # High 5
    print(" " * 12 + " x " * 19)  # High 4
    print(" " * 9 + " x " * 20)
    print(" " * 6 + " x " * 21)  # High 2
    print(" " * 3 + " x " * 22)
    print("" + " x " * 23)


def main() -> None:

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    # There must be a more efficient method...
    peaks_and_valleys(data)
    print("\n\n")
    peaks_and_valleys_water(data)


if __name__ == "__main__":
    main()
