# 面向对象 筛子
from random import randrange

class MSDie:

    def __init__(self,sides):
        self.sides=sides
        self.value=1

    def roll(self):
        self.value=randrange(1,self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value=value
        
def main():
    die=MSDie(12)
    #die.setValue(5)
    print(die.getValue())
main()
