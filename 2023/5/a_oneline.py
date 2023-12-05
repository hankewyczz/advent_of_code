#!/usr/bin/env python
with open('i.txt', 'r') as f: seeds, *maps = f.read().split('\n\n'); print(min(__import__('functools').reduce(lambda seed,mp: ([dst+seed-src for dst,src,length in mp if src<=seed<src+length]+[seed])[0], [[map(int, l.split()) for l in mp.split('\n')[1:]] for mp in maps], s) for s in [int(x) for x in seeds.split()[1:]]))
#340994526
