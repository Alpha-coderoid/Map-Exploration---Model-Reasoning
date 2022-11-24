from tabulate import tabulate
map = [[' ', ' ', ' '], [' ', ' ', ' ']]
# print(tabulate(map))
for i in range(len(map)):
    print(map[i])
# print(map[0])
print(map[0][4])
# print(map[1][1][1])
size = input()
while (True):
    inp = input()
    if inp == 'start':
        break
    inp = inp.split()
    inp = [eval(i) for i in inp]
    loc = (int(inp[0])*size)+int(inp[1])
    map[loc][0] = inp[2]
    for i in range(len(map)):
        print(map[i])
