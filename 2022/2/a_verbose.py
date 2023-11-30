win = {
  'X': 'C', 
  'Y': 'A',
  'Z': 'B'
}

draw = {
  'X': 'A',
  'Y': 'B',
  'Z': 'C'
}
with open('i.txt', 'r') as f:
  score = 0

  for line in f:
    a, b = line.split()
    score += 1 if b == 'X' else 2 if b == 'Y' else 3
    score += 6 if win[b] == a else 3 if draw[b] == a else 0
  print(score)