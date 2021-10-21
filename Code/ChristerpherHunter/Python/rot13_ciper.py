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

    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']

    decrypt_sig = bool()

    def __init__(self, message: str, rotation_num=13) -> None:

        self.message = message.lower().replace(" ", "")
        self.space_num = message.find(" ")
        self.rotation_num = rotation_num
        self.encrypted_message = str()
        self.decrypted_message = str()
        self.extra_val = str()

        for letter in message:
            if not letter.isalpha():
                self.extra_val = letter
                self.message = self.message.replace(letter, "")

    def __str__(self) -> str:
        return self.encrypted_message

    def encrypt(self) -> None:
        """Encrypt the message based on the ROT number"""

        self.encrypted_message = map(self.letters, self.message)
        self.encrypted_message = "".join("".join(i) for
                                         i in self.encrypted_message)
        self.encrypted_message = self.encrypted_message[0:self.space_num] +\
            " " + self.encrypted_message[self.space_num:] + self.extra_val

    def decrypt(self) -> None:
        """Decrypt the message based on the ROT number"""

        ROTN.decrypt_sig = True
        for letter in self.encrypted_message:
            if not letter.isalpha():
                self.encrypted_message = self.encrypted_message.\
                                         replace(letter, "")

        self.encrypted_message = self.encrypted_message.replace(" ", "")
        self.decrypted_message = map(self.letters, self.encrypted_message)

        self.decrypted_message = "".join("".join(i) for
                                         i in self.decrypted_message)
        self.decrypted_message = self.decrypted_message[0:self.space_num] +\
            " " + self.decrypted_message[self.space_num:] + self.extra_val

    def letters(self, letter: str) -> str:
        """Takes in a letter and rotation val and returns rotated value"""

        self.rotation_num = (-self.rotation_num if ROTN.decrypt_sig else
                             self.rotation_num)
        letter_val = [num for num, letters in enumerate(ROTN.ALPHABET, start=1)
                      if letter == letters].pop()
        letter_val += self.rotation_num if self.rotation_num > 0 else\
            abs(self.rotation_num)
        letter_val = [letters for num, letters in enumerate(ROTN.ALPHABET * 2,
                      start=1) if num == letter_val]

        return letter_val


def main() -> None:

    message = "Hello world!"
    secret = ROTN(message, 13)
    secret.encrypt()
    print(secret.encrypted_message)
    secret.decrypt()
    print("\n")
    print(secret.decrypted_message)


if __name__ == "__main__":
    main()
