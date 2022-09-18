#!/usr/bin/env python3

if __name__ == "__main__":
  insts = [(t[0], int(t[1])) for l in open("input_02").read().splitlines() if (t := l.split())]

  d, h = 0, 0
  for inst, n in insts:
    match inst:
      case "forward": h += n
      case "up": d -= n
      case "down": d += n
  print(d * h)

  d, h = 0, 0
  a = 0
  for inst, n in insts:
    match inst:
      case "forward": h += n; d += a * n
      case "up": a -= n
      case "down": a += n
  print(d * h)
