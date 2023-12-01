#!/usr/bin/env python
import re
# 
with open('i.txt', 'r') as f: 
  lines = [l for l in f.read().split('\n')]
  nums = [str(re.match(".*?(\d|one|two|three|four|five|six|seven|eight|nine)", l).group(1)) + str(re.match(".*(\d|one|two|three|four|five|six|seven|eight|nine).*?", l).group(1))  for l in lines]
  print(nums)
  print(sum(int(x.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")) for x in nums))
  # print(max((sum((int(x) for x in cur.split('\n'))) for cur in f.read().split('\n\n'))))
