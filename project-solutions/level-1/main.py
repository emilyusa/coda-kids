"""Turtle graphics project file."""
import turtle

# Create our screen
SCREEN = turtle.Screen()
SCREEN.title("Napster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic("Background.png")

SCREEN.register_shape("car", ((-4, 10), (4, 10), (4, -10), (-4, -10)))
turtle.shape("car")

# Code is explained by the book
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

# Student uncomments
turtle.left(180)
turtle.forward(510)

# Student copies from the book
turtle.right(90)
turtle.forward(220)

# Student follows instructions from the book
turtle.left(90)
turtle.forward(490)
turtle.right(90)
turtle.forward(250)

turtle.done()
