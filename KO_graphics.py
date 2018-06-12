from math import sqrt
import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("black")
    #define the turtle
    jim = turtle.Turtle()
    jim.shape("circle")
    jim.color("white")
    jim.speed(5)
    #draw K
    jim.left(90)
    jim.forward(100)
    jim.right(180)
    jim.forward(200)
    jim.left(90)
    jim.up()
    jim.forward(100)
    jim.down()
    jim.left(135)
    jim.forward(sqrt(20000))
    jim.right(90)
    jim.forward(sqrt(20000))
    #draw space
    jim.right(45)
    jim.up()
    jim.forward(50)
    jim.down()
    #draw o
    jim.right(90)
    jim.forward(200)
    jim.left(90)
    jim.forward(100)
    jim.left(90)
    jim.forward(200)
    jim.left(90)
    jim.forward(100)
    jim.hideturtle()
    window.exitonclick()

draw_shape()
