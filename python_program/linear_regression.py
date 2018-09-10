#线性回归曲线

from graphics import *

def handleKey(key,win):
    pass

def handleMouse(pt,win):
    if 2.0<pt.getX()<3.0 and 0.0<pt.getY()<0.5:
        print(pt.getX(),pt.getY())
        return False
    else:
        pt.draw(win)
        return True

def drawline(x,y,m,win):
    print(x,y,m)
    line=Line(Point(0.0,y-m*x),Point(3.0,y+m*(3.0-x)))
    line.draw(win)

def main():
    win = GraphWin("Linear Regression",500,500)
    win.setCoords(0.0,0.0,3.0,4.0)
    
    Rectangle(Point(2,0.0),Point(3,0.5)).draw(win)
    Text(Point(2.5,0.25),"Done").draw(win)

    sumx=0.0
    sumy=0.0
    sumx2=0.0
    sumxy=0.0
    count=0
    
    while True:
        key =win.checkKey()
        if key=="q":
            break
        if key:
            handleKey(key,win)
        pt=win.checkMouse()
        if pt:
            if(handleMouse(pt,win)): #点击有效区域
                count=count+1
                sumx=pt.getX()+sumx
                sumy=pt.getY()+sumy
                sumx2=pt.getX()**2+sumx2
                sumxy=pt.getX()*pt.getY()+sumxy
            else:#点击完成
                avgx=sumx/count
                avgy=sumy/count
                m=(sumxy-count*avgx*avgy)/(sumx2-count*avgx**2)
                drawline(avgx,avgy,m,win)
                win.getMouse()
                break
                
    win.close()
main()
