#/usr/bin/env python3

import sys
s = sys.stdin.readlines()
p = []
a = []
b = []
upalpha = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
for line in s:
   line = line.strip('\n')
   for lett in line:
      pass
      if lett in upalpha.lower():
         line = line.replace(lett, '0')
         r = line.split('0')
   p.append(r)
   print(max(r, key=len))
