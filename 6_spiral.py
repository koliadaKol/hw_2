import turtle

turtle.speed(0)
def spiral():
    x = 1
    y = 1
    turtle.shape('turtle')
    for j in range(360):
        for i in range(180):
            turtle.goto(x,y)
            turtle.right(x)
        x = x + 10

if __name__ == "__main__":
    spiral()
    while True:
        pass