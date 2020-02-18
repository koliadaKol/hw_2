import turtle

turtle.speed(100)
def flower():
    turtle.shape('turtle')

    x =20
    for j in range(x):
        for i in range(180):
            turtle.forward(3)
            turtle.right(2)
        for i in range(180):
            turtle.forward(3)
            turtle.left(2)
        if x == 2:
            turtle.right(90)
        else:
            turtle.right(360/x/2)
        00
if __name__ == "__main__":
    flower()
    turtle.done()