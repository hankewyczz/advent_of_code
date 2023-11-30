with open('i.txt', 'r') as f:
  charset = []

  for l in f:
    half = len(l) // 2
    charset += list(set(l.strip()[:half]) & set(l.strip()[half:]))
  print(sum((ord(x) - (ord('a') if x.islower() else ord('A') - 26) + 1 for x in charset)))
