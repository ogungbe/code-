#!/usr/bin/env python3

import sys

n = sys.stdin.read()
s = n.split()
line1 = s[0]
line2 = s[1:]
count = int(line1)
total = 0

for line in line2:
   if count > 0:
      new2 = int(line)
      count = count - new2
      if count >= 0:
         total = total + 1
print(total)
