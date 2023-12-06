import re

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as file:
    sum = 0

    for line in file.read().split('\n'):
        (game, subsets) = line.split(': ')
        id = int(game.split(' ')[1])
        sets = subsets.split('; ')

        possible = True

        for set in sets:
            for cube in set.split(', '):
                (count, color) = re.search(r"(\d+) (red|green|blue)", cube).groups()

                if bag[color] < int(count):
                    possible = False
                    break

        if possible:
            sum += id

    print(sum)