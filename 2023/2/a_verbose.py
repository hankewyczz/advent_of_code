#!/usr/bin/env python
import re
counts = { "red": 12, "green": 13, "blue": 14 }
# only 12 red cubes, 13 green cubes, and 14 blue cubes

with open('i.txt', 'r') as f:
  res = 0
  for l in f.read().split('\n'):
    match = re.match("Game (\d*): (.*)", l)
    pulls = [pull.split(', ') for pull in match.group(2).split('; ')]

    valid = True
    for pull in pulls:
      if not valid:
        break
      for color in pull:
        if not valid:
          break
        cnt, color = color.split()
        valid = counts[color] >= int(cnt)

    if valid:
      res += int(match.group(1))
  print(res) #1931
  # print(max((sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n'))))

