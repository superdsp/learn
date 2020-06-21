# coding=utf-8
import time #导入时间模块
from turtle import *

def HSVtoRGB(hue,s,v):
    hi=int(hue/60)%6
    f=hue/60-hi
    p=v*(1-s)
    q=v*(1-f*s)
    t=v*(1-(1-f)*s)
    RGB=[0.0,0.0,0.0]
    if hi==0:
        RGB[0]=v; RGB[1]=t; RGB[2]=p
    elif hi==1:
        RGB[0]=q; RGB[1]=v; RGB[2]=p
    elif hi==2:
        RGB[0]=p; RGB[1]=v; RGB[2]=t
    elif hi==3:
        RGB[0]=p; RGB[1]=q; RGB[2]=v
    elif hi==4:
        RGB[0]=t; RGB[1]=p; RGB[2]=v
    elif hi==5:
        RGB[0]=v; RGB[1]=p; RGB[2]=q
    return RGB

def Rainbow():
    hue=0.0
    color(1,0,0)
    hideturtle()
    speed(100)
    pensize(3)
    penup()
    goto(-500,-500)
    pendown()
    right(110)
    for i in range(110):
        circle(1000)
        right(0.1)
        hue=hue+3
        RGB=HSVtoRGB(hue,1.0,1.0)
        color(RGB[0],RGB[1],RGB[2])
    penup()
    done()
Rainbow()