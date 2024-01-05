#!/usr/bin/python3

import turtle

# Named constants
S_WIDTH = 600
S_HEIGHT = 600
T_LEFT_X = 100
T_LEFT_Y = 250
T_WIDTH = 25
FF = 30
PS = 1
N = 90
S = 270
E = 0
W = 180

def setup():
    turtle.setup(S_WIDTH, S_HEIGHT)

def draw_target():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(T_LEFT_X, T_LEFT_Y)
    turtle.pendown()
    turtle.setheading(E)
    turtle.forward(T_WIDTH)
    turtle.setheading(N)
    turtle.forward(T_WIDTH)
    turtle.setheading(W)
    turtle.forward(T_WIDTH)
    turtle.setheading(S)
    turtle.forward(T_WIDTH)
    turtle.penup()

def launch_projectile():
    # get the angle and force from the user
    angle = float(input("Enter projectile's Angle: "))
    force = float(input("Enter the launch force (1-10): "))

    # calculate the distance
    distance = force * FF

    # set the heading
    turtle.setheading(angle)

    # launch the projectile
    turtle.pendown()
    turtle.forward(distance)

    # did it hit the target?
    if (
        turtle.xcor() >= T_LEFT_X
        and turtle.xcor() <= (T_LEFT_X + T_WIDTH)
        and turtle.ycor() >= T_LEFT_Y
        and turtle.ycor() <= (T_LEFT_Y + T_WIDTH)
    ):
        print("Target Hit!")
    else:
        print("You Missed The Target")

    # Reset turtle position to (0, 0)
    turtle.goto(0, 0)

def main():
    setup()
    draw_target()

    while True:
        launch_projectile()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    turtle.done()

if __name__ == "__main__":
    main()

