import shapely

inp = [tuple(map(int, l.split(','))) for l in open('9.in').read().splitlines()]

def area(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

part1 = float('-inf')
for i, a in enumerate(inp):
    for j, b in enumerate(inp[i + 1:]):
        if i == j:
            continue
        part1 = max(part1, area(a, b))

polygon = shapely.Polygon(inp)
part2 = float('-inf')
for i, a in enumerate(inp):
    for j, b in enumerate(inp[i + 1:]):
        if i == j:
            continue
        x1, y1 = a
        x2, y2 = b
        box = shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if not shapely.contains(polygon, box):
            continue
        part2 = max(part2, area(a, b))

print(part1)
print(part2)
