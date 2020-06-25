import turtle

def move10639():
    global stars, speeds, t

    for i in range(len(stars)):
        (x, y) = stars[i].pos()
        #print(x, y)
        x += 10639*speeds[i][0]
        y += 10639*speeds[i][1]
        #print(x, y)
        stars[i].setposition(x, y)
    t += 10639
    print(t)


def create_star(p):
    global stars
    
    star = turtle.Turtle()
    star.color("black")
    star.shape("square")
    star.penup()
    star.speed(0)
    star.shapesize(.25, .25)
    star.setposition(p[0], p[1])
    stars.append(star)

        

def left50():
    global stars, speeds, t

    for i in range(len(stars)):
        (x, y) = stars[i].pos()
        #print(x, y)
        x -= 500
        #print(x, y)
        stars[i].setposition(x, y)
    print(t)
    
def down50():
    global stars, speeds, t

    for i in range(len(stars)):
        (x, y) = stars[i].pos()
        #print(x, y)
        y -= 50
        #print(x, y)
        stars[i].setposition(x, y)
    print(t)
    

def flip():
    global stars, speeds, t

    for i in range(len(stars)):
        (x, y) = stars[i].pos()
        #print(x, y)
        y *= -1
        #print(x, y)
        stars[i].setposition(x, y)
    print(t)


    
def expand5():
    global stars, speeds, t
    print("UP")
    for i in range(len(stars)):
        (x, y) = stars[i].pos()
        #print(x, y)
        x *= 2
        y *= 2
        #print(x, y)
        stars[i].setposition(x, y)
    print(t)

    
speeds = []
stars  = []
t = 0

f = open("day10_input.txt", "r")
for x in f:
    x = x.replace("<", " ")
    x = x.replace(">", " ")
    x = x.replace(",", "")
    x = x.split()
    point = (1*int(x[1]), 1*int(x[2]) )
    vel = (1*int(x[4]), 1*int(x[5]))
    create_star(point)
    speeds.append(vel)


wn = turtle.Screen()
turtle.listen()
turtle.onkey(move10639, "space")


turtle.onkey(left50, "Left")
turtle.onkey(down50, "Down")
turtle.onkey(expand5, "Up")

turtle.onkey(flip, "f")
#LCPGPXGL


