
data = [
    {'value': 10},
    {'value': 20},
    {'value': 30}
]


def average_value_of_elements(list_of_dict, key):
    total = count = 0
    for dict in data:
        if key in dict:
            total += dict[key]
            count += 1
    if count == 0:
        return None
    return total/count


print(average_value_of_elements(data, key='value'))







