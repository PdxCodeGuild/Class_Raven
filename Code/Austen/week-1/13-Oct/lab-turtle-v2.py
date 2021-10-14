from turtle import *


def stickfigure():
 # draw the head
    circle(50)
 # draw the neck
    right(90)
    forward(50)
 # draw the left arm
    right(45)
    forward(75)
    back(75)
 # draw the right arm
    left(90)
    forward(75)
    back(75)
 # draw the body
    right(45)
    forward(100)
 # draw the left leg
    right(45)
    forward(100)
    back(100)
 # draw the right leg
    left(90)
    forward(100)
    done()


stickfigure()
