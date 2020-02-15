import turtle

turtle.speed(0)
def smile():
    turtle.shape('turtle')
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(3)
        turtle.right(1)
    turtle.color("yellow")
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(-80,-80)
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
    turtle.goto(100,-80)
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
    turtle.color("red")
    turtle.goto(-120,-205)
    turtle.pendown()
    turtle.left(-90)
    turtle.width(20)
    for i in range(85):
        turtle.forward(4)
        turtle.left(2)

if __name__ == "__main__":
    smile()
    turtle.done()