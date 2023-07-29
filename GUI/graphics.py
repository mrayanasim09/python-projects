# This code is made by MRayan Asim
import turtle as tu

# Create a turtle object
fractal_turtle = tu.Turtle()

# Set up the screen
screen = tu.Screen()
screen.bgcolor("black")  # Screen Bg color
screen.title("Fractal Tree Pattern")

fractal_turtle.left(90)  # moving the turtle 90 degrees towards the left
fractal_turtle.speed(20)  # setting the speed of the turtle


# Recursive function to draw the fractal tree
def draw_fractal_tree(length):
    if length < 10:
        return
    else:
        fractal_turtle.pensize(2)  # Setting Pensize
        fractal_turtle.pencolor("yellow")  # Setting Pencolor as yellow
        fractal_turtle.forward(length)  # moving the turtle forward by 'length'
        fractal_turtle.left(30)  # moving the turtle 30 degrees towards the left
        draw_fractal_tree(
            3 * length / 4
        )  # drawing a fractal on the left with 3/4th of its length
        fractal_turtle.right(60)  # moving the turtle 60 degrees towards the right
        draw_fractal_tree(
            3 * length / 4
        )  # drawing a fractal on the right with 3/4th of its length
        fractal_turtle.left(30)  # moving the turtle 30 degrees towards the left
        fractal_turtle.pensize(2)
        fractal_turtle.backward(
            length
        )  # returning the turtle back to its original position


draw_fractal_tree(20)  # drawing the fractal tree 20 times

fractal_turtle.right(90)
fractal_turtle.speed(2000)


# Recursive function to draw the fractal tree
def draw_fractal_tree(length):
    if length < 10:
        return
    else:
        fractal_turtle.pensize(2)
        fractal_turtle.pencolor("magenta")  # magenta
        fractal_turtle.forward(length)
        fractal_turtle.left(30)
        draw_fractal_tree(3 * length / 4)
        fractal_turtle.right(60)
        draw_fractal_tree(3 * length / 4)
        fractal_turtle.left(30)
        fractal_turtle.pensize(2)
        fractal_turtle.backward(length)


draw_fractal_tree(20)

fractal_turtle.left(270)
fractal_turtle.speed(2000)


# Recursive function to draw the fractal tree
def draw_fractal_tree(length):
    if length < 10:
        return
    else:
        fractal_turtle.pensize(2)
        fractal_turtle.pencolor("red")  # red
        fractal_turtle.forward(length)
        fractal_turtle.left(30)
        draw_fractal_tree(3 * length / 4)
        fractal_turtle.right(60)
        draw_fractal_tree(3 * length / 4)
        fractal_turtle.left(30)
        fractal_turtle.pensize(2)
        fractal_turtle.backward(length)


draw_fractal_tree(20)
