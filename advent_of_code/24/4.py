#!/usr/bin/env python3

data = open("4.in", "r").read().splitlines()
M, N = len(data), len(data[0])

part1 = 0
part2 = 0
for i in range(M):
    for j in range(N):
        if 1 <= i < M - 1 and 1 <= j < N - 1 and data[i][j] == 'A':
            d1 = data[i-1][j-1] + 'A' + data[i+1][j+1]
            d2 = data[i+1][j-1] + 'A' + data[i-1][j+1]
            if set(d1) == set(d2) == set('MAS'):
                part2 += 1
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di, dj) == (0, 0): continue
                word = ""
                for k in range(4):
                    pi = i + di * k
                    pj = j + dj * k
                    if not (0 <= pi < M) or not(0 <= pj < N): break
                    word += data[pi][pj]
                if word == "XMAS": 
                    part1 += 1
print(part1)
print(part2)
