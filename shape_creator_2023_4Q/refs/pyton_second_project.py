import turtle

def draw_line():
    turtle.forward(100)
    turtle.right(90)

def draw_triangle():
    for _ in range(3):
        draw_line()

def draw_rectangle():
    for _ in range(2):
        draw_line()
        turtle.forward(100)
        turtle.right(90)

def draw_circle():
    turtle.circle(50)

def create_shape():
    user_input = int(input("Enter the number of sides (1-4) or a larger number for a circle: "))
    
    if user_input == 1:
        draw_line()
    elif user_input == 2:
        for _ in range(2):
            draw_line()
    elif user_input == 3:
        draw_triangle()
    elif user_input == 4:
        draw_rectangle()
    elif user_input > 4:
        draw_circle()
    else:
        print("Invalid input. Please enter a number between 1 and 4 or a larger number for a circle.")

turtle.speed(1)
create_shape()

turtle.done()
