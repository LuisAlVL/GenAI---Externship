import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    attempts += 1

    if guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:   
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} attempts.")
        break


