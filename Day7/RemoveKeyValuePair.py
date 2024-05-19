
dict = {'name': 'akash', 'job': 'engineer', 'age': 30, 'married': 'yes'}

def remove_key_value_pair(dict, key):
    dic = dict.pop(key)
    return dict


print(remove_key_value_pair(dict, 'name'))


