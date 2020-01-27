import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-t", help="how tall the tower is", type=int)
args = parser.parse_args()
tall = args.t
 
A = []
B = []
C = []
 
def print_all(A,B,C):
    print('A', A, '---', 'B', B, '---', 'C', C)
 
def reset_towers(num):
    del B[:]; del C[:]; del A[:]
    for i in range(num, 0, -1):
        A.append(i)
    print_all(A,B,C)
 
def move(num, origin, destination, auxiliary):
    if num == 1:
        destination.append(origin[-1])
        del origin[-1]
        print_all(A,B,C)
    if num > 1:
        move(num-1, origin, auxiliary, destination)
        move(1, origin, destination, auxiliary)
        move(num-1, auxiliary, destination, origin)
 
 
if tall <= 0:
    print('Place an argument that is a integer bigger than 0')
elif tall > 0:
    reset_towers(tall)
    move(tall, A, B, C)
