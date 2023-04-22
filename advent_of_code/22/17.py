#!/usr/bin/env python

moves = open("17.in").read().strip()
shapes = [
  [(i, 0) for i in range(4)],
  [(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)],
  [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
  [(0, i) for i in range(4)],
  [(0, 0), (1, 0), (0, 1), (1, 1)],
]
shapes = [[(x + 2, y) for x, y in shape] for shape in shapes]

rocks = set([(x, 0) for x in range(7)])
cache = {}
n = i = top = scrolled = 0
N = 1000000000000
part_one = part_two = 0
while n < N:
  if top >= 50:
    scrolled += 10
    rocks = set((x, y - 10) for x, y in rocks if y >= 10)
    top = max(y for _, y in rocks)
  piece = set([(x, y + top + 4) for x, y in shapes[n % len(shapes)]])
  while True:
    dir = -1 if moves[i] == "<" else 1
    piece = set((x + dir, y) for x, y in piece)
    if not(all(0 <= x <= 6 for x, _ in piece)) or piece & rocks:
       piece = set((x - dir, y) for x, y in piece)
    i = (i + 1) % len(moves)
    piece = set((x, y - 1) for x, y in piece)
    if piece & rocks:
      piece = set((x, y + 1) for x, y in piece)
      rocks |= piece
      top = max(y for _, y in rocks)
      fr = frozenset(rocks)
      if fr in cache and n >= 2022:
        old_n, old_top = cache[fr]
        delta_n, delta_top = n - old_n, top + scrolled - old_top
        repeat = (N - n) // delta_n
        n += repeat * delta_n
        scrolled += repeat * delta_top
      cache[fr] = (n, top + scrolled)
      break
  n += 1
  if n == 2022:
    part_one = max(y for _, y in rocks) + scrolled
part_two = top + scrolled

print(part_one)
print(part_two)
