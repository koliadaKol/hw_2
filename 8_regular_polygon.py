import turtle
import math

def polygon(R=10, n=3):
    a = 2*R*math.sin(math.pi/n)
    b = 180 - (180*(n-2)/2*n)
    print(b)
    alpha = 180*(n-2)/n
    gamma = 360/n
    turtle.left(b)
    for i in range (n):
        turtle.forward(a)
        turtle.left(gamma)

def reguolar_polygon():
    turtle.shape('turtle')
    polygon(50,6)
if __name__ == "__main__":
    reguolar_polygon()
    turtle.done()