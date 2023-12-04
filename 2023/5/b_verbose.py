#!/usr/bin/env python
import re
with open('i.txt', 'r') as f:
  res = 0
  # Split the maps, then split the lines
  grid = [l.split('\n') for l in f.read().split('\n\n')]
  # Grab the seeds, split + convert to ints
  seeds = [int(x) for x in grid[0][0].split(': ')[1].split()]
  seeds = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

  # Divy each map up, ignore its header, convert to ints
  maps = [[[int(x) for x in l.split()] for l in mp[1:]] for mp in grid[1:]]


  locations = []
  for pair in seeds:
    remainder = [pair]
    res = []

    for mp in maps:
      while remainder:
        p_start, p_end = remainder.pop()
        for dst, src, length in mp:
          if p_end < src or src + length <= p_start:
            continue # no overlap
          elif src <= p_start <= p_end < src + length:
            # full overlap
            offset = (p_start - src)
            res.append((dst + offset, dst + offset + p_end - p_start))
            break
          elif src <= p_start < (src + length) <= p_end:
            # Partial overlap - the pair straddles the end of the map
            offset = p_start - src
            res.append((dst + offset, dst + length - 1))
            remainder.append((src + length, p_end)) # add the remainder and keep going
            break
          elif p_start < src <= p_end < src + length:
            # straddles the start of the map
            offset = p_end - src
            res.append((dst, dst + offset))
            remainder.append((p_start, src - 1))
            break
          elif p_start < src <= src + length <= p_end:
            # mapping is contained in the pair
            res.append((dst, dst + length - 1))
            remainder.append((p_start, src-1))
            remainder.append((src+length, p_end))
            break
        else:
          # no matches with anything
          res.append((p_start, p_end))
      remainder = res
      res = []
      # print(pair, remainder)
    locations += remainder
  # print(locations)
    
  print(min(i[0] for i in locations))

  # print(min(seeds))

  # print([list(s) for s in seeds])

  # print(seeds, maps)
  
  # print(sum(2 ** (x-1) for x in [sum(1 for y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(2).split() if y in re.match("Card\s*\d+: (.*) \| (.*)", l).group(1).split()) for l in grid] if x != 0))

