import turtle

turtle.speed(10)
def circle():
    turtle.shape('turtle')
    type1 = 10
    for i in range(10):
        for i in range(4):
            turtle.forward(type1)
            turtle.left(90)
        turtle.penup()
        turtle.right(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
        type1 = type1 + 40

if __name__ == "__main__":
    circle()
    while True:
        pass