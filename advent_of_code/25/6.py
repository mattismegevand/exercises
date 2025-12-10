from math import prod

inp = open('6.in').read().splitlines()
numbers = [tuple(map(int, (c for c in l.split(' ') if c))) for l in inp[:-1]]
transposed = list(zip(*numbers))
ops = list(c for c in inp[-1].split(' ') if c)
part1 = sum(
    sum(transposed[i]) if o == '+' else prod(transposed[i])
    for i, o in enumerate(ops)
)

inp = inp[:-1]
transposed = []
l = []
for i in range(len(inp[0])):
    s = "".join(inp[j][i] for j in range(len(inp))).strip()
    if s:
        l.append(int(s))
    else:
        transposed.append(l)
        l = []
transposed.append(l)
part2 = sum(
    sum(transposed[i]) if o == '+' else prod(transposed[i])
    for i, o in enumerate(ops)
)

print(part1)
print(part2)

