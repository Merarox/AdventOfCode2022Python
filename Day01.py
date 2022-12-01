with open('Inputs/input01.txt', "r") as f:
    lines = f.readlines()

calories = []
calorie = 0

for line in lines:
    if line == '\n':
        calories.append(calorie)
        calorie = 0
    else:
        calorie += int(line)

def PartOne():
    print(f"PartOne:")
    print(max(calories))

def PartTwo():
    print(f"PartTwo:")
    calories.sort(reverse=True)
    result = sum(calories[0:3])
    print(result)

PartOne()
PartTwo()