import re

class Pairs:
    fromA = 0
    toA = 0
    fromB = 0
    toB = 0
    def __init__(self, a1, a2, b1, b2):
        self.fromA = a1
        self.toA = a2
        self.fromB = b1
        self.toB = b2



with open('Inputs/input04.txt', "r") as f:
    lines = f.readlines()

pairList = []

for line in lines:
    numbers = re.split(',|-', line)
    pairList.append(Pairs(int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])))

def PartOne():
    result = 0
    for pairElement in pairList:
        if((pairElement.fromA <= pairElement.fromB and pairElement.toA >= pairElement.toB) or (pairElement.fromA >= pairElement.fromB and pairElement.toA <= pairElement.toB)):
            result += 1
    print(f"PartOne: {result}")

def PartTwo():
    result = 0
    for pairElement in pairList:
        if((pairElement.fromA <= pairElement.fromB and pairElement.toA >= pairElement.fromB) or (pairElement.fromB <= pairElement.fromA and pairElement.toB >= pairElement.fromA)):
            result += 1
    print(f"PartTwo: {result}")

PartOne()
PartTwo()