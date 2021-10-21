"""
Author: Christerpher Hunter
PDX Code guild: Lab 11 ROT13 Cipher

Write a program that prompts the user for a string, and encodes it with ROT n.
For each character, find the corresponding character, add it to an output
string. Notice that there are 26 letters in the English language, so
encryption is the same as decryption.
"""


class ROTN:
    """Encode a string with a Rotation Cipher"""

    def __init__(self, message: str, rotation_num=13) -> None:

        self.message = message.lower().replace(" ", "")
        self.space_num = message.count(" ")
        self.rotation_num = rotation_num
        self.encrypted_message = str()
        self.decrypted_message = str()
        global ALPHABET
        ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z']

    def __str__(self) -> str:
        return self.encrypted_message

    def encrypt(self) -> None:
        """Encrypt the message based on the ROT number"""

        self.encrypted_message = map(ROTN.letters, self.message)

    def decrypt(self) -> None:
        """Decrypt the message based on the ROT number"""

        self.decrypted_message = "".join(map(ROTN.letters,
                                         (self.message, -self.rotation_num)))

    def letters(letter: str, rotation=13) -> str:
        """Takes in a letter and rotation val and returns rotated value"""

        letter_val = [num for num, letters in enumerate(ALPHABET, start=1)
                      if letter == letters].pop()
        letter_val += rotation
        letter_val = [letters for num, letters in enumerate(ALPHABET * 2,
                      start=1) if num == letter_val]

        return letter_val


def main() -> None:

    message = "hello world"
    secret = ROTN(message, 13)
    secret.encrypt()
    word = [i for i in secret.encrypted_message]
    print(real_word)


if __name__ == "__main__":
    main()
