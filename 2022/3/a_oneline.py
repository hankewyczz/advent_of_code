with open('i.txt', 'r') as f: print(sum(sum(ord(x) - (ord('a') - 1 if x.islower() else ord('A') - 27) for x in (set(l.strip()[:(len(l) // 2)]) & set(l.strip()[(len(l) // 2):]))) for l in f))
# 7831