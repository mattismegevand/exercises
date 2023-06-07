#!/usr/bin/env python

from itertools import permutations

for i, p in enumerate(permutations('0123456789')):
  if i + 1 == 1000000:
    print("".join(p))
    break
