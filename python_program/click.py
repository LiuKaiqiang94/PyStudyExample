from graphics import *

def main():
    win = GraphWin("Click Me")
    for i in range(10):
        p=win.getMouse()
        print("You click at :",i,p.getX(),p.getY())
    win.close()

main()
