def getDataPairs(data):
    data_pairs = []
    for item in data:
        data_pairs.append(item.rstrip().split(')'))
    return data_pairs

def getFirsts(dataPairs):
    notFirsts = []
    for item in dataPairs:
        for pair in dataPairs:
            if item[0] == pair[1]:
                notFirsts.append(item)
                break
    firsts =  list(set(dataPairs).difference(notFirsts))

    return firsts

if __name__ == '__main__':
    data = open('input6test')
    dataPairs = getDataPairs(data)
    firsts = getFirsts(dataPairs)
    print(firsts)
