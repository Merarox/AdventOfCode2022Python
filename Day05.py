import re

#PartOne Function
def moveCrate9000(amout, fromStack, toStack):
    for x in range(int(amout)):
        crate = stackList[int(fromStack) - 1].pop(0)
        stackList[int(toStack) - 1].insert(0, crate)

#PartTwo Function
def moveCrate9001(amout, fromStack, toStack):
    crates = []
    for x in range(int(amout)):
        crates.append(stackList[int(fromStack) - 1].pop(0))
    
    for i in range(len(crates), 0, -1):
        stackList[int(toStack) - 1].insert(0, str(crates[i - 1]))

#Load input
with open('Inputs/input05.txt', "r") as f:
    lines = f.readlines()

stackList = []
#Add the needed Lists to the List
for x in range(1, len(lines[0]), 4):
    stackList.append([])

def PartOne():
    for line in lines:
        if len(line) != 1 and line.replace(" ", "")[0] == '[':
            index = 0
            for x in range(1, len(line), 4):
                if line[x] != ' ':
                    stackList[index].append(line[x])
                index += 1
        elif line.startswith("move"):
            numbers = re.split('move|from|to', line.replace("\n", ""))
            moveCrate9000(numbers[1], numbers[2], numbers[3])
    resultOne = ""
    for stack in stackList:
        resultOne += stack[0]
    print(resultOne)

def PartTwo():
    for line in lines:
        if len(line) != 1 and line.replace(" ", "")[0] == '[':
            index = 0
            for x in range(1, len(line), 4):
                if line[x] != ' ':
                    stackList[index].append(line[x])
                index += 1
        elif line.startswith("move"):
            numbers = re.split('move|from|to', line.replace("\n", ""))
            print(numbers)
            moveCrate9001(numbers[1], numbers[2], numbers[3])
    resultTwo = ""
    for stack in stackList:
        resultTwo += stack[0]
    print(resultTwo)

#PartOne()
PartTwo()