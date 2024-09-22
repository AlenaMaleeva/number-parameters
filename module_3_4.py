def single_root_words (root_word, *other_words):
    same_words= []
    for upper_word in root_word:
        upper_word = root_word. upper(), root_word.lower()

    for words in other_words:
        if root_word.startswith(words) or words.startswith(upper_word):
            
                same_words.append(words)
                return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

