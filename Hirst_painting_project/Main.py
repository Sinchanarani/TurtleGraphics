# import colorgram
# color_list=[]
# colors= colorgram.extract('Hirstspotpainting.jpg', 30)
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     color_list.append((r,g,b))
# print(color_list)



import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
timmy=Turtle()
timmy.speed(5)
color_list=[(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]


def turn():
    timmy.setheading(90)
    timmy.forward(20)
    timmy.setheading(180)
    timmy.forward(200)
    timmy.setheading(0)
def line():
    for i in range(10):
        timmy.dot(10, random.choice(color_list))
        timmy.penup()
        timmy.forward(20)
        timmy.penup()
    turn()

for i in range(10):
    line()

screen=Screen()
screen.exitonclick()