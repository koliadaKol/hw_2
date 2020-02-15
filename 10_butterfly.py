import turtle

turtle.speed(0)
def circle(n=3):
    turtle.shape('turtle')
    for j in range (10):
        for i in range(180):
            turtle.forward(n)
            turtle.left(2)
        for i in range(180):
            turtle.forward(n)
            turtle.right(2)
        n += 1

if __name__ == "__main__":
    circle()
    turtle.done()