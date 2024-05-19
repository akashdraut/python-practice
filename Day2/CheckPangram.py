import string

str = input("Enter string value: ")
clean_str = ''.join(char.lower() for char in str if char.isalpha())
unique_chars = set(clean_str)

alphabets = set(string.ascii_lowercase)
if unique_chars == alphabets:
    print("It is Pangram string")
else:
    print("NOT")



