#!/usr/bin/env python

names = open("data/0022_names.txt").read().replace('"', '').split(",")
names.sort()
print(sum(sum(ord(c) - ord('A') + 1 for c in name) * (i + 1) for i, name in enumerate(names)))
