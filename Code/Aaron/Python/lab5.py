def palindrome(string):
    if(len(string) == 0):
        return string
    else:
        return palindrome(string[1:]) + string[0]

string1 = input("enter a word: ")
string = palindrome(string1)
# print(string1 + "is not a plalindrome")

if(string1 == string):
    print(string1 + " is a palindrome")
else:
    print(string1 + " is not a palindrome")