# Christerpher Hunter
# Lab 01: Turtle

from turtle import begin_fill, circle, done, end_fill, fillcolor, forward, home, left, pendown, penup, right, setheading, setposition, speed

# Draw the head connected to the body
def draw_body():
    right(-90)
    forward(200)
    penup()    
    forward(-150)
    pendown()
    
# Attach two arms to the body
def draw_arms():
    right(-45)
    forward(100)
    penup()
    forward(-100)
    pendown()
    right(90)
    forward(100)
    penup()
    forward(-100)
    pendown()

# Attach two legs to the body
def draw_legs():
    right(-45)
    forward(200)
    right(-45)
    forward(120)
    forward(-120)
    right(90)
    forward(120)
    forward(-120)# Attach two legs to the body
def draw_legs():
    right(-45)
    forward(200)
    right(-45)
    forward(120)
    forward(-120)
    right(90)
    forward(120)
    forward(-120)


def main():

    # Set initial position
    penup()     
    setposition(0, 45)
    pendown()

    # Draw the head as a circle
    speed(0)
    i = 0
    edge_length = 10
    while i < 60:    
        pendown()
        forward(edge_length)
        right(360/40)
        i += 1    

    draw_body()
    draw_arms()
    draw_legs()        

    done ()
    
if __name__ == '__main__':
    main()