#!/usr/bin/env python3

import sys
a = []
with open(sys.argv[1], 'r') as f:
   for line in f:
      first = line
      first = first.strip('\n')
      a.append(first)
with open(sys.argv[2], 'r') as g:
   for line in g:
      second = line
      if second not in a:
         p = second.strip('\n')
         a.append(p)
splitted = len(a) // 2
first = a[:splitted]
second = a[splitted:]
i = 0
while i < len(first) or i < len(second):
   if i < len(first):
      print(first[i])
   if i < len(second):
      print(second[i])
   i = i + 1
