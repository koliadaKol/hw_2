import turtle


turtle.speed(0.001)
def rect_pig(i = 0):
    turtle.shape('turtle')


    turtle.begin_fill()
    for i in range(360):
        turtle.forward(3)
        turtle.right(1)
    turtle.color("red")
    turtle.end_fill()

    turtle.penup()
    turtle.color("red")
    turtle.goto(70, 15)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.end_fill()

    turtle.penup()
    turtle.color("red")
    turtle.goto(-70, 15)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.end_fill()


    turtle.penup()
    turtle.color("black")
    turtle.goto(-70, -80)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.color("white")
    turtle.end_fill()
    turtle.penup()
    turtle.color("black")
    turtle.goto(-70, -110)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(100, -80)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.color("white")
    turtle.end_fill()
    turtle.penup()
    turtle.color("black")
    turtle.goto(100, -110)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(10, -190)
    turtle.width(1.5)
    turtle.pendown()
    for i in range(340):
        turtle.forward(1)
        turtle.right(1.1)

    turtle.penup()
    turtle.width(1)
    turtle.color("black")
    turtle.goto(-10, -220)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(45, -220)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("white")
    turtle.goto(300, -300)

if __name__ == "__main__":
    rect_pig()
    turtle.done()
