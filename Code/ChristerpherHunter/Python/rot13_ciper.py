"""
Author: Christerpher Hunter
PDX Code guild: Lab 11 ROT13 Cipher

Write a program that prompts the user for a string, and encodes it with ROT n.
For each character, find the corresponding character, add it to an output
string. Notice that there are 26 letters in the English language, so
encryption is the same as decryption.
"""


class ROT13:
    """Encode a string with a Rotation Cipher"""

    def __init__(self, message: str, rotation_num=13) -> None:

        self.message = message.lower()
        self.rotation_num = rotation_num
        self.encrypted_message = str()

    def encrypt(self) -> None:
        """Encrypt the message based on the ROT number"""

        self.encrypted_message = [letter for letter in
                                  zip(self.message,
                                      ROT13.letters(letter, self.rotation))]  # Use map() or zip(); Not sure

    def decrypt(self) -> None:
        """Decrypt the message based on the ROT number"""

    def letters(letter: str, rotation: int) -> str:
        """Takes in a letter and rotation val and returns rotated value"""

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']

        letter_val = int([num for num, letters in enumerate(alphabet, start=1)
                          if letter == letters])
        letter_val += rotation
        letter_val = str([letters for num, letters in enumerate(alphabet,
                          start=1) if num == letter_val])

        return letter_val
