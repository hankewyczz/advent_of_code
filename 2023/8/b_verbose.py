#!/usr/bin/env python
import re
import math
with open('i.txt', 'r') as f:
  ins, nodes = f.read().split('\n\n')
  ins = [1 if c == 'R' else 0 for c in ins]
  n_ins = len(ins)

  nodes = {n[:3]: (n[7:10], n[12:-1]) for n in nodes.split('\n')}
  cur = [n for n in nodes.keys() if n[2] == 'A']
  steps = [0] * len(cur)

  for i, node in enumerate(cur):
    while node[2] != 'Z':
      node = nodes[node][ins[steps[i] % n_ins]]
      steps[i] += 1
  
  print(math.lcm(*steps))

  