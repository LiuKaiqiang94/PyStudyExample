
from graphics import *

def drawYear(win,year,height):
    bar=Rectangle(Point(year,0),Point(year+1,height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

def main():
    print("This program plots the growth of a 10-year investment.")

    principal=float(input("Enter the inital princial:"))
    apr=float(input("Enter the annualized interest rate:"))

    win=GraphWin("Investment Growth Chart",320,240)
    win.setBackground("white")
    win.setCoords(-1.75,-200,11.5,10400)

    Text(Point(-1,0),"0.0K").draw(win)
    Text(Point(-1,2500),"2.5K").draw(win)
    Text(Point(-1,5000),"5.0K").draw(win)
    Text(Point(-1,7500),"7.5K").draw(win)
    Text(Point(-1,10000),"10.0K").draw(win)

    drawYear(win,0,principal)

    for year in range(1,11):
        principal = principal * (1 + apr)
        drawYear(win,year,principal)
    input("Press <Enter> to quit.")
    win.close()

main()
