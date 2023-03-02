from pathlib import Path
import re

input = Path(__file__).parents[0] / "input.txt"

def printStacks():
    print('1: ', stack_1)
    print('2: ', stack_2)
    print('3: ', stack_3)
    print('4: ', stack_4)
    print('5: ', stack_5)
    print('6: ', stack_6)
    print('7: ', stack_7)
    print('8: ', stack_8)
    print('9: ', stack_9)

def findColumns(lines):
    lineNum = 0
    for line in lines:
        lineNum += 1
        # For each line, check if line contains the string
        if ' 1   2   3' in line:
            return lineNum or False


with open(input, 'r') as f:
    lines = f.readlines()
    
    lineNum = findColumns(lines)

    #Find the largest number
    largestNumber = max(map(int,lines[lineNum - 1].split()))

    #Create list with largest number elements
    columnLocations = [None]*largestNumber
    print(columnLocations)
    currCol = 0
    for i,char in enumerate(lines[lineNum - 1]):
        if char.isnumeric():
            columnLocations[currCol] = i
            currCol += 1

    print('Line numbers on: ', lineNum)
    print(lines[lineNum - 1])

    print('Column locations:')
    print(columnLocations)

    stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9 = [], [], [], [], [], [], [], [], []

    for i,line in enumerate(lines):
        if i == 9:
            break
        else:
            stack_1.append(line[columnLocations[0]])
            stack_2.append(line[columnLocations[1]])
            stack_3.append(line[columnLocations[2]])
            stack_4.append(line[columnLocations[3]])
            stack_5.append(line[columnLocations[4]])
            stack_6.append(line[columnLocations[5]])
            stack_7.append(line[columnLocations[6]])
            stack_8.append(line[columnLocations[7]])
            stack_9.append(line[columnLocations[8]])
    
    stacks = []
    stacks.append(stack_1)
    stacks.append(stack_2)
    stacks.append(stack_3)
    stacks.append(stack_4)
    stacks.append(stack_5)
    stacks.append(stack_6)
    stacks.append(stack_7)
    stacks.append(stack_8)
    stacks.append(stack_9)
    
    for stack in stacks:
        while(" " in stack):
            stack.remove(" ")
        stack.pop()
        # print(stack)

    # printStacks()
    # ============================================

    lines = lines[largestNumber + 1:]

    for i,line in enumerate(lines):
        quantity, source, destination = [int(s) for s in line.split() if s.isdigit()]
        print(quantity, source, destination)

        source = eval('stack_{0}'.format(source))
        destination = eval('stack_{0}'.format(destination))

        for move in range(quantity):
            popped = source.pop(0)
            destination.insert(0,popped)

        # printStacks()

output = ''
for stackNum in range (1,9):
    output += eval('stack_{0}'.format(stackNum))[0]

print(output)