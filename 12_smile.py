import turtle

turtle.speed(1000)
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
    turtle.penup()





    turtle.color("black")
    turtle.goto(100,100)
    turtle.width(1)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(3)
        turtle.right(1)
    turtle.color("yellow")
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(120,120)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.color("white")
    turtle.end_fill()
    turtle.penup()
    turtle.color("black")
    turtle.goto(140, 100)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("black")
    turtle.goto(300,120)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
    turtle.color("white")
    turtle.end_fill()
    turtle.penup()
    turtle.color("black")
    turtle.goto(320, 100)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(1)
        turtle.right(3)
    turtle.end_fill()

    turtle.penup()
    turtle.color("red")
    turtle.goto(220,-40)
    turtle.pendown()

    turtle.left(-90)
    turtle.width(20)
    for i in range(85):
        turtle.forward(2)
        turtle.left(4)
    turtle.color("black")
    turtle.penup()
    turtle.goto(180, 160)
    turtle.width(60)
    turtle.pendown()
    turtle.left(29)
    turtle.forward(200)



    turtle.right(25)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-80, -80)
    turtle.width(60)
    turtle.pendown()
    turtle.left(29)
    turtle.forward(200)

if __name__ == "__main__":
    smile()
    turtle.done()