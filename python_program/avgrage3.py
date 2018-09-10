#哨兵循环 0作为边界‘哨兵’

def main():
    total=0.0
    count=0
    x=float(input("Enter a number (nagative to quit)>>"))
    while x>=0:
        total=total+x
        count=count+1
        x=float(input("Enter a number (nagative to quit)>>"))
    print("\nThe avgerage of th number is ",total/count)

main()

    
