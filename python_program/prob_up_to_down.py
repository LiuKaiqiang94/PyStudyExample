#自顶向下的设计

from random import random

def main():
    printIntro()#打印介绍
    probA,probB,n=getInputs()#获取输入
    winsA,winsB=simNGames(n,probA,probB)#计算概率
    printSummary(winsA,winsB)#打印结果

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".The ability of each palyer is ')
    print("indicated by a probability (a number between o and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    a = float(input("What is the prob player A wins a serve?"))
    b = float(input("What is the prob player B wins a serve?"))
    #b=1-a
    n = int(input("How many games to simulate?"))
    return a, b, n

def simNGames(n,probA,probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA>scoreB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB

def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA=scoreA+1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB = scoreB+1
            else:
                serving="A"
    return scoreA,scoreB

def gameOver(a,b):
    return a==15 or b==15

def printSummary(winsA,winsB):
    n=winsA+winsB
    print("\nGames simulated:",n)
    print("Wins for A:{0}({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB,winsB/n))
