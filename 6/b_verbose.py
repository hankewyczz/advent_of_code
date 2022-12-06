with open('i.txt', 'r') as f: print([[i + 1 for i in range(len(s)) if i >= 13 and len(set(s[i-13:i+1])) == 14] for s in f][0][0])
# 3613