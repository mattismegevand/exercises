#!/usr/bin/env python

import itertools
from collections import defaultdict

valves = set()
flows = {}
dists = defaultdict(lambda: float('inf'))
for line in open("16.in"):
  words = line.split()
  valve = words[1]
  rate = int(words[4][5:-1])
  valves.add(valve)
  if rate > 0: flows[valve] = rate
  for adj in "".join(words[9:]).split(","):
    dists[(valve, adj)] = 1
bits = {v: 1 << i for i, v in enumerate(flows)}

for k, i, j in itertools.product(valves, valves, valves):
  dists[(i, j)] = min(dists[(i, j)], dists[(i, k)] + dists[(k, j)])

def visit(u, time, state, flow, answer):
  answer[state] = max(answer.get(state, 0), flow)
  for v in flows:
    time_left = time - dists[(u, v)] - 1
    if bits[v] & state or time_left <= 0: continue
    visit(v, time_left, state | bits[v], flow + time_left * flows[v], answer)
  return answer

part_one = max(visit('AA', 30, 0, 0, {}).values())
visited_two = visit('AA', 26, 0, 0, {})
part_two = max(v1 + v2 for k1, v1 in visited_two.items() for k2, v2 in visited_two.items() if not k1 & k2)

print(part_one)
print(part_two)
