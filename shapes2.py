from turtle import Turtle,Screen
timmy = Turtle()
timmy.speed(2)

for i in range(3,11):
    for j in range(i):
        angle=360/i
        timmy.forward(100)
        timmy.right(angle)
my_screen=Screen()
my_screen.exitonclick()