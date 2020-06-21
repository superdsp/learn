# coding=utf-8
import turtle
import time #导入时间模块
 
turtle.pensize(5) #改变画笔尺寸pensize()或width()
turtle.pencolor("yellow")
turtle.fillcolor("red")
 
turtle.begin_fill()
for _ in range(6):
    turtle.forward(100)
    turtle.right(124)
turtle.end_fill()
time.sleep(2)
 
turtle.penup() #提起笔移动，不绘制图形，用于另起一个地方绘制,一般与goto搭配使用
turtle.goto(-150, -120)
turtle.color("violet") #设置笔的颜色
turtle.write("Done", font=('Arial', 40, 'normal'))
 
turtle.mainloop()