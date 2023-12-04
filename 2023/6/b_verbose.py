#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  time, dist = f.read().split('\n')
  time = int(time.split(':')[1].replace(' ',''))
  dist = int(dist.split(':')[1].replace(' ',''))

  ways = 0
  for i in range(time+1):
    if i * (time-i) > dist:
      ways += 1
  print(ways)
  