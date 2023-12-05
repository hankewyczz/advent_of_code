#!/usr/bin/env python
with open('i.txt', 'r') as f: print(sum([hand[-1] * (i+1) for i, hand in enumerate(sorted((sum(map(l.split()[0].count, l.split()[0])), *["23456789TJQKA".index(c) for c in l.split()[0]], int(l.split()[1])) for l in f.read().split('\n')))])) # 253910319

  