with open('i.txt', 'r') as f:
  charset = []
  lines = f.readlines()
  line_chunks = [[set(l.strip()) for l in lines[i:i+3]] for i in range(0, len(lines), 3)]
  line_badge = []
  for chunk in line_chunks:
    s = chunk[0]
    for line in chunk:
      s &= line    
    line_badge.append(s)
  line_badges = [list(s)[0] for s in line_badge]
  print(line_badges)
  
  print(sum((ord(x) - (ord('a') if x.islower() else ord('A') - 26) + 1 for x in line_badges)))
# 2683