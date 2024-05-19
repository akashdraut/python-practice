
dict1 = {"name": "akash", "job": "engineer"}
dict2 = {"age": 30, "married": "yes"}

# Method1
dict1.update(dict2)
print(dict1)


# Method2
result1 = dict(dict1, **dict2)
print(result1)


# Method3
result2 = {**dict1, **dict2}
print(result2)


# Method4
result3 = dict1 | dict2
print(result3)


