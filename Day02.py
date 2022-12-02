from enum import Enum

class RPS(Enum):
    ROCK = 0
    PAPER = 1
    Scissors = 2

class Game(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

#region Enums
def RPSEnum(input) -> RPS:
    if(input == 'A' or input == 'X'): return RPS.ROCK
    elif(input == 'B' or input == 'Y'): return RPS.PAPER
    elif(input == 'C' or input == 'Z'): return RPS.Scissors

def GameEnum(input) -> Game:
    if(input == 'X'): return Game.LOSE
    elif(input == 'Y'): return Game.DRAW
    elif(input == 'Z'): return Game.WIN

#endregion

#region Calculations
#PartOne Calculation
def CalcScore(enemy, me) -> int:
    status = 0
    if RPS(enemy) == RPS(me):
        return Game.DRAW.value + RPS(me).value + 1
    elif ((RPS(me).value + 2) % 3) == RPS(enemy).value:
        return Game.WIN.value + RPS(me).value + 1
    else:
        return Game.LOSE.value + RPS(me).value + 1

#PartTwo Calculation
def GameCalc(enemy, winStatus) -> int:
    if(Game(winStatus) == Game.DRAW):
        return RPS(enemy).value + Game(winStatus).value + 1
    elif(Game(winStatus) == Game.WIN):
        return ((RPS(enemy).value + 1) % 3) + Game(winStatus).value + 1
    else:
        return ((RPS(enemy).value + 2) % 3) + Game(winStatus).value + 1
#endregion

with open('Inputs/input02.txt', "r") as f:
    lines = f.readlines()

def PartOne():
    result = 0
    for line in lines:
        splits = line.split()
        result += CalcScore(RPSEnum(splits[0]), RPSEnum(splits[1]))
    print(f"PartOne: {result}")

#X = Lose, Y = Draw, Z = Win
def PartTwo():
    result = 0
    for line in lines:
        splits = line.split()
        result += GameCalc(RPSEnum(splits[0]), GameEnum(splits[1]))
    print(f"PartTwo: {result}")
    
PartOne()
PartTwo()