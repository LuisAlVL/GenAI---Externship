user_string = input("Enter a string: ")
reversed_string = user_string[::-1]

#Comparing to check if the string is a palindrome
if user_string == reversed_string:
    print(f"The string {user_string} is a palindrome.")
else:
    print(f"The string {user_string} is not a palindrome.")