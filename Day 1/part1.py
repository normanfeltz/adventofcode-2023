
with open('input.txt') as file:
    sum = 0

    for line in file.read().split('\n'):
        firstInt = None
        endInt = None

        for char in line:
            if not char.isdigit():
                continue

            if firstInt is None:
                firstInt = int(char)
                endInt = int(char)
            else:
                endInt = int(char)

        sum += firstInt * 10 + endInt

    print(sum)