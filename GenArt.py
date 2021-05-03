import turtle
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
#from tkinter import *

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

wn = turtle.Screen()

collst = ["black", "white", "blue", "red", "yellow", "pink", "brown", "silver", "gray", "purple", "gold", "green", "light blue", "light yellow", "light pink", "tan", "light gray", "lavender", "light green"]

bcollst = ["light blue", "light yellow", "light pink", "tan", "light gray", "lavender", "light green"]

tommy = turtle.Turtle()
tommy.shape("circle")
tommy.speed(1000)

bkgr = random_number(len(bcollst))

back = bcollst[bkgr]

turtle.bgcolor(back)

collst.remove(bcollst[bkgr])

shnum = random_number2(15, 30)

for ctr in range(shnum):

    fgr = random_number(len(collst))

    fore = collst[fgr]

    tommy.color(fore)

    xco = random_number2(-200, 200)

    yco = random_number2(-200, 200)

    csiz = random_number2(10, 200)

    tommy.penup()

    tommy.goto(xco, yco)

    tommy.begin_fill()

    tommy.circle(csiz)

    tommy.end_fill()

#ts = turtle.getscreen()

#filnm = "Turtle_" + tim + ".eps"

#ts.getcanvas().postscript(file=filnm)

turtle.exitonclick()