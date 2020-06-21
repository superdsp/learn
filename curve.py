
#绘制彩色螺旋线
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue","green"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 5])
    turtle.left(61)
turtle.tracer(True)
turtle.done()