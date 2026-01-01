import cmath
import math
from turtle import *

# Initializing speed
speed(0)

bgcolor("black")
color("#229302")  # A different color for triangle
hideturtle()

side = 3
angle = 360 / side

length = 2
#length of each side

for i in range(500):
    forward(length)
    right(angle)
    length += 1
done()
