done = False
while not done:
    try:
        number = float(input("Enter a number: "))
        print(f'100/{number} = {100/number}')
        done = True
    except ValueError:
        print("Invalid input! Please write a number.")
    except ZeroDivisionError:
        print("Oops! Zero division is invalid.")