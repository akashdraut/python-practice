
num_list = []
limit = int(input("How many nunbers you want to enter: "))
for num in range(1, limit + 1):
    number = int(input(f"Enter number {num}: "))
    num_list.append(number)

def sum_of_positive_nums(num_list):
    sum = 0
    for num in num_list:
        if num > 0:
            sum += num
    return sum


print(sum_of_positive_nums(num_list))



