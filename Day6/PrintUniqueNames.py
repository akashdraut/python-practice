my_list = ['akash', 'dilip', 'akash', 'riddish', 'palash', 'dilip']


def remove_duplicate_names(lst):
    unique_names = []

    for name in lst:
        if name not in unique_names:
            unique_names.append(name)

    return unique_names


print(remove_duplicate_names(my_list))
