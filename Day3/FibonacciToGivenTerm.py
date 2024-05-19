
def fibonacci(term):
    series = [0, 1]
    for i in range(2, term):
        next_term = series[i-1] + series[i-2]
        series.append(next_term)

    return series

num_terms = int(input("Enter the number of terms: "))
fib_series = fibonacci(num_terms)
print(f"The Fibonacci series up to {num_terms} terms is: {fib_series}")

