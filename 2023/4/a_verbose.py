#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  res = 0
  grid = f.read().split('\n')
  
  print(sum(2 ** (x-1) for x in [sum(1 for y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(2).split() if y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(1).split()) for l in grid] if x != 0))

