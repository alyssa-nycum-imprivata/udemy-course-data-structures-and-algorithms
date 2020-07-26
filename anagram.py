def anagram(s1,s2):

    # remove whitespace and lowercase letters
    new_s1 = s1.replace(' ', '').lower()
    new_s2 = s2.replace(' ', '').lower()

    if sorted(new_s1) == sorted(new_s2):
        return print(True)
    else: 
        return print(False)

anagram('god', 'dog')
anagram('clint eastwood', 'old west action')

def anagram2(s1,s2):

    # remove whitespace and lowercase letters
    new_s1 = s1.replace(" ", "").lower()
    new_s2 = s2.replace(" ", "").lower()

    # edge case check
    if len(new_s1) != len(new_s2):
        return print(False)
    
    count = {}

    for letter in new_s1:
        if letter in count:
            count[letter] += 1
        else: 
            count[letter] = 1

    for letter in new_s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return print(False)

    return print(True)

anagram2('god', 'dog')
anagram2('clint eastwood', 'old west action')