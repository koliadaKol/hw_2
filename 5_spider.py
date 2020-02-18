import turtle

turtle.speed(0)


def circle():
    turtle.shape('turtle')
    n=1000
    c = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.color(c[i% 6])


if __name__ == "__main__":
    circle()
    turtle.done()