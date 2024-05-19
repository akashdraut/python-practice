
my_list = ['akash', 'dilip', 'akash', 'riddish', 'palash', 'dilip']


def get_count_of_each_element(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count


print(get_count_of_each_element(my_list))
