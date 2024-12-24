#!/usr/bin/env python3

a, b = [], []
for l in open('1.in', 'r').read().splitlines():
    aa, bb = [int(t) for t in l.split()]
    a.append(aa)
    b.append(bb)
a.sort()
b.sort()

part1 = sum(abs(aa - bb) for aa, bb in zip(a, b))
part2 = sum(aa * b.count(aa) for aa in a)

print(part1)
print(part2)
