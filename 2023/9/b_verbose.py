#!/usr/bin/env python
import re
from functools import reduce

with open('i.txt', 'r') as f:
  res = 0
  for l in f.read().split('\n'):
    diffs = [list(map(int, l.split()))]
    while not all(d == 0 for d in diffs[-1]):
      diffs.append([diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)])

    # 0 2 0 3 10
    # 10-(3-(0-(2-0))))
    prev = 0
    for d in reversed(diffs):
      prev = (d[0]-prev)
    res += prev
  print(res)

  