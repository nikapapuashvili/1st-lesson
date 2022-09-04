import re
from sys import builtin_module_names
from tkinter import RIDGE
from turtle import *

#we want to paint house
width(6)
color("blue")

penup()
goto(-300, -300)
pendown()
#starting drowing house

forward(600)
left(90)
forward(300)
left(90)
forward(600)
left(90)
forward(300)
left(180)
forward(150)
right(90)
forward(600)
left(90)
forward(150)

#end of square

#starting drowing roof

left(45)
forward(150)
left(45)
forward(350)
left(35)
forward(200)
left(180)
forward(200)
left(280)
forward(150)
left(315)
forward(300)


#finish drowing roof

#start drowing door1

right(90)
forward(80)
right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

#finish dowing door 1)

#start drowing door 2 
penup()
goto(-135, -150)
pendown()
left(180)

forward(80)
left(90)
forward(100)
left(90)
forward(80)

#finishh drowing door 2 


#start drowing windows
color("red")

penup()
goto(50, -50)
pendown()
forward(50)
left(90)
forward(150)
left(90)
forward(50)
left(90)
forward(150)
left(180)
forward(75)
right(90)
forward(50)

penup()
goto(50,-200)
pendown()
forward(50)
left(90)
forward(150)
left(90)
forward(50)
left(90)
forward(150)
left(180)
forward(75)
right(90)
forward(50)

#finishh drowing windows 

#finish homework 
exitonclick()