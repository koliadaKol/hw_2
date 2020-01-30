import turtle

turtle.speed(100)
def circle():
    turtle.shape('turtle')
    for i in range(360):
        turtle.forward(3)
        turtle.right(1)


if __name__ == "__main__":
    circle()
    while True:
        pass