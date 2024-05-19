
num = int(input("How many string values you want to add: "))
string_list = []

for i in range(1, num+1):
    string_value = input(f"Enter string {i}: ")
    string_list.append(string_value)


def sort_list_elements(lst):
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            if len(lst[i]) <= len(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst


print(sort_list_elements(string_list))


