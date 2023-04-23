#!/usr/bin/env python

convert = {
  'A': 'R',
  'B': 'P',
  'C': 'S',
  'X': 'R',
  'Y': 'P',
  'Z': 'S',
}
shape_score = {'R': 1, 'P': 2, 'S': 3}

winning_move = {'R': 'P', 'P': 'S', 'S': 'R'}
losing_move  = {v: k for k, v in winning_move.items()}

def part_one(t):
  op, us = t
  if op == us:
    return 3 + shape_score[us]
  if losing_move[op] == us:
    return shape_score[us]
  return 6 + shape_score[us]

def part_two(t):
  op, goal = t
  if goal == 'R':
    return shape_score[losing_move[op]]
  if goal == 'P':
    return 3 + shape_score[op]
  return 6 + shape_score[winning_move[op]]

rounds = [tuple(convert[p] for p in l.split()) for l in open("2.in")]

print(sum(part_one(r) for r in rounds))
print(sum(part_two(r) for r in rounds))
