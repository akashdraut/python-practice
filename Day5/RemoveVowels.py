
sentence = "An apple a day keeps doctor away"

vowels = ['a', 'e', 'i', 'o', 'u']

a = ''.join([l for l in sentence if l not in vowels])
print(a)

