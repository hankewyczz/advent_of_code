#!/usr/bin/env python
import re
from collections import defaultdict
c = defaultdict(list)

with open('i.txt', 'r') as f:
  res = 0
  grid = f.read().split('\n')
  for i, l in enumerate(grid):
    for num in re.finditer(r'\d+', l):
      for m in range(i-1, i+2):
        for n in range(num.start()-1, num.end()+1):
          if 0 < m and m < len(grid) and 0 < n and n < len(l) and re.match("\*", grid[m][n]):
            c[(m,n)].append(int(num.group()))
            
# 527446
  print(sum(nums[0] * nums[1] for nums in c.values() if len(nums) == 2))
