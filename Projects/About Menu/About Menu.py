def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1)*n

while True:
    print("Welcome to the menu of recursive functions!")
    print("Select the option you want to choose:")
    print("1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Draw a recursive fractal pattern.")
    print("4. Exit the program.")

    choice = input("Enter your choice (1-4): ")

