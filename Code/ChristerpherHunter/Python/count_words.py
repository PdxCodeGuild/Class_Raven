"""
Christerpher Hunter
Lab 13: Count Words
Find a book on [Project Gutenberg](http://www.gutenberg.org) and
navigate to the plain-text version. You can then send a request to that
*url* using the `requests` library to get the text into Python. You can
also save the file into the same folder as the `.py` file and open it
using `with`.Find a book on [Project Gutenberg](http://www.gutenberg.
org) and navigate to the plain-text version. You can then send a
request to that *url* using the `requests` library to get the text into
Python. You can also save the file into the same folder as the `.py`
file and open it using `with`.
"""

from requests import get


class Count:
    """Count down to the number of letters a plain text"""

    def __init__(self) -> None:

        self.texts = None
        self.lists = list()
        self.count = int()
        self.dict_count = dict()
        self.top_ten = list()
        self.word_pick = str()

    def get_text(self) -> None:
        """Retrieve the text"""

        self.texts = \
            get('https://www.gutenberg.org/cache/epub/66595/pg66595.txt')
        self.texts.encoding = "utf-8"

    def create_text(self) -> None:
        """Create the text file"""

        with open("book_text.txt", 'w', encoding="utf-8") as file:
            file.write(self.texts.text)

    def open_text(self) -> str:
        """Open the text and work with it"""

        with open("book_text.txt", "r") as r_file:
            self.texts = r_file.read()

        return self.texts

    def make_list(self) -> list:
        """Make everything lowercase, strip punctuation, and split to a list"""

        self.lists = [self.texts
                      .split()[i]
                      .replace(";", "")
                      .replace(",", "")
                      .replace("'", "")
                      .replace("?", "")
                      .replace("!", "")
                      .replace(".", "")
                      .replace("*", "")
                      .replace("(", "")
                      .replace(")", "")
                      .replace("/", "")
                      .replace('"', "")
                      .replace("\\", "")
                      .replace("_", "")
                      .lower() for i in range((len(self.texts) - 1) // 100)]

        return self.lists

    def make_dict(self) -> dict:
        """Key is the word and the Value is the occurence"""

        for i in self.lists:
            self.dict_count[i] = self.lists.count(i)

        return self.dict_count

    def highest_count(self) -> list:
        """Return the top 10 highest count words"""

        intermediate_list = list(self.dict_count.items())
        intermediate_list.sort(key=lambda tup: tup[1], reverse=True)
        [intermediate_list.pop(i)
            for i in range(min(10, len(intermediate_list)))]

        if not self.word_pick:
            [self.top_ten.append(intermediate_list[i]
                                 if len(intermediate_list[i]) > 3 else
                                 intermediate_list[i + 1])
                for i in range(min(10, len(intermediate_list)))]
        else:
            [self.top_ten.append(intermediate_list[i]
                                 if intermediate_list[i] == self.word_pick else
                                 "Word not found")
                for i in range(min(10, len(intermediate_list)))]

        return self.top_ten

    def user_input(self) -> None:
        """Ask user input then match word for the count"""

        while not self.word_pick:
            self.word_pick = input("Enter a word to be matched and counted: ")


def main() -> None:

    words = Count()
    # words.get_text()
    # words.create_text()
    words.open_text()
    words.make_list()
    words.make_dict()
    words.user_input()
    high_count = words.highest_count()

    print(high_count)


if __name__ == "__main__":
    main()
