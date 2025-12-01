inp = [int(x[1:]) * (-1 if x[0] == 'L' else 1) for x in open('1.in').read().splitlines()]
acc = 50
part1 = part2 = 0
for x in inp:
  for _ in range(abs(x)):
    acc += -1 if x < 0 else 1
    acc %= 100
    if acc == 0:
      part2 += 1
  if acc == 0:
    part1 += 1
print(part1)
print(part2)
