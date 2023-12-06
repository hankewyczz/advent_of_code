#!/usr/bin/env python
import math
from collections import deque
neighbors = {'|': [(0, -1), (0, 1)], "-": [(1, 0), (-1, 0)], "L": [(0, -1), (1, 0)], "J": [(0, -1), (-1, 0)], "7": [(-1, 0), (0, 1)], "F": [(0, 1), (1, 0)], ".": []}

with open('i.txt', 'r') as f:
  grid = [[c for c in l] for l in f.read().split('\n')]

  inrange = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
  tomark = deque([])

  seen = set()
  maxval = 0

  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "S":
        seen.add((i, j))

        for di,dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          if (-dj,-di) in neighbors[grid[i+di][j+dj]]:
            tomark.append((i+di, j+dj, 1))
        break

  

  while tomark:
    i, j, n = tomark.popleft()
    if inrange(i,j) and (i,j) not in seen and grid[i][j] in neighbors:
      seen.add((i, j))
      maxval = max(maxval, n)
      for dj, di in neighbors[grid[i][j]]:
        tomark.append((i+di, j+dj, n+1))

  print(maxval)


  