
lst = [1,2,4,5,6,7,3,1,4,2]

def find_most_frequent_element(lst):
    counts = {}
    for elem in lst:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    max_count = max(counts.values())
    most_frequent_element = [elem for elem, count in counts.items() if count == max_count]
    return most_frequent_element


print(find_most_frequent_element(lst))

