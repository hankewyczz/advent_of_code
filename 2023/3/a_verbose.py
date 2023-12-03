#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  res = 0
  grid = f.read().split('\n')
  for i, l in enumerate(grid):
    for num in re.finditer(r'\d+', l):
      if any(0 < m and m < len(grid) and 0 < n and n < len(l) and re.match("[^\d\.]", grid[m][n]) for m in range(i-1, i+2) for n in range(num.start()-1, num.end()+1)):
        res += int(num.group())
# 527446
  print(res)
