#!/usr/bin/env python

best = 0
best_p = 0
for p in range(2, 1001):
  c = 0
  for a in range(2, p // 3):
    if ((p * (p - 2 * a)) % (2 * (p - a))) == 0:
      c += 1
  if c > best:
    best = c
    best_p = p
print(best_p)
