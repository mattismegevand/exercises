#!/usr/bin/env python

from math import sqrt

def minimal_diophantine(D):
  P, Q, a = 0, 1, int(sqrt(D))
  x, y, lx, ly = a, 1, 1, 0
  while x * x - D * y * y != 1:
    P = a * Q - P
    Q = (D - P * P) // Q
    a = (P + int(sqrt(D))) // Q
    x, y, lx, ly = a * x + lx, a * y + ly, x, y
  return x

def max_x_value(limit):
  max_x, D_val = 0, 0
  for D in range(2, limit + 1):
    if int(sqrt(D))**2 == D: continue
    x = minimal_diophantine(D)
    if x > max_x:
      max_x, D_val = x, D
  return D_val

print(max_x_value(1000))
