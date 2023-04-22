#!/usr/bin/env python

import numpy as np
from scipy.ndimage import binary_fill_holes

cubes = [tuple(map(int, l.split(','))) for l in open("18.in")]

def sides(x, y, z):
  return ((x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1))

def n_exposed(cubes):
  return sum(1 for c in cubes for s in sides(*c) if s not in cubes)

part_one = n_exposed(cubes)
cubes = np.array(cubes)
space = np.zeros(cubes.max(axis=0) + 1)
x, y, z = cubes.T
space[x, y, z] = 1
space = binary_fill_holes(space)
cubes = set(zip(*np.where(space)))
part_two = n_exposed(cubes)

print(part_one)
print(part_two)
