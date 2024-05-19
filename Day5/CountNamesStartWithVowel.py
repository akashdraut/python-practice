vowels = ['a', 'e', 'i', 'o', 'u']

list_of_words = ["An", "apple", "a", "day", "keeps", "doctor", "away"]

def count_words_starts_with_vowel(list):
    count = 0
    for word in list:
        if word[0].lower() in vowels:
            count += 1

    return count


print(count_words_starts_with_vowel(list_of_words))

