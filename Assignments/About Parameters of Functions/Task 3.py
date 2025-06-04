def make_sandwich(*args):
    print("Ingredients for the sandwich: ", end="")
    for i,ingredient in enumerate(args):
        if i != len(args) - 1:
            print(ingredient, end= ', ')
        else:
            print(ingredient + ".")

make_sandwich("White bread", "Ham", "Mozzarella", "Pickles", "Mayonnaise", "Jalapeños")