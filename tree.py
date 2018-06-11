import turtle
import random
import math


def tree(branchLen,t):
    if branchLen > 5:
        width = branchLen/10
        t.width(width)
        t.pencolor(0, 1.0/math.pow(width+1, 1.0/3), 0)
        rightangle = random.randrange(15, 45)
        leftangle = random.randrange(15, 45)
        rightlen = random.randrange(5, 15)
        leftlen = random.randrange(5, 15)
        t.forward(branchLen)
        t.right(rightangle)
        tree(branchLen-leftlen,t)
        t.left(rightangle+leftangle)
        tree(branchLen-rightlen,t)
        t.right(leftangle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75,t)
    myWin.exitonclick()

main()

