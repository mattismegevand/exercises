#!/usr/bin/env python

def is_pandigital(n):
  return set(str(n)) == set('123456789')

best = float('-inf')
for n in range(1, 10000):
  s = ""
  i = 1
  while len(s) < 9:
    s += str(n * i)
    i += 1
  if len(s) == 9 and is_pandigital(int(s)):
    best = max(best, int(s))
print(best)
