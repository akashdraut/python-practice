
from functools import reduce

def is_palindrome(string):
    rev_str = reduce(lambda x, y: y + x, string)

    if rev_str == string:
        return True
    return False


str = input("Enter string value: ")
print(is_palindrome(str))



def is_palindrome(string):
    rev_str = ''
    for char in string:
        rev_str = char + rev_str

    if rev_str == string:
        return True
    return False


str = input("Enter string value: ")
print(is_palindrome(str))


