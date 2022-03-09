#!/usr/bin/env python3

import sys

#n = sys.stdin.read()
#isdigit
#a = '3e3'
#isalnum()
#islower()
#isupper()
str = sys.stdin.read().split()
for line in str:
   s = [0, 0, 0, 0]
   for c in line:
      if c.islower():
         s[0] = 1
      elif c.isupper():
         s[1] = 1
      elif c.isdigit():
         s[2] = 1
      else:
         s[3] = 1
   print(sum(s))
