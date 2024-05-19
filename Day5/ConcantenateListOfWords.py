
list_of_words = ["An", "apple", "a", "day", "keeps", "doctor", "away"]

def concatenate_words(list):
    sentence = " ".join(list_of_words).strip()
    return sentence


print(concatenate_words(list_of_words))

