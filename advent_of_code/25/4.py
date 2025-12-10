from copy import deepcopy

inp = [list(l) for l in open('4.in').read().splitlines()]
I, J = len(inp), len(inp[0])

def f(inp):
    l = deepcopy(inp)
    n = 0
    for i in range(I):
        for j in range(J):
            if inp[i][j] == '.': continue
            acc = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == dj == 0: continue
                    if not(0 <= i + di < I and 0 <= j + dj < J): continue
                    if inp[i + di][j + dj] == '@':
                        acc += 1
            if acc < 4:
                n += 1
                l[i][j] = '.'
    return l, n

part1 = part2 = 0
while True:
    inp, n = f(inp)
    if n == 0:
        break
    if part1 == 0:
        part1 = n
    part2 += n
print(part1)
print(part2)
