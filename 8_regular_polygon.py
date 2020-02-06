import turtle


def reguolar_polygon():
    turtle.shape('turtle')
    x =  3
    for i in range(10):
        for i in range(x):
            turtle.left(360 /-x)
            turtle.forward(20)

        x = x +1
        turtle.right(90)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()

if __name__ == "__main__":
    reguolar_polygon()
    while True:
        pass