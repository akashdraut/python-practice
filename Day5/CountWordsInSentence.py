
sentence = "An apple a day keeps doctor away"

def count_words(sentence):
    lst = sentence.split()
    return len(lst)


def count_words_in_sentence(sentence):
    word_count = 1
    for word in sentence:
        if word == " ":
            word_count += 1
    return word_count


print(count_words_in_sentence(sentence))

print(count_words(sentence))

