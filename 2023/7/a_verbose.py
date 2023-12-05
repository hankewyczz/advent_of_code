#!/usr/bin/env python
import re
from collections import Counter
with open('i.txt', 'r') as f:
  res = 0
  hands = []
  for l in f.read().split('\n'):
    hand, bid = l.split()
    print(list(map(hand.count, hand)))
    x = Counter(hand).most_common(2)
    x = f"{x[0][1]}{x[1][1]}" if len(x) > 1 else "50"
    hands.append(({"50": 7, "41": 6, "32": 5, "31": 4, "22": 3, "21": 2, "11": 1}[x], *["23456789TJQKA".index(c) for c in hand], int(bid)))
  hands.sort()
  # print(hands)
  print(sum([hand[-1] * (i+1) for i, hand in enumerate(hands)])) # 253910319

  