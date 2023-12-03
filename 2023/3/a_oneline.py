#!/usr/bin/env python
with open('i.txt', 'r') as f: grid = f.read().split('\n'); print(sum([int(num.group()) for i, l in enumerate(grid) for num in __import__('re').finditer(r'\d+', l) if any(0<m and m<len(grid) and 0<n and n<len(l) and __import__('re').match("[^\d\.]", grid[m][n]) for m in range(i-1, i+2) for n in range(num.start()-1, num.end()+1))]))

# 527446