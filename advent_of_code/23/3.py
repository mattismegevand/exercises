#!/usr/bin/env python

symbols = set() 
gears = dict()

def convert(c, coord):
    if c.isdigit():
        return int(c)
    if c != ".":
        symbols.add(coord)
        if c == "*":
            gears[coord] = []
    return -1 

def is_part(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

def process_number(digits, cell, coord):
    digits["d"] += str(cell)
    for s in symbols:
        if is_part(s, coord):
            digits["is_part"] = True
            if s in gears:
                digits["close_gears"].add(s)
    return digits

def process_symbol(digits):
    global p1
    if digits["is_part"]:
        p1 += int(digits["d"])
        for cg in digits["close_gears"]:
            gears[cg].append(int(digits["d"]))
    return {"d": "", "is_part": False, "close_gears": set()}

lines = [[convert(c, (i, j)) for j, c in enumerate(l)] for i, l in enumerate(open("3.in").read().strip().splitlines())]
digits = {"d": "", "is_part": False, "close_gears": set()}
p1, p2 = 0, 0
for i, l in enumerate(lines):
    for j, cell in enumerate(l):
        digits = process_number(digits, cell, (i, j)) if cell != -1 else process_symbol(digits)
    digits = process_symbol(digits)

for g in gears.values():
    if len(g) == 2:
        p2 += g[0] * g[1]

print(p1)
print(p2)
