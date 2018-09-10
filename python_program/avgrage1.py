
def main():
    n=int(input("How many numbers do you have?"))
    total = 0.0
    for i in range(n):
        x=int(input("Enter a number >>"))
        total=total+x
    print("\nThe avgrage of the numbers is ",total/n)

main()
