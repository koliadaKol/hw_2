import turtle


def rect_spiral():
    x=20
    turtle.shape('turtle')
    for j in range(360):
        for i in range(1):
            turtle.forward(x)
            turtle.right(90)
        x = x + 10

if __name__ == "__main__":
    rect_spiral()
    while True:
        pass