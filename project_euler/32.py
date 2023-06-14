#!/usr/bin/env python

def is_pandigital(a, b):
  s = str(a) + str(b) + str(a * b)
  return len(s) == 9 and set(s) == set('123456789')

pandigital = set(a * b for a in range(1, 100) for b in range(1, 10000) if is_pandigital(a, b))
print(sum(pandigital))
