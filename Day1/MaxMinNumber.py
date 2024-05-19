# Method 1:
lst = [5, 2, 8, 1, 9]
print("Max value is: ", max(lst), "and Min value is: ", min(lst))

# Method 2:
lst = [5, 2, 8, 1, 9]
lst.sort()
print("Max value is: ", lst[-1], "and Min value is: ", lst[0])

# Method 3:
lst = [5, 2, 8, 1, 9]
max_num = lst[0]
min_num = lst[0]
for num in lst:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
print("Max value is: ", max_num, "and Min value is: ", min_num)

# Method 4:
lst = [5, 2, 8, 1, 9]
max_num = max(lst, key=lambda x:x)
min_num = min(lst, key=lambda x:x)
print("Max value is: ", max_num, "and Min value is: ", min_num)

# Method 5:
from functools import reduce
lst = [5, 2, 8, 1, 9]

max_num = reduce(lambda a, b:a if a > b else b, lst)
min_num = reduce(lambda a, b:a if a < b else b, lst)
print("Max value is: ", max_num, "and Min value is: ", min_num)


