#!/usr/bin/env python

from itertools import permutations

divs = [2, 3, 5, 7, 11, 13, 17]
s = 0
for n in permutations(range(10)):
  for i, d in enumerate(divs):
    if (100*n[i+1] + 10*n[i+2] + n[i+3]) % d != 0:
      break
  else: s += int(''.join(str(i) for i in n))
print(s)
