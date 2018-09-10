# -*- coding: utf-8 -*-
from math import *
from turtle import *
from graphics import *
 
 
def main():
    #创建窗口对象，默认为200*200px，（0,0）表示屏幕左上角
    win=GraphWin()
 
    #画点
    p1=Point(100,100)
    p1.draw(win)
 
    #画圆，以p1为圆心，半径为100
    circ=Circle(p1,100)
    circ.draw(win)
    circ.setOutline("red")#外围轮廓颜色
    circ.setFill("yellow")#填充颜色
 
    #画线
    line=Line(Point(650,100),Point(250,100))
    line.draw(win)
 
    #在p1点上显示文字
    message=Text(p1,"圆心")
    message.draw(win)
     
main()
