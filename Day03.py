#PartOne
def findDifference(partOne, partTwo) -> int:
    for element in str(partOne):
        foundNumber = str(partTwo).find(element)
        if(foundNumber > -1):
            return PriorityCalc(element)

#PartTwo
def findBadge(partOne, partTwo, partThree) -> int:
    for element in str(partOne):
        if (str(partTwo).find(element) >= 0 and str(partThree).find(element) >= 0):
            return PriorityCalc(element)

def PriorityCalc(letter) -> int:
    asciiNumber = ord(letter)
    if(asciiNumber >= 97):
        return asciiNumber - 96
    else:
        return asciiNumber - 38

with open('Inputs/input03.txt', "r") as f:
    lines = f.readlines()

def PartOne():
    result = 0
    for line in lines:
        firstPart = slice(0, int((len(line) - 1)/2))
        secondPart = slice(int((len(line) - 1)/2), len(line)-1)
        result += findDifference(line[firstPart], line[secondPart])
    print(f"PartOne: {result}")

def PartTwo():
    result = 0
    for x in range(0, len(lines), 3):
        result += findBadge(lines[x], lines[x + 1], lines[x + 2])
    print(f"PartTwo: {result}")

PartOne()
PartTwo()