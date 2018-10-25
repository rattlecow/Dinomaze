import turtle
import math
import random

# creating a screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A  Maze Game")
wn.setup(700,700)
wn.tracer(0)

# register shapes
turtle.register_shape("pumpkin.gif")
turtle.register_shape("meteor.gif")
turtle.register_shape("$ (2).gif")
turtle.register_shape("hy.gif")

# draw one white square
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("$ (2).gif")
        self.color("white")
        self.penup()
        self.speed(0)
# making player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("hy.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
# make player move
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # to see if there is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)        
    def go_right(self):      
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)  
    #collect treasure
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()    
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

# make treasure chest
class Treasure(turtle.Turtle):
    def __init__(self, x, y):    
        turtle.Turtle.__init__(self)
        self.shape("pumpkin.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
#make enemy
class enemy(turtle.Turtle):
    def __init__(self, x, y,):
        turtle.Turtle.__init__(self)
        self.shape("meteor.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0  

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"    
            elif player.xcor() > self.xcor():
                self.direction = "right"   
            elif player.ycor() < self.ycor():
                self.direction = "down"   
            elif player.ycor() > self.ycor():
                self.direction = "up"   

        move_to_x = self.xcor() + dx  
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])
        
        turtle.ontimer(self.move, t=random.randint(200, 500))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))   
        
        if distance < 75:
            return True
        else:
            return False
            
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
#levels
levels = [""]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"XXX  XXXXXXXXX     XXXX X",
"XXX  XXXXX E      XXXXX X",
"XXX  XXXXX XXXXX   XXXX X",
"XXX  XXXXX XXXXXX   XXX X",
"XT X        XXXX   XXXX X",
"XX XXXXXXX    XXX   XXX X",
"XX XXXXXX     XX  XXXXX X",
"XX        XXXXXX   XXXX X",
"XXXX                  X X",
"XXXXX  XXXXXXXX  XXXXXX X",
"XXXXX XXXXXXXXX  XXXXXX X",
"X   E XX         XXT    X",
"X       XXXXXXX   XXXXX X",
"XX  XXX XXXXXX    XXXXX X",
"XX  XXX   XXXXXE  XXXXX X",
"XX  XX X T      XX  X   X",
"XX       XX XXXXX  XXXX X",
"XXXXXXXX XX XXXXX  XXXX X",
"XXXXXX       XX         X",
"XXXXXXXX XXXXXXXXXXX XXXX",
"XT          XX         XX",
"XXXXXX    XXXXXX    XXXXX",
"X         TEXX   E      X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
enemies = []
# add a treasures list
treasures = []

levels.append(level_1)

# create a maze by using the pen class to draw it
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # add coordinates to walls list
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            # MAKE TREASURES
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            # make enemies
            if character == "E":
                enemies.append(enemy(screen_x, screen_y))



pen = Pen()
player = Player()
# create wall coordinate list
walls = []
# setting up maze
setup_maze(levels[1])

# make player move by pressing keys
turtle.listen()
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True:
    for Treasure in treasures:
        if player.is_collision(Treasure):
            player.gold += Treasure.gold
            print("Player Gold: {}".format(player.gold))
            Treasure.destroy()
            treasures.remove(Treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("You're Dead!")
            
    wn.update()