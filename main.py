###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

colors = colorgram.extract('image.jpg', 25)
colours_list = []

for colour in colors:
    rgb = colour.rgb
    colours_list.append(rgb)

import random

from turtle import *

turtle = Turtle()
screen = Screen()
colormode(255)
turtle.setpos(0, 0)
screen.setworldcoordinates(-50, -50, 550, 550)
#bla bla bla
ypsilon_list = []
for y in range(50,550,50):
    ypsilon_list.append(y)

for n in range(10):
    for i in range(10):
        turtle.dot(50, (random.choice(colours_list)))
        turtle.penup()
        turtle.fd(50)
    turtle.setpos(0, ypsilon_list[n])

screen.exitonclick()
