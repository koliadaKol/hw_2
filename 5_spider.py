import turtle

turtle.speed(0)


def circle():
    turtle.shape('turtle')
    n=12
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)

if __name__ == "__main__":
    circle()
    while True:
        pass