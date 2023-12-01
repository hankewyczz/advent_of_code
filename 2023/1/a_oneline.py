#!/usr/bin/env python
with open('i.txt', 'r') as f: print(sum(int(x) for x in [str(__import__('re').match(".*?(\d)", l).group(1)) + str(__import__('re').match(".*(\d).*?", l).group(1))  for l in f.read().split('\n')]))

# 54597