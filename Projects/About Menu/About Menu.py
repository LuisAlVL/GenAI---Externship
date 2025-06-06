import turtle

#Simple recursive function to calculate n!
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

#Simple recursive function to calculate the nth fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Recursive function to draw an asymetric fractal canopy
# Memoization could improve this function, but it's not clear how to implement it with Turtle
def draw_line(turtle, length, level):
    if level == 0:
        return
    turtle.forward(length)
    # Storing turtle position
    heading = t.heading()
    position = t.pos()
    
    length /= 2
    
    # Drawing right branch
    turtle.right(30)
    draw_line(turtle, length, level - 1)

    # Restoring position and direction of turtle 
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()

    #Drawing left branch
    turtle.left(60)
    draw_line(turtle, length, level - 1) 

print("Welcome to the menu of recursive functions!")
while True:
    print("\nSelect the option you want to choose:")
    print("1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Draw a recursive fractal pattern.")
    print("4. Exit the program.")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        n = int(input("Enter a number: "))
        print(f'The factorial of {n} is {factorial(n)}')
    if choice == "2":
        n = int(input("Enter the Fibonacci number you want: "))
        print(f'The {n}th fibonacci number is {fibonacci(n)}')
    if choice == "3":
        # Setup screen size
        screen = turtle.Screen()
        screen.setup(width=800, height=600)  # width x height in pixels

        # Create turtle
        t = turtle.Turtle()
        t.speed(0)  # Fastest drawing

        # Move turtle to bottom center of the screen
        t.penup()
        t.goto(0, -screen.window_height() // 2)
        t.setheading(90)  # Face upward
        t.pendown()

        draw_line(t, 250, 9)
        turtle.done()

    if choice == "4":
        break
    