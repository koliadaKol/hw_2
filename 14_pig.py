import turtle


turtle.speed(0.01)
def rect_pig(i = 0):
    turtle.shape('turtle')


    turtle.penup()
    turtle.color("black")
    turtle.goto(10, 70)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(130):
        turtle.forward(1)
        turtle.right(3)
    turtle.color("pink")
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(3)
        turtle.right(1)
    turtle.color("pink")
    turtle.end_fill()


    turtle.penup()
    turtle.color("black")
    turtle.goto(-80, -80)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.color("white")
    turtle.end_fill()
    turtle.penup()
    turtle.color("black")
    turtle.goto(-60, -100)
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
    turtle.goto(120, -100)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(10, -190)
    turtle.pendown()
    for i in range(340):
        turtle.forward(1)
        turtle.right(1.1)

    turtle.penup()
    turtle.color("black")
    turtle.goto(-20, -220)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(35, -220)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

if __name__ == "__main__":
    rect_pig()
    turtle.done()
