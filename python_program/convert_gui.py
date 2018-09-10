from graphics import *

def main():
    win=GraphWin("温度转换")
    win.setCoords(0.0,0.0,3.0,4.0)

    Text(Point(1,3),"摄氏度：").draw(win)
    Text(Point(1,1),"华氏度：").draw(win)
    inputText=Entry(Point(2.25,3),5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText=Text(Point(2.25,1),"")
    outputText.draw(win)
    button=Text(Point(1.5,2.0),"转换")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)

    win.getMouse()

    celsius=float(inputText.getText())
    f=9.0/5.0*celsius+32

    outputText.setText(round(f,2))
    button.setText("quit")

    win.getMouse()
    win.close()

main()
