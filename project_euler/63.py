#!/usr/bin/env python

s = 0
for n in range(1, int(1e6)):
  for base in range(1, 10):
    p = base ** n
    if len(str(p)) == n:
      s += 1
  if len(str(9 ** n)) < n:
    break
  n += 1
print(s)
