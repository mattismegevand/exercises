from functools import cache

inp = tuple(open('7.in').read().splitlines())
s1 = set()
seen = set()

def f1(inp, i, j):
    if (i, j) in seen:
        return
    seen.add((i, j))
    if not(0 <= i < len(inp) and 0 <= j < len(inp[0])):
        return
    if inp[i][j] == '^':
        s1.add((i, j))
        f1(inp, i + 1, j - 1)
        f1(inp, i + 1, j + 1)
        return
    f1(inp, i + 1, j)

@cache
def f2(inp, i, j):
    if not(0 <= i < len(inp) and 0 <= j < len(inp[0])):
        return 1
    if inp[i][j] == '^':
        return f2(inp, i + 1, j - 1) + f2(inp, i + 1, j + 1)
    return f2(inp, i + 1, j)

f1(inp, 0, inp[0].index('S'))
part1 = len(s1)
part2 = f2(inp, 0, inp[0].index('S'))
print(part1)
print(part2)
