my_list = ['akash', 'dilip', 'akash', 'riddish', 'palash', 'dilip']


def sorted_list(my_list):
    original_list = my_list[:]
    for i in range(0, len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] >= my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    res = my_list == original_list
    return res


print(sorted_list(my_list))
    

