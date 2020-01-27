#Space Invader
#Python 3.8
import turtle
import winsound
import random
import math

#Setup screen
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invader")
main_screen.bgpic(".\img\space_invaders_background.gif")

#Register shapes
turtle.register_shape(".\img\invader.gif")
turtle.register_shape(".\img\player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()

#Set the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-295, 275)
score_str = "Score: %s" %score
score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create player Turtle
player = turtle.Turtle()
player.setposition(0, -250)
player.color("blue")
player.shape(".\img\player.gif")
player.penup()
player.speed(0)
player.setheading(90)

player_speed = 15

#Create enemy
number_of_enemies = 7
enemies = []
for enemy in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    enemy.color("red")
    enemy.shape(".\img\invader.gif")
    enemy.penup()
    enemy.speed(0)

enemy_speed = 2

#Create player's bullet
bullet = turtle.Turtle()
bullet.setposition(0, -400)
bullet.color("yellow")
bullet.shape("triangle")
bullet.shapesize(0.4, 0.4)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)

bullet_speed = 18

#Bullet state
#ready - ready to fire
#fire - bullet is firing
bullet_state = "ready"


#Move the player left & right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x= 280
    player.setx(x)


def fire_bullet():
    #Declare bullet state as a global if it needs changed
    global bullet_state
    if bullet_state == "ready":
        winsound.PlaySound(".\sound\laser.wav", winsound.SND_ASYNC)
        bullet_state = "fire"
        #Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 5
        bullet.setposition(x, y)
        bullet.showturtle()


def is_hit(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor() - obj2.xcor(), 2) + math.pow(obj1.ycor() - obj2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


def respawn(obj):
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    obj.setposition(x, y)


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x -= enemy_speed
        enemy.setx(x)

        #Move enemy back and down
        if enemy.xcor() < -280 or enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            #Change direction
            enemy_speed *= -1

        if enemy.ycor() < -280:
            respawn(enemy)

        #Check bullet hit enemy
        if is_hit(bullet, enemy):
            winsound.PlaySound(".\sound\explosion.wav", winsound.SND_ASYNC)
            #Reset bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400) 
            #Reset the enemy
            respawn(enemy)
            #Update score
            score += 10
            score_str = "Score: %s" %score
            score_pen.clear()
            score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
        
        #Bullet move
        if bullet_state == "fire":
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)

        if bullet.ycor() > 280:
            bullet.hideturtle()
            bullet_state = "ready"

        #Check enemy hit player
        if is_hit(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    



delay = input("Press enter to finish.")