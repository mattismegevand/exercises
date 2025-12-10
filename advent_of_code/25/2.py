inp = [tuple(map(int, x.split('-'))) for x in open('2.in').read().strip().split(',')]
part1 = part2 = 0
for a, b in inp:
    for n in range(a, b + 1):
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            m = l // 2
            if s[:m] == s[m:]:
                part1 += n
        for i in range(1, l // 2 + 1):
            if l % i == 0:
                ss = s[:i] * (l // i)
                if ss == s:
                    part2 += n
                    break
print(part1)
print(part2)
