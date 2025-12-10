from functools import cache

inp = [tuple(map(int, l)) for l in open('3.in').read().splitlines()]

@cache
def f(l, s, k):
    if len(l) - s < k:
        return float('-inf')
    if k == 1:
        return max(l[s:])
    m = -1
    for i in range(s, len(l) - k + 1):
        m = max(m, (l[i] * (10**(k - 1))) + f(l, i + 1, k - 1))
    return m

part1 = sum(f(l, 0, 2) for l in inp)
part2 = sum(f(l, 0, 12) for l in inp)
print(part1)
print(part2)

