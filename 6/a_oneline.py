with open('i.txt', 'r') as f: print([[i + 1 for i in range(len(s)) if i >= 3 and len(set(s[i-3:i+1])) == 4] for s in f][0][0])
# 1640