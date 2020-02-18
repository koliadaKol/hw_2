import turtle

turtle.speed(100)
def flower():
    turtle.shape('turtle')
    c = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    x =5
    n = 0
    for j in range(x):

        for i in range(180):
            turtle.forward(3)
            turtle.right(2)
        turtle.color(c[n])
        for i in range(180):
            turtle.forward(3)
            turtle.left(2)
        if x == 2:
            turtle.right(90)
        else:
            turtle.right(360/x/2)
        n +=1
        if n == 7:
            n = 0

if __name__ == "__main__":
    flower()
    turtle.done()