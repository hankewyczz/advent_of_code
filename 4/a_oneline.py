with open('i.txt', 'r') as f: print(sum([1 if x else 0 for x in [(e[0][0] >= e[1][0] and e[0][1] <= e[1][1]) or (e[0][0] <= e[1][0] and e[0][1] >= e[1][1]) for e in [[[int(y) for y in x.split('-')] for x in p.strip().split(',')] for p in f]]]))