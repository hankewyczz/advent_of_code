#!/usr/bin/env python
import re
def num_next(dp, grid, i):
  if dp[i] is not None:
    return dp[i]
  res = 1
  for j in (range(i+1, i + 1 + sum(1 for y in re.match("Card\s*\d+: (.*) \| (.*)", grid[i]).group(2).split() if y in re.match("Card\s*\d+: (.*) \| (.*)", grid[i]).group(1).split()))):
    res += num_next(dp, grid, j)
  dp[i] = res
  return res

with open('i.txt', 'r') as f:
  # Could I cache this? yeah. should I? probably.
  res = 0
  grid = f.read().split('\n')
  res = 0
  dp = [None] * len(grid)
  for i in range(len(grid)):
    res += num_next(dp, grid, i)
  print(res)


  

