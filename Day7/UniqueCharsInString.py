
list = ['akash', 'palash', 'riddhish']

def return_unique_set_of_chars(list):
    result = set()
    for elem in list:
        for char in elem:
            if char not in result:
                result.add(char)
    return result


print(return_unique_set_of_chars(list))

