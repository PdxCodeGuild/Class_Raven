def is_palindrome(letters, reversed):
    reversed.reverse()
    if letters == reversed:
        palindrome = 'is'
    else:
        palindrome = 'is not'
    return palindrome


def check_palindrome():
    letters = []
    reversed = []
    response = input('Enter a word: \n').lower()
    i = 0
    while len(response) > len(letters):
        letter = response[i]
        letters.append(letter)
        reversed.append(letter)
        i += 1
    palindrome = is_palindrome(letters, reversed)
    message = f'{response.capitalize()} {palindrome} a palindrome.'
    return message
