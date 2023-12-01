#!/usr/bin/env python
with open('i.txt', 'r') as f: print(sum(int(l.split(': ')[0].split()[1]) for l in f.read().split('\n') if all([{"r":12,"g":13,"b":14}[pull[1][0]] >= int(pull[0]) for pull in [x.split() for x in l.split(": ")[1].replace(';',',').split(', ')]])))
#1931