# Christerpher Hunter
# Lab 07: Peaks and Valleys

def peaks(data: list) -> list:

    lst = list()
    for i in range(len(data) - 1):
        if (data[i - 1] < data[i] and data[i + 1] < data[i]):
            lst.append(i)
        
    return lst


def valleys(data: list) -> list:

    lst = list()
    for i in range(len(data) - 1):
        if (data[i - 1] > data[i] and data[i + 1] > data[i]):
            lst.append(i)

    return lst


def peaks_and_valleys(data: list) -> list:

    lst = list()
    for i in range(len(data) - 1):
        if (data[i - 1] < data[i] and data[i + 1] < data[i]):
            lst.append(i)
        if (data[i - 1] > data[i] and data[i + 1] > data[i]):
            lst.append(i)
    lst.sort()
    return lst


def main() -> None:

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    val = peaks(data)
    val2 = valleys(data)

    val3 = peaks_and_valleys(data)

    print(f"Peaks: {val}\nValleys: {val2}\nPeaks and Valleys: {val3}")

    for i, val in enumerate(data):
        if val == 9:
            print(" " * 14 + "x" + " " * 6 + "x")
            



if __name__ == "__main__":
    main()
