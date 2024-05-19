
# Method1:
lst1 = [1,5,8,2,3,8,3,5]
lst2 = [9,6,8,0,4,3,6,2]

def intersection_of_list(lst1, lst2):
    result = list(set(lst1) & set(lst2))
    return result

# Method2
res = []

def intersection_of_list(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j and i not in res:
                res.append(j)

    return res

print(intersection_of_list(lst1, lst2))



