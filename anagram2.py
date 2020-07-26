word_list = ["Halsey", "tac", "dog", "Clint Eastwood", "act", "God", "old west action", "Ashley", "cat", "hello"]

def anagram(word_list):

    word_dict = {}

    for word in word_list:
        key = ''.join(sorted(word.replace(" ", "").lower()))
        if key in word_dict.keys():
            word_dict[key].append(word)
        else:
            word_dict[key] = []
            word_dict[key].append(word)

    word_list = []

    for value in word_dict.values():
        word_list.append(value)

    print(word_list)

anagram(word_list)