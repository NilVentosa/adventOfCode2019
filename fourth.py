small = 197487
big = 673251

# Given small and big numbers finds amount that comply with the rules
def findThem(s, b):
    result = []
    numArray = getArray(s, b)
    for item in numArray:
        if sixDigits(item) and adjecentTwo(item) and increase(item):
            result.append(item)

    return(len(result))

# given small and big number returns array of arrays of the digits of each number
def getArray(s, b):
    thing = []
    for i in range(s, b+1):
        n = []
        for j in range(len(str(i))):
            n.append(int(str(i)[j]))
        thing.append(n)
    return thing

# returns True if number array has 6 elements
def sixDigits(numArray):
    if len(numArray) == 6:
        return True
    else:
        return False

# returns true if there are at least two adjecent numbers with sme value
def adjecent(numArray):
    for i in range(len(numArray)-1):
        if numArray[i] == numArray[i+1]:
            return True

# returns true if the digits are in increasing order
def increase(numArray):
    for i in range(len(numArray)-1):
        if numArray[i] > numArray[i+1]:
            return False
    return True

# for the second part there has to be at least one instance with the adjecent numbers being no more than two
def adjecentTwo(numArray):
    for item in numArray:
        if numArray.count(item) == 2:
            return True


print(findThem(small,big))
