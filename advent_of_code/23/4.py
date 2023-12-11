#!/usr/bin/env python

lines = open("4.in").read().strip().splitlines()
p1 = 0
p2 = {i+1: 1 for i in range(len(lines))}
for i, l in enumerate(lines):
    _, game = l.split(": ")
    winning_cards, our_cards = game.split(" | ")
    winning_cards = [int(i) for i in winning_cards.split()]
    our_cards = [int(i) for i in our_cards.split()]
    matches = len(set(winning_cards) & set(our_cards))
    if matches > 0:
        p1 += 2**(matches - 1)
        for j in range(matches):
            p2[i+1 + j+1] += p2[i+1] 
print(p1)
print(sum(p2.values()))