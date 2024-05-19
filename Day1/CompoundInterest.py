
def compound_interest(principal, rate, time):
    # Calculate compound interest
    amount = principal * (pow((1 + rate / 100), time))
    interest = amount - principal
    return interest

# Example usage
principal = 1000  # Initial amount of money
rate = 5  # Annual interest rate (in percentage)
time = 5  # Time period (in years)

interest = compound_interest(principal, rate, time)
print("Compound Interest:", round(interest, 2))


'''
from math import pow

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
tenure = int(input("Enter tenure of the loan: "))

amount  = principal * (pow((1+rate/100), tenure))
compound_interest = amount - principal
print("Compound Interest: ", compound_interest)
'''
