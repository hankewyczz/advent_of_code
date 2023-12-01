#!/usr/bin/env python
import re

with open('i.txt', 'r') as f: 
  nums = [str(re.match(".*?(\d)", l).group(1)) + str(re.match(".*(\d).*?", l).group(1))  for l in f.read().split('\n')]
  print(sum(int(x) for x in nums))
  # print(max((sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n'))))

