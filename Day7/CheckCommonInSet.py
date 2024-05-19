# Method1
def check_common_elem_set(set1, set2):
    res = set1 & set2
    if res:
        return True
    return False


set1 = {1,2,4,6}
set2 = {1,4,7,9}
print(check_common_elem_set(set1, set2))


# Method2
def have_common_elem(set1, set2):
    for elem in set1:
        if elem in set2:
            return True
    return False


print(have_common_elem(set1, set2))


# get count too

def have_common_elem(set1, set2):
    common_elems = set()
    for elem in set1:
        if elem in set2:
            common_elems.add(elem)
    return common_elems

print(have_common_elem(set1, set2))
