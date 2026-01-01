from turtle import *
import math
import cmath

# Initializing speed
speed(0)

bgcolor("black")
color("#9C026B")
hideturtle()

side = 5
angle = 360 / side

length = 2
#length of each side

# Drawing the pentagon
for i in range(500):
    forward(length)
    right(angle)
    length += 1

done()
