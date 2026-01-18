import turtle
import math
import random

# Ekran sozlamalari
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders - Koinot Jangi")
wn.tracer(0)

# Chegarani chizish
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_left = border_pen.left(90)
border_pen.hideturtle()

# O'yinchi kemasi
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Dushmanlar soni
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# O'yinchi o'qi
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready" # "ready" - otishga tayyor, "fire" - o'q uchmoqda

# Funksiyalar
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    return distance < 20

# Klaviatura nazorati
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Asosiy o'yin tsikli
while True:
    wn.update()
    
    for enemy in enemies:
        # Dushmanni harakatlantirish
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Dushman chetga yetganda pastga tushishi
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        # O'q dushmanga tegishini tekshirish
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Dushmanni qayta joylashtirish
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))

        # Dushman kema bilan to'qnashsa
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("O'YIN TUGADI!")
            break

    # O'q harakati
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # O'q tepaga chiqib ketsa
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"