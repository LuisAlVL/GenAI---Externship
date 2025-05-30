my_info = {"name": "Luis Aldana", "age": 28, "city": "Aguascalientes"}
my_info["favorite_color"] = "Blue"
my_info["city"]= "Mexico City"

print("Keys : ", end = "")
for i, key in enumerate(my_info):
    if i < len(my_info) - 1:
        print(f"{key}", end = ", ")
    else:
        print(f"{key}.")

print("Values : ", end = "")
for i, value in enumerate(my_info.values()):
    if i < len(my_info) - 1:
        print(f"{value}", end = ", ")
    else:
        print(f"{value}.")