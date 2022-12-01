with open('i.txt', 'r') as f: print(max((sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n'))))
