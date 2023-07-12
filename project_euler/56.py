#!/usr/bin/env python

best = float('-inf')
for a in range(100):
  for b in range(100):
    n = a**b
    best = max(best, sum(int(c) for c in str(n)))
print(best)
