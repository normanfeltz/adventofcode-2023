numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

with open('input.txt') as file:
    sum = 0

    for line in file.read().split('\n'):
        firstIndex = None
        firstInt = None

        endIndex = None
        endInt = None

        print(line)

        for key in numbers.keys():
            findIndex = line.find(key)

            if findIndex >= 0 and (firstIndex is None or firstIndex > findIndex):
                firstIndex = findIndex
                firstInt = numbers[key]

            rfindIndex = line.rfind(key)

            if rfindIndex >= 0 and (endIndex is None or endIndex < rfindIndex):
                endIndex = rfindIndex
                endInt = numbers[key]

        totalInt = firstInt * 10 + endInt
        sum += totalInt

        print(totalInt)
        print()

    print(sum)