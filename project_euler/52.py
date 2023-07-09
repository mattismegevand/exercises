#!/usr/bin/env python

def same_digits(n, m):
  return sorted(str(n)) == sorted(str(m))

n = 2
while True:
  is_valid = True
  for i in range(2, 7):
    if not same_digits(n, n * i):
      is_valid = False
      break
  if is_valid:
    print(n)
    break
  n += 1
