def greet_user(name):
    print(f"Hello {name}, it's great to see you!")

def add_numbers(a, b):
    return a + b

name = input("Please enter your name: ")
a, b = map(int, input("Enter two numbers separated by a space: ").split())

greet_user(name)
print(f"The sum of the numbers {a} and {b} is {add_numbers(a,b)}")
