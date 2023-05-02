#!/usr/bin/env python

from copy import deepcopy

data = open("11.in").read()

lcd = 1
d = {}
for m in data.split("\n\n"):
  i, items, f, test, true, false = m.splitlines()
  i = int(i.split()[-1][:-1])
  items = [int(n) for n in items.split(":")[1].split(", ")]
  f = "".join(f.split()[-3:])
  test = int(test.split()[-1])
  lcd *= test
  true = int(true.split()[-1])
  false = int(false.split()[-1])
  d[i] = {"items": items, "f": lambda old, f=f: eval(f), "test": test, "t_dest": true, "f_dest": false}

start = deepcopy(d)
for p, n in enumerate([20, 10000]):
  d = deepcopy(start)
  counts = [0 for _ in range(len(d))]
  for _ in range(n):
    for i, m in d.items():
      for item in m["items"]:
        item = m["f"](item)
        item = item // 3 if p == 0 else item % lcd
        key = m["t_dest"] if item % m["test"] == 0 else m["f_dest"]
        d[key]["items"].append(item)
      counts[i] += len(m["items"])
      d[i]["items"] = []
  top2, top1 = sorted(counts)[-2:]
  print(top1 * top2)
