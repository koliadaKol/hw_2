import turtle

turtle.speed(0)
def circle():
    turtle.shape('turtle')
    x = 2
    for j in range(x):
        for i in range(360):
            turtle.forward(2)
            turtle.right(1)
        for i in range(360):
            turtle.forward(2)
            turtle.left(1)
        if x == 2:
            turtle.right(90)
        else:
            turtle.right(360/x)

if __name__ == "__main__":
    circle()
    while True:
        pass