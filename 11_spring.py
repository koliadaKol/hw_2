import turtle

turtle.speed(0)
def spring():
    turtle.shape('turtle')
    turtle.left(90)
    for j in range(5):
        for i in range(180):
            turtle.right(1)
            turtle.forward(3)
        for i in range(90):
            turtle.right(2)
            turtle.forward(2)


if __name__ == "__main__":
    spring()
    turtle.done()