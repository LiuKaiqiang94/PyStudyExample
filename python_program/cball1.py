#炮弹下落问题，抛物线问题
from math import sin,cos,radians

def main():
    angle=float(input("Enter the launch angle(in degrees):"))
    vel=float(input("Enter the initial velocaty (in meters/sec):"))
    h0=float(input("Enter the initial height (in meters):"))
    time=float(input("Enter tehe time interval between position calculations:"))

    theta=radians(angle)

    xpos=0
    ypos=h0
    xvel=vel*cos(theta)
    yvel=vel*sin(theta)

    while ypos >=0.0:
        xpos=xpos+time*xvel
        yvel1=yvel-time*9.8
        ypos=ypos+time*(yvel+yvel1)/2.0
        yvel=yvel1
    print("\nDistance travled:{0:0.1f} meters.".format(xpos))

main()
