number = int(input("Please enter a number: "))
result = 1
for i in range(1, number + 1):
    result *= i

print(f"{number}! = {result}")