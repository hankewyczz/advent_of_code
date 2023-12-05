#!/usr/bin/env python
import re
from collections import Counter
with open('i.txt', 'r') as f:
  res = 0
  hands = []
  for l in f.read().split('\n'):
    hand, bid = l.split()
    fst, snd = (Counter(hand).most_common(2) + [("", 0)])[:2]

    hand2 = hand
    if fst[1] == 1:
      hand2 = hand.replace("J", sorted([("J23456789TQKA".index(c), c) for c in hand], reverse=True)[0][1])
    elif fst[1] == 2 and snd[1] == 2:
      hand2 = hand.replace("J", sorted([("J23456789TQKA".index(c), c) for c in [fst[0], snd[0]]], reverse=True)[0][1])
    elif fst[0] == "J":
      if snd[0] == "":
        hand2 = hand.replace("J", "A")
      else:
        hand2 = hand.replace("J", snd[0])
    else:
      hand2 = hand.replace("J", fst[0])
    
    fst, snd = (Counter(hand2).most_common(2) + [("", 0)])[:2]
    # 2J992
    x = f"{fst[1]}{snd[1]}" 
    print(hand2, x)
    hands.append(({"50": 7, "41": 6, "32": 5, "31": 4, "22": 3, "21": 2, "11": 1}[x], *["J23456789TQKA".index(c) for c in hand], int(bid)))
  hands.sort()
  # print(hands)
  print(sum([hand[-1] * (i+1) for i, hand in enumerate(hands)]))

  