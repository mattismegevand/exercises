#!/usr/bin/env python

total = 1
n = (1001 - 1) // 2
for i in range(1, n+1):
  total += 16*i**2 + 4*i + 4
print(total)
