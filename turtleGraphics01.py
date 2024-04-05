from turtle import *

def draw_rectangle():
    for k in range(4):
        t.forward(100)
        t.left(90)

t = Turtle()
for i in range(7):
    draw_rectangle()
    t.left(50)

done()
