#!/usr/bin/env python3

from collections import defaultdict
from copy import copy

part_one = 0
part_two = 0

def get_path(graph, seen, current, joker_used=False, path=None, is_part_one=True):
  global part_one, part_two

  if path is None:
    path = []
  path.append(current)

  if current == "end":
    if is_part_one:
      part_one += 1
    else:
      part_two += 1
    return

  if current in seen:
    seen[current] = True

  for n in graph[current]:
    if n == "start":
      continue

    if n in seen:
      if not seen[n]:
        get_path(graph, copy(seen), n, joker_used, path=path, is_part_one=is_part_one)
      elif not is_part_one and not joker_used:
        get_path(graph, copy(seen), n, True, path=path, is_part_one=is_part_one)
    else:
      get_path(graph, copy(seen), n, joker_used, path=path, is_part_one=is_part_one)

if __name__ == "__main__":
  edges = [l.strip().split("-") for l in open("input_12")]
  graph = defaultdict(list)
  for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
  seen = {k: False for k in graph.keys() if not k.isupper()}
  get_path(graph, seen, "start")
  get_path(graph, seen, "start", is_part_one=False)

  print(part_one)
  print(part_two)
