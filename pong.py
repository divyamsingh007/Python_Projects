# Simple Pong game
import turtle
import random


# Window creation
win = turtle.Screen()  # creates a window
win.title("Pong By Div")  # title of the window
win.bgcolor("black")  # background color
win.setup(width=800, height=600)  # width and height of the window
win.tracer(0)  # stops the window from updating

# paddle A
paddle_A = turtle.Turtle()  # creates a turtle object
paddle_A.speed(0)  # speed of the animation
paddle_A.shape("square")  # shape of the object
paddle_A.color("white")  # color of the object
paddle_A.penup()  # stops the object from drawing lines
paddle_A.goto(-350, 0)  # position of the object
paddle_A.shapesize(stretch_wid=5, stretch_len=1)  # size of the object

# paddle B
paddle_B = turtle.Turtle()  # creates a turtle object
paddle_B.speed(0)  # speed of the animation
paddle_B.shape("square")  # shape of the object
paddle_B.color("white")  # color of the object
paddle_B.penup()  # stops the object from drawing lines
paddle_B.goto(350, 0)  # position of the object
paddle_B.shapesize(stretch_wid=5, stretch_len=1)  # size of the object

# Ball
ball = turtle.Turtle()  # creates a turtle object
ball.speed(0)  # speed of the animation
ball.shape("circle")  # shape of the object
ball.color("white")  # color of the object
ball.penup()  # stops the object from drawing lines
ball.goto(0, 0)  # position of the object
ball.dx = 0.3  # ball movement speed in x direction
ball.dy = 0.3  # ball movement speed in y direction
# ball.dx = random.randrange(-0.5, 0.5)  # ball movement speed in x direction
# ball.dy = random.randrange(-0.5, 0.5)  # ball movement speed in y direction


# game functions
def paddle_up(target):
    y = target.ycor()  # gets the y coordinate
    y += 20  # adds 20 to the y coordinate
    target.sety(y)  # sets the y coordinate


def paddle_down(target):
    y = target.ycor()  # gets the y coordinate
    y -= 20  # adds 20 to the y coordinate
    target.sety(y)  # sets the y coordinate


# Keyboard binding
win.listen()  # listens for keyboard input
# if (paddle_A.ycor < 250 and paddle_A.ycor > -250):
win.onkeypress(lambda: paddle_up(paddle_A), "w")  # moves paddle A up
win.onkeypress(lambda: paddle_down(paddle_A), "s")  # moves paddle A down
win.onkeypress(lambda: paddle_up(paddle_B), "Up")  # moves paddle B up
win.onkeypress(lambda: paddle_down(paddle_B), "Down")  # moves paddle B down


# Main loop
while True:
    win.update()  # updates the window

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)  # moves the ball in x direction
    ball.sety(ball.ycor() + ball.dy)  # moves the ball in y direction

    # Border checking for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

