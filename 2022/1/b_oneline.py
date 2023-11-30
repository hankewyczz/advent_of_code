with open('i.txt', 'r') as f: print(sum(sorted([sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n')], reverse=True)[:3]))
