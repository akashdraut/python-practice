
set1 = {1,2,3,4,56,7,8}
set2 = {00,9,8,7,6,5}

# Union Operations
print(set1 | set2) 
print(set1.union(set2))

def set_union(set1, set2):
    result = set()
    for element in set1:
        result.add(element)
    
    for element in set2:
        result.add(element)

    return result

print(set_union(set1, set2))

# Intersection Operations
print(set1 & set2)
print(set1.intersection(set2))

def set_intersection(set1, set2):
    result = set()
    for elem in set1:
        for element in set2:
            if elem == element:
                result.add(elem)

    return result

print(set_intersection(set1, set2))


# Difference Operations
print(set1 - set2)
print(set2.difference(set1))

def set_difference(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)

    return result

print(set_difference(set1, set2))

