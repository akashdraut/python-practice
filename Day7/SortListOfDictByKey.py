
def sort_list_of_dicts(list_of_dict, key):
    return sorted(list_of_dict, key=lambda x: x[key])

data = [
    {'name': "Akash", 'age': 30},
    {'name': "Palash", 'age': 27},
    {'name': "Dilip", 'age': 50}
]

sorted_data = sort_list_of_dicts(data, key='age')
print(sorted_data)

