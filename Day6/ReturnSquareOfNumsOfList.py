
lst = [2,4,7,8,9,13,6,8,12]

def square_of_nums_from_list(lst):
    sqr_lst = []
    for num in lst:
        sqr_lst.append(num * num)
    return sqr_lst


print(square_of_nums_from_list(lst))

