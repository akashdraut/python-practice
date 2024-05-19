
lst = ['rekha', 'dilip', 'akash', 'palash', 'mohini', 'monali', 'riddhish']
sorted_list = []
lst.sort()
print(lst)


lst = ['rekha', 'dilip', 'akash', 'palash', 'mohini', 'monali', 'riddhish']

def sort_list_of_strings(lst):
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j],lst[i]
    
    return lst

print(sort_list_of_strings(lst))

# print(lst)
