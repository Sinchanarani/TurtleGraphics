import random
import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
turtle.colormode(255)
timmy.speed(30)
timmy.pensize(2)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    choice = (r,g,b)
    return choice
for i in range(73):
    timmy.color(random_colors())
    timmy.circle(100)
    timmy.right(5)
screen=Screen()
screen.exitonclick()