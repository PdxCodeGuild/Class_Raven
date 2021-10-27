def check_anagram(list_to_check) -> bool:
    sorted_strings = []
    for ana_string in list_to_check:  # Move through the list of strings.
        ana_string = list(ana_string)  # Convert string to a list.
        ana_string.sort()  # Sort the list by alphabetical order.
        sorted_strings.append("".join(ana_string))  # Convert list back to string
    for check_string in range(len(sorted_strings)):  # Check each sorted string.
        if (
            not sorted_strings[check_string] == sorted_strings[check_string - 1]
        ):  # If current string being checked does not match previous string then not anagram.
            return False
    return True


def get_list_of_words() -> list:
    add_another_word, list_of_strings = True, []
    while add_another_word:
        list_of_strings.append(
            input(
                f"Please enter a word to check if it is an anagram with other words.\n> "
            )
            .replace(" ", "")
            .lower()
        )  # Get user input, remove spaces. Change input to lowercase.
        if (
            list_of_strings[len(list_of_strings) - 1] == "!quit"
        ):  # Check if user typed "!quit"
            list_of_strings.remove(
                "!quit"
            )  # Remove "!quit" as it is not intended to be checked for anagram.
            add_another_word = False
    return list_of_strings


if __name__ == "__main__":
    list_to_check = get_list_of_words()
    if check_anagram(list_to_check):
        print(f"Your words {list_to_check} are an anagram!")
    else:
        print(f"Your words {list_to_check} are not an anagram!")
    print("\ngoodbye")  # Tell user goodbye.pyth
