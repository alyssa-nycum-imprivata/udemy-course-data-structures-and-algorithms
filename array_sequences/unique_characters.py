def uni_char(s):
    return print(len(set(s)) == len(s))

uni_char('abcde')
uni_char('abcdeabc')
uni_char('123456')
uni_char('1234561')

def uni_char2(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return print(False)
        else:
            chars.add(letter)
    return print(True)

uni_char2('abcde')
uni_char2('abcdeabc')
uni_char2('123456')
uni_char2('1234561')