try:
    a, b = map(float, input("Enter two numbers (separated by a space):").split())
    result = a/b
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
except ValueError:
    print("Oops! ValueError detected. The input should be two numbers separated by a space.")
else:
    print(f"Dividing the first number by the second results in {result}")
finally:
    print("Have a nice day!")