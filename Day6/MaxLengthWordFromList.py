
lst = ['akash', 'dilip', 'raut', 'riddish', 'palash']


def max_length_word_and_length(lst):
    longest_string = ''
    
    for index in range(len(lst)):
        if len(lst[index]) > len(longest_string):
            longest_string = lst[index]
    return len(longest_string), longest_string


obj = max_length_word_and_length(lst)
print("Length of longest string is: ", obj[0], "and string is: ", obj[1])




