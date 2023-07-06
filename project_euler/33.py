#!/usr/bin/env python

dp = 1
np = 1
for c in range(1, 10):
  for d in range(1, c):
    for n in range(1, d):
      if (10 * n + c) * d == (10 * c + d) * n:
        dp *= d
        np *= n
print(dp // np)
