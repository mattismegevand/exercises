#!/usr/bin/env python

from collections import defaultdict
from functools import reduce

MAX = {'red': 12, 'green': 13, 'blue': 14}

def process(sets):
    cubes = [m.split(", ") for m in sets]
    is_possible = True
    min_needed = defaultdict(lambda: 1) 
    for c in cubes:
        for cc in c:
            n, color = cc.split(" ")
            n = int(n)
            if n > MAX[color]:
                is_possible = False
            min_needed[color] = max(min_needed[color], n)
    return is_possible, min_needed.values()

with open("2.in") as f:
    p1, p2 = 0, 0
    for l in f:
        l = l.strip()
        game_id, game = l.split(": ")
        sets = game.split("; ")
        is_possible, min_needed = process(sets)
        p1 += int(game_id[5:]) * is_possible
        p2 += reduce(lambda x, y: x * y, min_needed, 1)
    print(p1)
    print(p2)