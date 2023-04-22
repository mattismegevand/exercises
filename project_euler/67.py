#!/usr/bin/env python

from functools import cache

triangle = tuple(tuple(int(n) for n in line.split()) for line in open("data/p067_triangle.txt").read().strip().split('\n'))

@cache
def max_path(triangle):
  if len(triangle) == 1:
    return triangle[0][0]
  return triangle[0][0] + max(max_path(tuple(row[:-1] for row in triangle[1:])),
                              max_path(tuple(row[1:] for row in triangle[1:])))

print(max_path(triangle))
