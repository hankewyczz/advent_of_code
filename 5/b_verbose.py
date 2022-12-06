import re
with open('i.txt', 'r') as f:
  arrs = None
  for line in f:
    matches_init = re.findall("(\s{3}|\[.\])\s", line)
    if arrs is None:
      arrs = [[] for i in range(len(matches_init))]
    
    for i in range(len(matches_init)):
      if matches_init[i].strip() != '':
        arrs[i] = [matches_init[i][1]] + arrs[i]

    matches_move = re.findall("move (\d*) from (\d*) to (\d*)", line)
    
    print(matches_move)
    if len(matches_move) > 0:
      num = int(matches_move[0][0])
      arr_idx = int(matches_move[0][1]) - 1
      to_move = arrs[arr_idx][-num:]
      arrs[arr_idx] = arrs[arr_idx][:-num]
      print(to_move)
      print(arrs)
      arrs[int(matches_move[0][2]) - 1] += to_move

  print(''.join([arr[-1] for arr in arrs]))
#RGLVRCQSB