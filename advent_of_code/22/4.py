#!/usr/bin/env python

lines = [l.split(',') for l in open("4.in").read().splitlines()]

part_one = 0
part_two = 0

for l in lines:
  p1, p2 = l
  s1, e1 = (int(n) for n in p1.split('-'))
  s2, e2 = (int(n) for n in p2.split('-'))

  if (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2):
    part_one += 1
  if (s2 <= e1) and (s1 <= e2):
    part_two += 1

print(part_one)
print(part_two)
