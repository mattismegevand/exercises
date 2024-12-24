#!/usr/bin/env python3

data = [list(map(int, l.split())) for l in open("2.in", "r").read().splitlines()]

def is_safe(r):
    is_inc = None
    for a, b in zip(r, r[1:]):
        diff = a - b
        if is_inc is None:
            is_inc = (diff < 0)
        if not(1 <= abs(diff) <= 3) or (diff < 0) != is_inc:
            return False
    return True

part1 = -1 
part2 = -1 
for l in data:
    safe = is_safe(l)
    part1 += safe
    if safe:
        part2 += safe
    else:
        part2 += any(is_safe(l[:i] + l[i+1:]) for i in range(len(l)))
print(part1)
print(part2)
