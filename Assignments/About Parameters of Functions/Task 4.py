def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(f'Factorial of 6 is {factorial(6)}. The 6th Fibonacci number is {fibonacci(6)}.')
