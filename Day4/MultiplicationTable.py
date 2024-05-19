
num = int(input("Enter number for the table: "))

def table_of_number(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


table_of_number(num)

