
string = 'akash'

def count_chars(strnig):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


print(count_chars(string))

