inventory = {}
# We will represent the inventory as a dictionary where the keys are item names and the values are tuples consisting of the quantity and price per item.
print("Welcome to the Grocery Store Inventory System!")
print("Current inventory is empty.")

while True:
    print("\nYou can perform the following actions:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Update quantity or price of an item")
    print("4. Calculate the total value of inventory")
    print("5. Exit the program")
    action = int(input(("What would you like to do? ")))

    if action == 1:
        item_name = input("Enter the name of the item: ")
        quantity = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        inventory[item_name] = (quantity, price)
    elif action == 2:
        item_name = input("Enter the name of the item to remove: ")
        if item_name in inventory:
            del inventory[item_name]
        else:
            print(f"{item_name} is not in the inventory.")
            continue
    elif action == 3:
        item_name = input("Enter the name of the item to be updated: ")
        if item_name in inventory:
            quantity = int(input("Enter the new quantity: "))
            price = float(input("Enter the new price: "))
            inventory[item_name] = (quantity, price)
        else:
            print(f"{item_name} is not in the inventory.")
            continue
    elif action == 4:
        total = sum(inventory[item][0]*inventory[item][1] for item in inventory)
        print(f"The total value of the inventory is: {total}")
        continue
    elif action == 5:
        break
    
    print("\nUpdated inventory: ")
    for item in inventory:
        print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")
