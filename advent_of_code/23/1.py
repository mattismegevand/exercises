#!/usr/bin/env python

spelled_digits = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("1.in") as f:
    p1, p2 = 0, 0
    for l in f:
        d1, d2 = [], []
        for i, c in enumerate(l):
            if c.isdigit():
                d1.append(c)
                d2.append(c)
            else:
                for k, v in spelled_digits.items():
                    if l[i:].startswith(k):
                        d2.append(v)
                        break
        p1 += int(d1[0] + d1[-1])
        p2 += int(d2[0] + d2[-1])
    print(p1)
    print(p2)