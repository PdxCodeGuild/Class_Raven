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

    def get_text(self) -> None:
        """Retrieve the text"""

        self.texts = get('https://www.gutenberg.org/files/62897/62897-0.txt')
        self.texts.encoding = "utf-8"

    def create_text(self) -> None:
        """Create the text file"""

        with open("book_text.txt", 'w', encoding="utf-8") as file:
            file.write(self.texts)


def main() -> None:

    words = Count()
    words.get_text()
    words.create_text()


if __name__ == "__main__":
    main()
