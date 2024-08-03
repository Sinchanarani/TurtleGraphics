from turtle import Turtle, Screen
timmy = Turtle()
timmy.speed(2)
def triangle():
    timmy.color('blue')
    for i in range(3):
        timmy.forward(100)
        timmy.right(120)




def square():
    timmy.color('red')
    timmy.forward(100)
    for i in range(4):
        timmy.right(90)
        timmy.forward(100)



def pentagon():
    timmy.color('pink')
    for i in range(5):
        timmy.right(72)
        timmy.forward(100)
def hexagon():
    timmy.color('orange')
    for i in range(6):
        timmy.right(60)
        timmy.forward(100)
def heptagon():
    timmy.color('black')
    angle=360/7
    for i in range(7):

        timmy.right(angle)
        timmy.forward(100)
    #timmy.right(180)
def octagon():
    timmy.color('green')
    for i in range(8):
        timmy.right(45)
        timmy.forward(100)

def nanogon():
    timmy.color('violet')
    for i in range(9):
        timmy.right(40)
        timmy.forward(100)
def decagon():
    timmy.color('green')
    for i in range(10):
        timmy.right(36)
        timmy.forward(100)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nanogon()
decagon()
my_screen=Screen()
my_screen.exitonclick()