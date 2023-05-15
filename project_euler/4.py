#!/usr/bin/env python

best = float('-inf')
for a in range(999, 99, -1):
  for b in range(999, a-1, -1):
    c = a * b
    if c <= best:
      break
    if str(c) == str(c)[::-1]:
      best = c
print(best)
