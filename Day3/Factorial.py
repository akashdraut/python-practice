
def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


num = int(input("Enter number to calculate factorial: "))
print(factorial(num))

