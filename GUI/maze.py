import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("A Maze Game")
window.setup(700,700)

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
         
#Create levels list
levels= [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXX  XXX   XXXX  XX"
"X  XXX    XXX   XXXXXXXXX"
"X  XXXXXXXXXX  XXXXXXXXXX"
"XXXXXXX    XX  XXXXX  XXX"
"XXXXX       X      X  XXX"
"XX   XXX  XX  X  XXX  XXX"
"XXX  XXXX  XXX         XX"
"XXXX    XXX    XX XXX XX "
"XXX   XX XX   XX   XX   X"
"X   XX    X   X X  XXXXXX"
"X   XX    XXXXX        XX"
"XX   X    X   X    XXX XX"
"X   XX   X X   XXXXXX  XX"
"X   X XXXXX XXX XXX X X X"
"XXXX   XXXX  XXX  XXX X  "
"XXXX   XXXX  X   X    XXX"
"XXX            XXXXXXXXXX"
"XXXXXXXXXX     XXXX   XXX"
"XXXXXXXX     XXXXX    XXX"
"XXXXXXXXX            XXXX"
"XXXX      XXXX          X"
"XXXXX         XXXX    XXX"
]

#Add maze to maze list
levels.append(level_1)

#Create Level Setup Function
def setup_maze(levels):
    for y in range(len(levels)):
        for x in range(len(levels[y])):
            #Get the character at each x, y coordinate
            #NOTE the order of y and x in the next line
            character = levels[y][x]
            #Calculate the screen x y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)


            #Check if it is an X(representing a wall)
            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()

            #Check if it is a P(representing a player)
                if character == "P":
                    player.goto(screen_x,screen_y)
            

#Create class instances
pen = Pen()
player = Player()

#Set up the level
setup_maze(levels[1])


#Main Game Loop



