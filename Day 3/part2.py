
def isSymbol(char):
    return char == '*'

with open('input.txt') as file:
    gearRatios = dict()

    lines = file.readlines()

    for i in range(0, len(lines)):
        currentLine = lines[i].strip()
        previousLine = lines[i-1].strip() if i > 0 else None
        nextLine = lines[i+1].strip() if i < len(lines)-1 else None

        gear = None
        currentNumber = ''

        for j in range(0, len(currentLine)):
            char = currentLine[j]

            if char.isdigit():
                currentNumber += char

                if not gear is None:
                    continue

                if previousLine is not None and isSymbol(previousLine[j]):
                    gear = (i-1, j)
                elif nextLine is not None and isSymbol(nextLine[j]):
                    gear = (i+1, j)
                elif j > 0:
                    if isSymbol(currentLine[j-1]):
                        gear = (i, j-1)
                    elif previousLine is not None and isSymbol(previousLine[j-1]):
                        gear = (i-1, j-1)
                    elif nextLine is not None and isSymbol(nextLine[j-1]):
                        gear = (i+1, j-1)
                    elif j < len(currentLine)-1:
                        if isSymbol(currentLine[j+1]):
                            gear = (i, j+1)
                        elif previousLine is not None and isSymbol(previousLine[j+1]):
                            gear = (i-1, j+1)
                        elif nextLine is not None and isSymbol(nextLine[j+1]):
                            gear = (i+1, j+1)
            else:
                if not gear is None:
                    gearStr = f"{gear[0]},{gear[1]}"

                    if not gearStr in gearRatios.keys():
                        gearRatios[gearStr] = list()

                    gearRatios[gearStr].append(int(currentNumber))

                gear = None
                currentNumber = ''

        if not gear is None:
            gearStr = f"{gear[0]},{gear[1]}"

            if not gearStr in gearRatios.keys():
                gearRatios[gearStr] = list()

            gearRatios[gearStr].append(int(currentNumber))

    sum = 0

    for gearRatio in gearRatios.values():
        if len(gearRatio) == 2:
            (first, second) = gearRatio
            sum += first * second

    print(sum)