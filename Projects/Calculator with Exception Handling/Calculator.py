import logging
import os

# Get directory of current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define full path for the log file in the script's folder
log_file = os.path.join(script_dir, 'error_log.txt')

logging.basicConfig(
    filename = log_file,
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filemode = 'a'
)

print("Welcome to the calculator program!")
while True:
    print("Menu of operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    try:
        operation = int(input("Enter the number corresponding to the operation you want to perform (1–5):"))
        #Exit
        if operation == 5:
            print("Goodbye!")
            break
        a, b = map(float, input("Enter two numbers separated by a space: "
        "").split())

        #Division
        if operation == 4:
            print(f"{a} / {b} = {a / b}")

    except ValueError:
        print("ValueError detected! Please make sure to follow the instructions and enter numbers only")
        logging.error("ValueError occurred: Invalid input")
    except ZeroDivisionError:
        print("Division by zero is not allowed!")
        logging.error("ZeroDivisionError: Attempted division by zero.")
    else:
        #Addition
        if operation == 1:
            print(f'{a} + {b} = {a + b}')
        #Subctraction
        elif operation == 2:
            print(f'{a} - {b} = {a - b}')
        #Multiplication
        elif operation == 3:
            print(f'{a}*{b} = {a*b}')
        #If operation is not in the range (1-5)
        elif operation != 4:
            print("That option is not available in the menu. Please try again.")
    finally:
        print("\n\n")    

    

