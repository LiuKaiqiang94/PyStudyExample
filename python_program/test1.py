import math
import graphics

def main():
    a= float(input("input a:"))
    b = float(input("input b:"))
    c = float(input("input c:"))
    discRoot=math.sqrt(b*b-4*a*c)
    root1=(-b+discRoot)/(2*a)
    root1=(-b-discRoot)/(2*a)
    print()
    print("a=",a,"b=",b)
    
def square():
    a=float(input("input a :"))
    b=float(input("input b :"))
    c=float(input("input c :"))
    s=(a+b+c)/2
    A=math.sqrt(s * (s - a ) * (s - b) * (s - c))
    print("square is ",A)

def graphicsTest():
    win=graphics.GrapWin()
    
graphicsTest()
