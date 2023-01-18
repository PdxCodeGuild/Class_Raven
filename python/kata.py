def duplicate_encode(word):
    s = ""
    for i in word.lower():
        if word.lower().count(i) < 2:
            s += ''.join('(')
        else:
            s += ''.join(')')
    print(s)
    return s
duplicate_encode('Success')