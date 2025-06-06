grocery_list = ["Bread", "Tomatoes", "Water", "Soda", "Sugar", "Coffee", "Steak"]

try:
    print(grocery_list[9])
except IndexError:
    print("Index error! List index out of range.")

num_fruits = {"Mango" : 12, "Banana": 10, "Strawberry": 1, "Apple": 10}

try:
    print(num_fruits["kiwi"])
except KeyError:
    print("KeyError! Key not found in the keyboard.")

price = {"Mango" : 1, "Banana": 2, "Strawberry": '0.4', "Apple": 2}

try:
    total_price_fruits = sum(num_fruits[fruit] * price[fruit] for fruit in num_fruits)
    print(total_price_fruits)
except TypeError:
    print("TypeError! Unsupported operand types.")