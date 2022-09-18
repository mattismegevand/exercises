#!/usr/bin/env python3

import numpy as np
from PIL import Image

SIZE = (895, 1311)

if __name__ == "__main__":
  board = np.zeros(SIZE)
  dots, folds = open("input_13").read().strip().split("\n\n")
  dots = [list(map(int, l.split(","))) for l in dots.split("\n")]
  folds = [l.split("=") for l in folds.split("\n")]
  folds = list(map(lambda t: (t[0][-1], int(t[1])), folds))

  for d in dots:
    board[d[1], d[0]] = 1

  part_one = None
  for f in folds:
    a, b = f
    if a == "x":
      b1, b2 = board[:, :b], board[:, b+1:]
    else:
      b1, b2 = board[:b, :], board[b+1:, :]

    b2 = np.flip(b2, a == "x")
    board = b1 + b2
    if part_one is None:
      part_one = np.sum(board >= 1)

print(part_one)
img = Image.fromarray(board * 255)
img.show()
