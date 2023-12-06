import re

def isSymbol(char):
    return not re.search(r"[0-9.]", char)

with open('input.txt') as file:
    sum = 0

    lines = file.readlines()

    for i in range(0, len(lines)):
        currentLine = lines[i].strip()
        previousLine = lines[i-1].strip() if i > 0 else None
        nextLine = lines[i+1].strip() if i < len(lines)-1 else None

        validNumber = False
        currentNumber = ''

        for j in range(0, len(currentLine)):
            char = currentLine[j]

            if char.isdigit():
                currentNumber += char

                if validNumber:
                    continue

                if previousLine is not None and isSymbol(previousLine[j]) or nextLine is not None and isSymbol(nextLine[j]):
                    validNumber = True
                elif j > 0 and (isSymbol(currentLine[j-1]) or previousLine is not None and isSymbol(previousLine[j-1]) or nextLine is not None and isSymbol(nextLine[j-1])):
                    validNumber = True
                elif j < len(currentLine)-1 and (isSymbol(currentLine[j+1]) or previousLine is not None and isSymbol(previousLine[j+1]) or nextLine is not None and isSymbol(nextLine[j+1])):
                    validNumber = True
            else:
                if validNumber:
                    sum += int(currentNumber)

                validNumber = False
                currentNumber = ''

        if validNumber:
            sum += int(currentNumber)

    print(sum)