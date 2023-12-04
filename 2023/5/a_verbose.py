#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  res = 0
  # Split the maps, then split the lines
  grid = [l.split('\n') for l in f.read().split('\n\n')]
  # Grab the seeds, split + convert to ints
  seeds = [int(x) for x in grid[0][0].split(': ')[1].split()]
  # Divy each map up, ignore its header, convert to ints
  maps = [[[int(x) for x in l.split()] for l in mp[1:]] for mp in grid[1:]]

  for mp in maps:
    seeds = list(map(lambda seed: ([dst+seed-src for dst, src, length in mp if src <= seed and seed <= src+length] + [seed])[0], seeds))

  print(min(seeds))

  # print([list(s) for s in seeds])

  # print(seeds, maps)
  
  # print(sum(2 ** (x-1) for x in [sum(1 for y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(2).split() if y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(1).split()) for l in grid] if x != 0))

