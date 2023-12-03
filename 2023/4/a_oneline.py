#!/usr/bin/env python
with open('i.txt', 'r') as f: print(sum(2 ** (x-1) for x in [sum(1 for y in __import__('re').match("Card\s*\d+: (.*) \| (.*)", l).group(2).split() if y in __import__('re').match("Card\s*\d+: (.*) \| (.*)", l).group(1).split()) for l in f.read().split('\n')] if x != 0))
  # 25174