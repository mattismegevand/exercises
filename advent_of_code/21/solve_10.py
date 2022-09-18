#!/usr/bin/env python3

OPENING = "([{<"
CLOSING = ")]}>"

POINTS_ONE = [3, 57, 1197, 25137]
POINTS_TWO = [1, 2, 3, 4]

if __name__ == "__main__":
  lines = [line.strip() for line in open("input_10")]
  part_one = 0
  part_two = []
  for line in lines:
    stack = []
    corrupted = False

    for c in line:
      if c in OPENING:
        stack.append(c)
      else:
        i = CLOSING.index(c)
        if stack.pop() != OPENING[i]:
          corrupted = True
          part_one += POINTS_ONE[i]

    if not corrupted:
      missing = [CLOSING[OPENING.index(c)] for c in stack[::-1]]
      score = 0
      for c in missing:
        score = score * 5 + POINTS_TWO[CLOSING.index(c)]
      part_two.append(score)

  print(part_one)
  print(sorted(part_two)[len(part_two) // 2])
