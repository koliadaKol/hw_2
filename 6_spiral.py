import turtle
import math


turtle.speed(0)
def spiral(n, h = 10 , m = 60, r=10):
    for i in range(n):
        for _ in range(m):
            r +=1
            a = 2*r*math.sin(math.pi/m)
            turtle.forward(a)
            turtle.right(360/m)

if __name__ == "__main__":
    turtle.shape('turtle')
    spiral(10)