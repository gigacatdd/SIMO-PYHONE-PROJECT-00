import turtle
import time
import random


score = 0
delay = 0.10
high = 0

#the window
wn = turtle.Screen()
wn.title('snake game🐍')
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.cv._rootwindow.resizable(False, False)
wn.tracer(0)
#the head of the snake
head = turtle.Turtle()
head.shape('square')
head.color('white')
head.goto(0, 0)
head.speed(0)
head.penup()
head.direction = 'stop'


food = turtle.Turtle()
x = random.randint(-270,270)
y = random.randint(-270,270)
colors = 'red'
shapes = 'circle'
food.shape(shapes)
food.color(colors)
food.penup()
food.speed(0)
food.goto(0, 100)


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
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)



wn.listen()
wn.onkeypress(goup, 'w')
time.sleep(0.1)
wn.onkeypress(godown, 's')
time.sleep(0.1)
wn.onkeypress(goleft, 'a')
time.sleep(0.1)
wn.onkeypress(goright, 'd')
time.sleep(0.1)
segments = []
while True:
    wn.update()

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        food.shape('circle')
        food.color('red')
        for segment in segments:
          segment.goto(0, 1000)
          segments.clear()
          score = 0 
          delay = 0.1
          pen.clear()
          pen.write('score: {} high score: {}'.format(score, high)
                 , align='center'
                 , font=("Arial", 24, "bold"),
                 )
    if head.distance(food) < 25:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        lor = turtle.Turtle()
        lor.shape('square')
        lor.color('red')
        lor.speed(0)
        lor.penup()
        segments.append(lor)
        score += 1
        if score > high:
            high = score
            pen.clear()
            pen.write(pen.write('score: {} high score: {}'.format(score, high)
                                   ,align='center', 
                                   font=("Arial", 24, "bold"),))
    for ind in range(len(segments) - 1, 0, -1):
        y = segments[ind - 1].ycor()
        x = segments[ind - 1].xcor()
        segments[ind].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
       if segment.distance(head) < 20:
           time.sleep(1)
           head.goto(0, 0)
           colors = 'red'
           shapes = 'circle'
           food.shape(shapes)
           food.color(colors)
           for segment in segments:
               segment.goto(1000, 1000)
               segments.clear()
               pen.write(pen.write('score: {} high score: {}'.format(score, high)
                    , align='center'
                      , font=("Arial", 24, "bold")))
    time.sleep(delay)