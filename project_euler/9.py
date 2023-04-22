#!/usr/bin/env python

n = 1000
for c in range(n//3, n//2):
  for b in range((n-c)//2, c):
    a = n - b - c
    if c*c == a*a + b*b:
      print(a*b*c)
      exit(0)
