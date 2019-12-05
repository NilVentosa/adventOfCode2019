import math

def calculateFuel(w):
    return math.floor(w/3) - 2


def allFuel(w):
    result = 0
    thing = w
    while calculateFuel(thing) > 0:
        result = result + calculateFuel(thing)
        thing = calculateFuel(thing)
    return result

with open('input1') as f:
    result = 0
    for line in f:
        result = result + allFuel(int(line))
    print(result)
