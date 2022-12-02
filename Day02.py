from enum import Enum

class RPS(Enum):
    A = 1 #Rock
    B = 2 #Paper
    C = 3 #Scissors
    X = 1 #Rock
    Y = 2 #Paper
    Z = 3 #Scissors

class Game(Enum):
    X = 0 #Lose
    Y = 3 #Draw
    Z = 6 #Win

#PartOne Calculation
def CalcScore(enemie, me) -> int:
    status = 0
    if RPS[enemie] == RPS[me]:
        status = 3
    elif RPS[enemie].value == 1 and RPS[me].value == 3:
        status = 0
    elif RPS[enemie].value == 3 and RPS[me].value == 1:
        status = 6
    elif RPS[enemie].value > RPS[me].value:
        status = 0
    else:
        status = 6
    return status + RPS[me].value

#PartTwo Calculation
def GameCalc(enemie, winStatus) -> int:
    if(Game[winStatus] == Game.Y):
        return RPS[enemie].value + Game[winStatus].value
    elif(Game[winStatus] == Game.Z):
        return (RPS[enemie].value % 3) + 1 + Game[winStatus].value
    else:
        return RPS[enemie].value - 1 + Game[winStatus].value if RPS[enemie].value > 1 else RPS[enemie].value + 2 + Game[winStatus].value

with open('Inputs/input02.txt', "r") as f:
    lines = f.readlines()

def PartOne():
    result = 0
    for line in lines:
        splits = line.split()
        result += CalcScore(splits[0], splits[1])
    print(f"PartOne: {result}")

#X = Lose, Y = Draw, Z = Win
def PartTwo():
    result = 0
    for line in lines:
        splits = line.split()
        result += GameCalc(splits[0], splits[1])
    print(f"PartTwo: {result}")
    
PartOne()
PartTwo()