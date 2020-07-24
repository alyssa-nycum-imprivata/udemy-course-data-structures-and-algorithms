s = "This is the best"

def rev_word1(s):
    print(" ".join(reversed(s.split())))

rev_word1(s)

def rev_word2(s):
    print(" ".join(s.split()[::-1]))

rev_word2(s)

def rev_word3(s):

    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            
            words.append(s[word_start:i])

        i += 1

    print(' '.join(reversed(words)))

rev_word3(s)


