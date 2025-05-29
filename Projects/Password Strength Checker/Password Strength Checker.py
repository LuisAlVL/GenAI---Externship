user_input = input("Enter a password: ")

# Check password length
correct_length = len(user_input) >= 8
has_digit = any(char.isdigit() for char in user_input)
has_upper = any(char.isupper() for char in user_input)
has_special = any(char in "@#$!^&%()[]*" for char in user_input)

# Check if all conditions are met
if correct_length and has_digit and has_upper and has_special:
    print("Password is strong!")
    Strength = 8
    if len(user_input) >= 12:
        Strength += 2
    print(f"Password strength score: {Strength}")
else:
    output = ""
    if not correct_length:
        output += "Password must be at least 8 characters long"
        if not has_digit:
            output += ", must contain at least one digit"
        if not has_upper:
            output += ", must contain at least one uppercase letter"
        if not has_special:
            output += ", must contain at least one special character (@#$!^&%()[]*)"
    elif not has_digit:
        output += "Password must contain at least one digit"
        if not has_upper:
            output += ", must contain at least one uppercase letter"
        if not has_special:
            output += ", must contain at least one special character (@#$!^&%()[]*)"
    elif not has_upper:
        output += "Password must contain at least one uppercase letter"
        if not has_special:
            output += ", must contain at least one special character (@#$!^&%()[]*)"
    elif not has_special:
        output += "Password must contain at least one special character (@#$!^&%()[]*)"
    
    print(output, ". Please try again.")