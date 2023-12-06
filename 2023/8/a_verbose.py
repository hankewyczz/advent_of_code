#!/usr/bin/env python
import re

with open('i.txt', 'r') as f:
  ins, nodes = f.read().split('\n\n')
  i_map = {"L": 0, "R": 1}
  nodes = {n[:3]: (n[7:10], n[12:-1]) for n in nodes.split('\n')}
  cur = "AAA"
  steps = 0
  while cur != "ZZZ":
    cur = nodes[cur][i_map[ins[steps % len(ins)]]]
    steps += 1
    
  print(steps)

  