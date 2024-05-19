# Method 1:
str = input("Enter some string: ")
rev_str = "".join(reversed(str))
if str == rev_str:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")

# Method 2:
str = input("Enter some string: ")
rev_str = ""
for char in str:
    rev_str = char + rev_str
print("Given string is Palindrome") if str == rev_str else print("Given string is not Palindrome")

# Method 3:
str = input("Enter some string: ")
rev_str = str[::-1]
print("Given string is Palindrome") if str == rev_str else print("Given string is not Palindrome")

# Method 4:
from functools import reduce

str = input("Enter some string: ")
rev_str = reduce(lambda x, y:y + x, str)
print("Given string is Palindrome") if str == rev_str else print("Given string is not Palindrome")


