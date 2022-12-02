win = {
  'A': 'C', 
  'B': 'A',
  'C': 'B'
}

lose = {
  'A': 'B',
  'B': 'C',
  'C': 'A'
}

scores = {
  'A': 1,
  'B': 2,
  'C': 3
}

with open('i.txt', 'r') as f:
  score = 0

  for line in f:
    a, b = line.split()
    if b == 'X':
      score += 0
      score += scores[win[a]]
    elif b == 'Y':
      score += 3
      score += scores[a]
    else:
      score += 6
      score += scores[lose[a]]
  print(score)