import re
import functools 

with open('input.txt') as file:
    sum = 0

    for line in file.read().split('\n'):
        (game, subsets) = line.split(': ')
        id = int(game.split(' ')[1])
        sets = subsets.split('; ')

        bag = {
            'red': None,
            'green': None,
            'blue': None
        }

        for set in sets:
            for cube in set.split(', '):
                (count, color) = re.search(r"(\d+) (red|green|blue)", cube).groups()

                if bag[color] is None or bag[color] < int(count):
                    bag[color] = int(count)

        sum += functools.reduce(lambda a, b: a * b, bag.values())

    print(sum)