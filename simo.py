import turtle
from turtle import *
import random
import itertools
import time
wn = turtle.Screen()
score = 0
score2 = 0
wn.title('fight')
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)
player = turtle.Turtle()
player.shape('square')

player.color('white')
player.shapesize(0.000000000000001, 3, 3)
player.goto(0, -250)
player.speed(0)
player.penup()
player.direction = 'stop'

ball = Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)
ball.goto(0, 0)
ball.penup()


def left():
    player.setx(player.xcor() + 15)
def right():
    player.setx(player.xcor() - 15)


wn.listen()
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

while True:
  ball.lt(40)
  for i in itertools.count():
    wn.update()
    ball.fd(0.1)
    if ball.xcor() > 285:
      ball.lt(45)
    if  ball.ycor() > 285:
      ball.lt(45)
    if ball.xcor() < -285:
      ball.lt(45)
    if  ball.ycor() < -285:
      time.sleep(1)
      ball.goto(0, 0)
    if player.distance(ball) < 10:
      ball.right(90)
