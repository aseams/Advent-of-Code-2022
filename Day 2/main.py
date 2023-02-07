inputFile = open("./Day 2/input.txt", "r")

inputValues = inputFile.read().split("\n")

overallScore = 0

def getPoints(input):
    if(input == "Y"):
        return 2
    elif(input == "X"):
        return 1
    elif(input == "Z"):
        return 3
    else:
        return 0

def toWin(input):
    if(input == "C"):
        return "X"
    elif(input == "B"):
        return "Z"
    elif(input == "A"):
        return "Y"

def toLose(input):
    if(input == "C"):
        return "Y"
    elif(input == "B"):
        return "X"
    elif(input == "A"):
        return "Z"

def isTie(input):
    if(input == "C"):
        return "Z"
    elif(input == "B"):
        return "Y"
    elif(input == "A"):
        return "X"

for game in inputValues:
    valuesFormatted = game.split(" ")

    opponent = valuesFormatted[0]
    response = valuesFormatted[1]

    if(isTie(opponent) == response):
        # Draw
        overallScore += getPoints(response) + 3
    else:
        if(toWin(opponent) == response):
            # Best response to opponent
            overallScore += getPoints(response) + 6
        else:
            # Worst response to opponent
            overallScore += getPoints(response)
print(overallScore)

overallScore = 0

for game in inputValues:
    valuesFormatted = game.split(" ")

    opponent = valuesFormatted[0]
    response = valuesFormatted[1]
    
    if (response == "Y"):
        response = isTie(opponent)
    elif (response == "X"):
        response = toLose(opponent)
    elif (response == "Z"):
        response = toWin(opponent)

    if(isTie(opponent) == response):
        # Draw
        overallScore += getPoints(response) + 3
    else:
        if(toWin(opponent) == response):
            # Best response to opponent
            overallScore += getPoints(response) + 6
        else:
            # Worst response to opponent
            overallScore += getPoints(response)
print(overallScore)
