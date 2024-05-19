
str = 'akash raut dilip'

def remove_duplicate_chars(string):
    res = ''
    for i in string:
        if i not in res and i != ' ':
            res += i

    return res


print(remove_duplicate_chars(str))



