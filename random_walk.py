import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
turtle.colormode(255)
timmy.speed(10)
timmy.pensize(10)
num_steps = 500
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    choice=(r, g, b)
    return choice
# Perform the random walk
for _ in range(num_steps):

    timmy.color(random_color())
    angle = random.choice([0, 90, 180, 270])  # Randomly choose a direction (0°, 90°, 180°, or 270°)
    timmy.setheading(angle)  # Set the turtle's direction
    timmy.forward(15)


My_screen=Screen()
My_screen.exitonclick()