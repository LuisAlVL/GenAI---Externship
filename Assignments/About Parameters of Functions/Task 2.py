def describe_pet(pet_name, animal_type = "dog"):
    print(f"This is my cute {animal_type.lower()}, its name is {pet_name.capitalize()}")

describe_pet("Milka")
describe_pet("catarino", "Cat")