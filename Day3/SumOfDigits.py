
def sum_of_digits(num):
    sum = 0
    if num < 1:
        return "Invalid number"
    while num != 0:
        digit = num % 10
        sum += digit
        num = num // 10
    return sum


num = int(input("Enter number: "))
print(sum_of_digits(num))
        

