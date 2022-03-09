#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()

def tagger(item):
   return float(item[1])


ting = {}
r = []
w = []
b = []
for line in s:
   line = line.strip('\n')
   i = 0
   while i < len(line):
      e = []
      if line[i] == ':':
         pos = line.find(line[i])
         r.append(pos)
         scores = line[pos + 1:]
         name = line[:pos + 1]
         scores = scores.split()
         scores = ''.join(scores)
         p = scores.split(',')
         for o in p:
            o = int(o)
            e.append(o)
         w.append(f'{line[:pos + 1]} {sum(e) / len(e):.2f}')
         avg = f'{sum(e) / len(e):.2f}'
         avg2 = f'{sum(e) / len(e):.2f}'
         b.append(avg2)
         ting[name] = avg
      i = i + 1
b.sort(key=float, reverse=True)

for k, v in sorted(ting.items(), key=tagger, reverse=True):
   print(f'{k} {v}')
