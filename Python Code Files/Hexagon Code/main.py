import math
import cmath
from turtle import *


#inititalisng speed
speed(0)
bgcolor("black")
color("cyan")
hideturtle()

sides = 6

angle = 360 / sides
length = 2

for i in range(2000):
    forward(length)
    right(angle)
    length += 1
done() 
