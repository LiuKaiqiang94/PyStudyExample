
from graphics import *
from inputdialog import InputDialog
from shottracker import ShotTracker

def main():
    win=GraphWin("Projectile Animation",640,480,autoflush=False)

    win.setCoords(-10,-10,210,155)

    Line(Point(-10,0),Point(210,0)).draw(win)

    for x in range(0,210,50):
        Text(Point(x,-5),str(x)).draw(win)
        Line(Point(x,0),Point(x,2)).draw(win)

    angle,vel,height=45.0,40.0,2.0
    
    while True:
        inputwin=InputDialog(angle,vel,height)
        choice=inputwin.interact()
        inputwin.close()

        if choice=="Quit":
            break

        angle,vel,height=inputwin.getValues()
        shot=ShotTracker(win,angle,vel,height)
        while 0<shot.getY() and -10<shot.getX()<=210:
            shot.update(1/100)
            update(50)
    win.close()

main()
