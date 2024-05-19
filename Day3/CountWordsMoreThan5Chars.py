
names_list = ['akash', 'palash', 'monali', 'mohini', 'dilip', 'rekha', 'riddhish']
name_length_more_than_5 = []

def count_words_having_more_than_5_chars(names_list):
    for name in names_list:
        if len(name) == 5:
            name_length_more_than_5.append(name)
    return name_length_more_than_5


print(count_words_having_more_than_5_chars(names_list))

