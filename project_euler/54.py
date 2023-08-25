#!/usr/bin/env python

from collections import Counter

hands_list = [l.strip().split() for l in open('data/0054_poker.txt')]

def value(card):
  card_value = card[0]
  if card_value in '23456789':
    return int(card_value)
  value_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  return value_map[card_value]

def hand_rank(hand):
  values = [value(card) for card in hand]
  value_counts = Counter(values)
  unique_values_sorted = sorted(value_counts, key=lambda x: (-value_counts[x], -x))

  flush = len(set([card[1] for card in hand])) == 1
  straight = (max(values) - min(values) == 4 and len(unique_values_sorted) == 5) or (set(values) == {14, 2, 3, 4, 5})

  if straight and flush:
    return (9, max(values))
  if 4 in value_counts.values():
    return (8, unique_values_sorted[0])
  if 3 in value_counts.values() and 2 in value_counts.values():
    return (7, unique_values_sorted[0], unique_values_sorted[1])
  if flush:
    return (6, ) + tuple(unique_values_sorted)
  if straight:
    return (5, max(values))
  if value_counts.most_common(1)[0][1] == 3:
    return (4, unique_values_sorted[0]) + tuple(unique_values_sorted[1:])
  if len(unique_values_sorted) == 3:
    return (3, unique_values_sorted[0], unique_values_sorted[1], unique_values_sorted[2])
  if len(unique_values_sorted) == 4:
    return (2, unique_values_sorted[0]) + tuple(unique_values_sorted[1:])
  return (1, ) + tuple(unique_values_sorted)

print(sum(1 for hand in hands_list if hand_rank(hand[:5]) > hand_rank(hand[5:])))
