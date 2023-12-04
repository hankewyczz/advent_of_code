#!/usr/bin/env python
with open('i.txt', 'r') as f: print(__import__('math').prod((sum(1 for i in range(time+1) if i * (time-i) > dist) for time, dist in zip(*(map(int, l.split(':')[1].split()) for l in f.read().split('\n')))))) #633080
  