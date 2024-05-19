
num = int(input("Enter number to limit 1 to that number: "))
prime_nums = []
'''
def is_prime(num):
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


def prime_nums_in_range(num):
    for num in range(1, num + 1):
        if is_prime(num):
            prime_nums.append(num)

    return prime_nums


print(prime_nums_in_range(num))
'''


def find_prime_nums(num):

    def is_prime(num):
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

    primes = []
    for num in range(1, num + 1):
        if is_prime(num):
            primes.append(num)
    return primes


print(find_prime_nums(num))

