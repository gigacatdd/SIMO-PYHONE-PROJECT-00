import turtle
import random
import time

# إعدادات الشاشة
wn = turtle.Screen()
wn.title('Fight')
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)

# إعدادات اللاعب
player = turtle.Turtle()
player.shape('square')
player.color('white')
player.shapesize(1, 3, 3)  # تغيير الحجم لتناسب اللعبة
player.goto(0, -250)
player.penup()
player.speed(0)

# إعدادات الكرة
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed(1)  # سرعة الكرة
ball.goto(0, 0)

# متغيرات
player_speed = 15
ball_speed = 0.1
ball_angle = random.randint(30, 60)  # زاوية عشوائية للبداية
ball_direction = random.choice(['up', 'down'])

# دوال تحريك اللاعب
def move_left():
    x = player.xcor()  # الحصول على الإحداثيات الحالية للاعب
    x -= player_speed  # تحريك اللاعب إلى اليسار
    player.setx(x)  # تحديث الموقع الجديد

def move_right():
    x = player.xcor()  # الحصول على الإحداثيات الحالية للاعب
    x += player_speed  # تحريك اللاعب إلى اليمين
    player.setx(x)  # تحديث الموقع الجديد

# دالة تحريك الكرة
def move_ball():
    global ball_angle, ball_direction
    if ball_direction == 'down':
        ball.setheading(ball_angle)
    else:
        ball.setheading(180 - ball_angle)
    
    ball.forward(ball_speed)
    
    # التحقق من اصطدام الكرة بالحواف
    if ball.xcor() > 290:
        ball.setx(290)
        ball_angle = random.randint(120, 150)  # زاوية عشوائية جديدة عند الاصطدام
    if ball.xcor() < -290:
        ball.setx(-290)
        ball_angle = random.randint(30, 60)
    if ball.ycor() > 290:
        ball.sety(290)
        ball_angle = random.randint(120, 150)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_angle = random.randint(30, 60)
    
    # التحقق من الاصطدام مع اللاعب
    if player.distance(ball) < 40:
        ball_angle = random.randint(120, 150)  # تغيير اتجاه الكرة عند الاصطدام باللاعب

# الاستماع إلى ضغطات المفاتيح
wn.listen()
wn.onkeypress(move_left, 'a')  # عند الضغط على "a" يتحرك اللاعب لليسار
wn.onkeypress(move_right, 'd')  # عند الضغط على "d" يتحرك اللاعب لليمين

# الحلقة الرئيسية للعبة
while True:
    wn.update()  # تحديث الشاشة في كل مرة
    move_ball()  # تحريك الكرة

    # التحقق إذا كانت الكرة خرجت من الشاشة (أسفل)
    if ball.ycor() < -300:
        ball.goto(0, 0)  # إعادة الكرة إلى المنتصف
        ball_angle = random.randint(30, 60)  # تعيين زاوية عشوائية جديدة للكرة

    time.sleep(0.0000000000000001)  # تبطيء حلقة اللعبة لتكون قابلة للعب
