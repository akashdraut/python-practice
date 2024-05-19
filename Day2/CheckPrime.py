
def check_if_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
        
    return True


num = int(input("Enter number: "))
if check_if_prime(num):
    print("Number is prime number")
else:
    print("Number is not prime number")

