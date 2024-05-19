
sentence = "An apple a day keeps doctor away"

def longest_word_length(sentence):
    words = sentence.split()
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    
    return length


print(longest_word_length(sentence))
    

