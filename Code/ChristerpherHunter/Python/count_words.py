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

    def get_text(self) -> None:
        """Retrieve the text"""

        self.texts = get('https://www.gutenberg.org/files/62897/62897-0.txt')
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
                      .replace("_", "")
                      .lower() for i in range((len(self.texts) // 1_000))]

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
        for i in range(min(10, len(intermediate_list))):
            self.top_ten.append(intermediate_list[i])

        return self.top_ten


def main() -> None:

    words = Count()
    # words.get_text()
    # words.create_text()
    words.open_text()
    words.make_list()
    words.make_dict()
    high_count = words.highest_count()
    print(high_count)


if __name__ == "__main__":
    main()
