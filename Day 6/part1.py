import re

with open('input.txt') as file:
    times = re.search(r"Time: +(\d+) +(\d+) +(\d+) +(\d+)\n", file.readline()).groups()
    distances = re.search(r"Distance: +(\d+) +(\d+) +(\d+) +(\d+)", file.readline()).groups()

    if len(times) != len(distances):
        print("Error ! 'times' and 'distances' have not the same size")

    sum = 1
    for i in range(0, len(times)):
        count = 0

        time = int(times[i])
        distance = int(distances[i])

        for x in range(1, time):
            d = (time - x) * x

            if d > distance:
                count += 1

        sum *= count

    print(sum)