import re
with open('i.txt', 'r') as f:
  arrs = []
  for line in f:
    for i, m in enumerate(re.findall("(\s{3}|\[.\])\s", line)):
      if i >= len(arrs):
          arrs.append([])
      if m.strip() != '':
        arrs[i] = [m[1]] + arrs[i]
    
    for m in re.findall("move (\d*) from (\d*) to (\d*)", line):
      for i in range(int(m[0])):
        to_move = arrs[int(m[1]) - 1].pop()
        arrs[int(m[2]) - 1].append(to_move)

  print(''.join([arr[-1] for arr in arrs]))
# SBPQRSCDF