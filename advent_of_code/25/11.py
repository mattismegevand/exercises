from functools import cache

inp = open('11.in').read().splitlines()
d = {}
for i in inp:
    k, v = i.split(': ')
    d[k] = v.split()

def dfs1(n):
    if n == 'out':
        return 1
    if (neighbours := d.get(n)) is None:
        return 0
    return sum(dfs1(neighbour) for neighbour in neighbours)

@cache
def dfs2(n, dac = False, fft = False):
    if n == 'out':
        return 1 if dac and fft else 0
    elif n == 'dac':
        dac = True
    elif n == 'fft':
        fft = True
    if (neighbours := d.get(n)) is None:
        return 0
    return sum(dfs2(neighbour, dac, fft) for neighbour in neighbours)

print(dfs1('you'))
print(dfs2('svr'))
