# Cantor fractal set.
# Save file as cantor.py.
# Run the module (F5).
from turtle import *
def cantor(x, y, length):
    if length >= 5:                 # Exit program if length < 5.
        speed(0)                     # Set fastest speed.
        penup()                       # Raise the turtle.
        pensize(3)                  # Line thickness.
        pencolor('blue')
        setpos(x , y)               # Coordinates of start point.
        pendown()                 # Put turtle down.
        fd(length)                  # Forward.
        y -= 30                      # y = y - 30.
        cantor(x , y, length / 3)
        cantor(x + 2 * length / 3, y, length / 3)
        penup()
        setpos(x , y + 30)
