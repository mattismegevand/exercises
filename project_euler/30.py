#!/usr/bin/env python

def digit_fifth_powers(n):
  return sum(int(c) ** 5 for c in str(n))

print(sum(i for i in range(2, 1000000) if i == digit_fifth_powers(i)))
