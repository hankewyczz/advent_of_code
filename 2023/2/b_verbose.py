#!/usr/bin/env python
import re
import math
from functools import reduce
counts = { "red": 12, "green": 13, "blue": 14 }
# only 12 red cubes, 13 green cubes, and 14 blue cubes

with open('i.txt', 'r') as f:
  res = 0
  for l in f.read().split('\n'):
    match = re.match("Game (\d*): (.*)", l)
    pulls = [pull.split(', ') for pull in match.group(2).split('; ')]

    cur_cnt = { "red": 0, "green": 0, "blue": 0 }
    for pull in pulls:
      for color in pull:
        cnt, color = color.split()
        cur_cnt[color] = max(cur_cnt[color], int(cnt))

    res += reduce(lambda x, y: x*y, (v for k, v in cur_cnt.items()))
  print(res)
  # print(max((sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n'))))

