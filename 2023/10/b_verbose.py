#!/usr/bin/env python
import math
from collections import deque
neighbors = {'|': [(0, -1), (0, 1)], "-": [(1, 0), (-1, 0)], "L": [(0, -1), (1, 0)], "J": [(0, -1), (-1, 0)], "7": [(-1, 0), (0, 1)], "F": [(0, 1), (1, 0)], ".": [], "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]}

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
  
  grid_clean = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
  for i, j in seen:
    grid_clean[i][j] = grid[i][j]
  
  are_neighbors = lambda i,j,i2,j2: any((i+di,j+dj) == (i2,j2) for dj,di in neighbors[grid_clean[i][j]])

  grid2 = []
  for i in range(len(grid_clean)):
    row = []
    row2 = []
    for j in range(len(grid_clean[0])):
      row.append(grid_clean[i][j])
      if j+1 < len(grid_clean[0]) and are_neighbors(i,j,i,j+1):
        row.append('-')
      else:
        row.append('.')
      
      if i+1 < len(grid_clean) and are_neighbors(i,j,i+1,j):
        row2 += ['|', '.']
      else:
        row2 += ['.', '.']
      
      # # Handle right/row2
      # pass
    grid2.append(row)
    grid2.append(row2)
  
  queue = deque([(0,0)])
  # for j in range(len(grid2[0])):
  #   queue.append((0, j))
  #   queue.append((len(grid)-1, j))
  # for i in range(len(grid2)):
  #   queue.append((i, 0))
  #   queue.append((i, len(grid[0])-1))

  while queue:
    i,j = queue.popleft()
    if 0 <= i < len(grid2) and 0 <= j < len(grid2[0]) and grid2[i][j] == '.':
      grid2[i][j] = 'X'
      for di,dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        queue.append((i+di,j+dj))

  print(''.join(''.join(l[::2]) for l in grid2[::2]).count('.'))
  # print('\n'.join(''.join(l) for l in grid2))
  # print('\n'.join(''.join(l[::2]) for l in grid2[::2]))


  