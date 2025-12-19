import heapq
from tqdm import trange
from math import prod
from collections import Counter

inp = [tuple(map(int, l.split(','))) for l in open('8.in').read().splitlines()]
parent = list(range(len(inp)))
size = [1] * len(inp)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

def dist(i, j):
    x1, y1, z1 = inp[i]
    x2, y2, z2 = inp[j]
    return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

def f():
    it = 1
    while True:
        heap = []
        for i in range(len(inp)):
            for j in range(i+1, len(inp)):
                if find(i) == find(j):
                    continue
                d = dist(i, j)
                if len(heap) < 1000:
                    heapq.heappush(heap, (-d, i, j))
                else:
                    if d < -heap[0][0]:
                        heapq.heapreplace(heap, (-d, i, j))
        edges = [(-d, i, j) for (d, i, j) in heap]
        edges.sort()
        for _, i, j in edges:
            union(i, j)
            if len(set(parent)) == 1:
                print(inp[i][0] * inp[j][0])
                return
        if it == 1:
            counts = Counter(find(i) for i in range(len(inp)))
            print(prod(b for _, b in counts.most_common(3)))
        it += 1
f()
