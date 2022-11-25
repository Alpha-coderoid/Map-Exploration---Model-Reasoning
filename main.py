from tabulate import tabulate
import random


def add_surroundings(surround, x, y):
    if x > 0:
        map[x-1][y] += surround
    if x < size - 1:
        map[x+1][y] += surround
    if y > 0:
        map[x][y-1] += surround
    if y < size - 1:
        map[x][y+1] += surround


def generate_world():

    for i in range(size):
        for j in range(size):
            num = random.randrange(0, 100)
            if num >= 85 and num < 93:
                add_surroundings("B", i, j)
                map[i][j] = "P"
    x = random.randrange(0, size)
    y = random.randrange(0, size)
    add_surroundings("S", x, y)
    map[x][y] = "M"
    x = random.randrange(0, size)
    y = random.randrange(0, size)
    map[x][y] = "G"


def search_node(x, y):
    for node in fringe:
        if node[0] == x and node[1] == y:
            return node
    return 0


def expand(x, y):
    if x > 0:
        tmp = search_node(x-1, y)
        if tmp == 0:
            node = [x-1, y, 0, 0]
        else:
            node = tmp
        if map[x][y] == "~B":
            node[2] += 1
            node[3] -= 1
        if map[x][y] == "~S":
            node[2] -= 1
            node[3] += 1
        if map[x][y] == "~SB" or map[x][y] == "~BS":
            node[2] += 1
            node[3] += 1
        if tmp == 0:
            fringe.append(node)

    if x < size-1:

        tmp = search_node(x+1, y)
        if tmp == 0:
            node = [x+1, y, 0, 0]
        else:
            node = tmp
        if map[x][y] == "~B":
            node[2] += 1
            node[3] -= 1
        if map[x][y] == "~S":
            node[2] -= 1
            node[3] += 1
        if map[x][y] == "~SB" or map[x][y] == "~BS":
            node[2] += 1
            node[3] += 1
        if tmp == 0:
            fringe.append(node)

    if y > 0:

        tmp = search_node(x, y-1)
        if tmp == 0:
            node = [x, y-1, 0, 0]
        else:
            node = tmp
        if map[x][y] == "~B":
            node[2] += 1
            node[3] -= 1
        if map[x][y] == "~S":
            node[2] -= 1
            node[3] += 1
        if map[x][y] == "~SB" or map[x][y] == "~BS":
            node[2] += 1
            node[3] += 1
        if tmp == 0:
            fringe.append(node)

    if y < size-1:

        tmp = search_node(x, y+1)
        if tmp == 0:
            node = [x, y+1, 0, 0]
        else:
            node = tmp
        if map[x][y] == "~B":
            node[2] += 1
            node[3] -= 1
        if map[x][y] == "~S":
            node[2] -= 1
            node[3] += 1
        if map[x][y] == "~SB" or map[x][y] == "~BS":
            node[2] += 1
            node[3] += 1
        if tmp == 0:
            fringe.append(node)


map = []
size = int(input())
print("Do you want the program to generate a world for you? y/n")
if input() == "y":
    while input() != "start":
        map = [["~" for i in range(size)] for j in range(size)]
        generate_world()
        for row in map:
            print(row)
else:
    map = [["~" for i in range(size)] for j in range(size)]
    for row in map:
        print(row)
    while (True):
        inp = input()
        if inp == 'start':
            break
        inp = inp.split()
        map[int(inp[0])][int(inp[1])] = inp[2]
        if inp[2] == 'P':
            add_surroundings("B", int(inp[0]), int(inp[1]))
        if inp[2] == 'M':
            add_surroundings("S", int(inp[0]), int(inp[1]))
        for row in map:
            print(row)
print("Enter Start Position: ")
start = input()
start = start.split()
visited = []
fringe = []
fringe.append([start[0], start[1], 0, 0])
while True:
    min = 999
    for i in range(len(fringe)):
        priorty = 0
        pnn = [fringe[i][0], fringe[i][1]]
        if fringe[i][2] > 0:
            priorty += fringe[i][2]
        if fringe[i][3] > 0:
            priorty += fringe[i][3]
        if priorty < min and pnn not in visited:
            min = priorty
            index = i
    node = fringe.pop(index)
    print("current row: ", node[0], "current col: ", node[1])
    print("priority: ", priorty)
    if map[node[0]][node[1]] == "G":
        print("Goal Reached at: ", node[0], " , ", node[1], " !")
        break
    expand(node[0], node[1])
    visited.append([node[0], node[1]])
    for row in map:
        print(row)
    print("visited: ", visited)
    print("fringe: ", fringe)
    input()
