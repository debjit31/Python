import turtle
import os
import math
import random

#Set up the screen

window=turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
#window.bgpic("bk.png")

#Draw a border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14, "normal"))
score_pen.hideturtle()

#Create a player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)



playerspeed = 15



###Create the enemy
##
##enemy=turtle.Turtle()
##enemy.color("red")
##enemy.shape("circle")
##enemy.penup()
##enemy.speed(0)
##enemy.setposition(-250,200)
##
##enemyspeed = 2

#Chose the number of enemies
number_of_enemies = 5
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

    enemyspeed = 2


#Create the players bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#Define  bullet state

#ready-- ready to fire
#fire-- firing
bulletstate = "ready"

#Move the player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x+= playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance=math.sqrt(math.pow(t2.xcor()-t1.xcor(),2)+math.pow(t2.ycor()-t1.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")




#Main game loop

while True:

    for enemy in enemies:
        
       #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down

        if enemy.xcor() > 280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
             
        if enemy.xcor() < -280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

            #Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
                #Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                #Reset the enemy
                x = random.randint(-200,200)
                y = random.randint(100,250)
                enemy.setposition(x,y)
                #Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring,False,align="left",font=("Arial",14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

   #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


                         
    
