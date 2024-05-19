lst = ['apple', 'banaba', 'cherry', 'straberry']
index = int(input("Enter index to access element: "))

try:
    value = lst[index]
    print("Value is:", value)
except IndexError:
    print("Invalid index value")


