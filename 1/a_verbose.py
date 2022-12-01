with open('i.txt', 'r') as f:
  cur = 0
  maxCal = 0

  for line in f:  
    if line != '\n':
      cur += int(line)
    else:
      maxCal = max(maxCal, cur)
      cur = 0
  print(maxCal)