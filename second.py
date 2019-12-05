initial_data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0'

goal=19690720

def doTheThing(lst, noun, verb):
    data_list = [int(item) for item in lst.split(',')]
    data_list[1]=noun
    data_list[2]=verb
    i = 0
    while i != 99:
        if data_list[i] == 1:
            data_list[data_list[i+3]] = data_list[data_list[i+1]]+data_list[data_list[i+2]]
            i = i+4
        elif data_list[i] == 2:
            data_list[data_list[i+3]] = data_list[data_list[i+1]]*data_list[data_list[i+2]]
            i = i+4
        elif data_list[i] == 99:
            return data_list[0]
        else:
            return 'Error'

for i in range(100):
    for j in range(100):
        if doTheThing(initial_data, i, j) == goal:
            print(100*i+j)
        
