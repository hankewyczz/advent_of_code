#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  time, dist = f.read().split('\n')
  time = map(int, time.split(':')[1].split())
  dist = map(int, dist.split(':')[1].split())
  races = zip(time, dist)
  ways = 1
  for time, dist in races:
    cur = 0
    for i in range(time+1):
      if i * (time-i) > dist:
        cur += 1
    ways *= cur
      
  print(ways)
  