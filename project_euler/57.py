#!/usr/bin/env python

c = 0
n = d = 1
for i in range(1, 1001):
  n, d = 2 * d + n, n + d
  if len(str(n)) > len(str(d)):
    c += 1
print(c)
