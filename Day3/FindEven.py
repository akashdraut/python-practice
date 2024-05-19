
# Method 1
lst = [12,3,32,56,63,13,65,98,79]
even = []
for num in lst:
    if num % 2 == 0:
        even.append(num)


print("Even number list is: ", even)

# Method2: List Comprehension
even =[ num for num in lst if num % 2 == 0]

# Method3: Using filter function
even = list(filter(lambda x : x % 2 == 0, lst))
