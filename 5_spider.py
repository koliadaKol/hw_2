import turtle

turtle.speed(10)
def circle():
    turtle.shape('turtle')
    n=1000
    for i in range(n):
        turtle.left(360/n)
        turtle.forward(100)
        turtle.backward(100)
if __name__ == "__main__":
    circle()
    while True:
        pass