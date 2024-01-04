#!/usr/bin/python3

import turtle

# named constants
s_width = 600
s_height = 600
t_left_x = 100
t_left_y = 250
t_width = 25
ff = 30
ps = 1
n = 90
s = 270
e = 0
w = 180

# setup window
turtle.setup(s_width, s_height)

# draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(t_left_x, t_left_y)
turtle.pendown()
turtle.setheading(e)
turtle.forward(t_width)
turtle.setheading(n)
turtle.forward(t_width)
turtle.setheading(w)
turtle.forward(t_width)
turtle.setheading(s)
turtle.forward(t_width)
turtle.penup()

# centre the turtle
turtle.goto(0, 0)
turtle.setheading(e)
turtle.showturtle()
turtle.speed(ps)

# get the angle and force from the user
angle = float(input("Enter projectile's Angle: "))
force = float(input("Enter the launch force (1-10): "))

# calculate the distance
distance = force * ff

# set the heading
turtle.setheading(angle)

# launch the projectile
turtle.pendown()
turtle.forward(distance)

# did it hit the target?
if (
    turtle.xcor() >= t_left_x
    and turtle.xcor() <= (t_left_x + t_width)
    and turtle.ycor() >= t_left_y
    and turtle.ycor() <= (t_left_y + t_width)
):
    print("Target Hit!")
else:
    print("You Missed The Target")

turtle.done()

