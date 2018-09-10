
from graphics import *

def handleKey(key,win):
    if key=="w":
        win.setBackground("white")
    elif key=="g":
        win.setBackground("lightgray")
    elif key=="r":
        win.setBackground("pink")
    elif key == "b":
        win.setBackground("lightblue")

def handleClick(pt,win):
    entry=Entry(pt,10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key =="Return":break

    entry.undraw()
    typed=entry.getText()
    Text(pt,typed).draw(win)

    win.checkMouse()

def main():
    win=GraphWin("Click and Type",500,500)

    while True:
        key = win.checkKey()
        if key=="q":
            break
        if key:
            handleKey(key,win)
        pt=win.checkMouse()
        if pt:
            handleClick(pt,win)
    win.close()

main()
