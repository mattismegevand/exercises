#!/usr/bin/env python3

import re

data = open("3.in", "r").read().strip()

do_or_dont = list(re.finditer(r"(?:do(?:n't)?\(\))", data))
do = True
part1 = 0
part2 = 0
for m in re.finditer(r'mul\((\d+),(\d+)\)', data):
    start = m.start()
    for match in do_or_dont:
        if match.start() < start:
            do = match.group() == 'do()'
        else:
            break
    l = m.group().split(',')
    v = int(l[0][4:]) * int(l[1][:-1])
    part1 += v
    if do: part2 += v
print(part1)
print(part2)

