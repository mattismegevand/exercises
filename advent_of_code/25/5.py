ranges, ids = [p.splitlines() for p in open('5.in').read().split('\n\n')]
ranges = sorted(tuple(map(int, t.split('-'))) for t in ranges)
ids = list(map(int, ids))

part1 = part2 = 0
for id in ids:
    for a, b in ranges:
        if id in range(a, b + 1):
            part1 += 1
            break
c = -1
for a, b in ranges:
    if c >= a:
        a = c + 1
    if a <= b:
        part2 += b - a + 1
    c = max(c, b)
print(part1)
print(part2)
