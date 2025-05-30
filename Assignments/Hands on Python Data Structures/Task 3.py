my_preferences = ("Interstellar", "Sinnerman", "Émile, ou De l’éducation")
try:
    my_preferences[0] = "Inception"  
except TypeError as e:
    print(f"You cannot alter an immutable element in a tuple!!")

print(f"There are {len(my_preferences)} items in my preferences.")