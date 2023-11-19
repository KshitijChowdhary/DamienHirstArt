import random
import turtle
from turtle import Screen, Turtle
from random import choice

tim = Turtle()

#Colours
turtle.colormode(255)
colour_list = [(194, 160, 120), (72, 92, 125), (143, 87, 59), (216, 209, 122), (140, 160, 188), (183, 147, 162), (29, 33, 46), (119, 73, 92), (56, 35, 26), (174, 160, 42), (139, 174, 153), (78, 115, 80), (62, 30, 40), (139, 27, 18), (118, 29, 40), (182, 101, 87), (47, 59, 92), (174, 99, 115), (102, 120, 167), (33, 51, 45), (103, 155, 87), (214, 176, 190), (216, 181, 174), (66, 83, 28), (164, 208, 188), (182, 187, 212), (218, 206, 11), (49, 71, 60), (171, 200, 208), (109, 135, 143), (49, 72, 77)]

#Pen
tim.pensize(2)

#Motion
tim.penup()
tim.setposition(-300,-200)
for j in range(1, 11):
    for i in range(10):
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20, random.choice(colour_list))
    tim.penup()
    tim.setposition(-300,-200)
    tim.left(90)
    tim.forward(50*j)
    tim.right(90)








screen = Screen()
screen.exitonclick()