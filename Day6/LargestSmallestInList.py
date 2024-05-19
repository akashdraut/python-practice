
lst = [2,4,7,8,9,13,6,8,12]

smallest = largest = lst[0]

def find_smallest_largest_from_list(lst):
    smallest = largest = lst[0]
    for index in range(len(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
        if lst[index] > largest:
            largest = lst[index]
    return smallest, largest

print(find_smallest_largest_from_list(lst))

