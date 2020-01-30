import turtle


def rectangle():
    turtle.shape('turtle')
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)


if __name__ == "__main__":
    rectangle()
    while True:
        pass
