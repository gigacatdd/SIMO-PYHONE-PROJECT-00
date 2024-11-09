import turtle
import time
import random
wn = turtle.Screen()
wn.title('snake game🐍')
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.cv._rootwindow.resizable(False, False)


head = turtle.Turtle()
head.shape('square')
head.color('white')
head.goto(0, 0)
head.speed(0)
head.deriction = 'stop'


food = turtle.Turtle()
got = random.randint(1,600)
colors = random.choice(['red', 'blue', 'green'])
shapes = 'square'
food.goto(got)
food.penup()
food.speed()


pen = turtle.Turtle()
pen.shape('square')
pen.color('white')
pen.penup()
pen.speed()
pen.goto(0, 250)
pen.hideturtle()
pen.write('score: 0 high score: 0', align='center', font=("Arial", 24, "bold"))
def goup():
    if head.direction != 'down':
        head.direction = 'up'
def godown():
    if head.direction != 'up':
        head.direction = 'down'
def goleft():
    if head.direction != 'right':
        head.direction = 'left'
def goright():
    if head.direction != 'left':
        head.direction = 'right'
def ff():
    if head == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head == 'right':
        x = head.xcor()
        head.setx(x + 20)

