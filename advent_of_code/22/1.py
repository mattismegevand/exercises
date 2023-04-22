#!/usr/bin/env python

chunks = open("1.in").read().strip().split("\n\n")
cals = sorted([sum(map(int, c.split())) for c in chunks], reverse=True)

print(cals[0])
print(sum(cals[:3]))
