#!/usr/bin/env python3

import sys
data = sys.stdin.readlines()
defs = {}
for line in data:
   line = line.split()
   #print(line)
   if line[0] == 'def':
      #print('yes')
      defs[line[1]] = int(line[2])
   if line[0] == 'calc':
      if '+' in line or '-' in line:
         try:
            add = line.index('+')
            result = defs[line[add - 1]] + defs[line[add + 1]]
            #print(result)
            for k, v in defs.items():
               pass
               #print(v, k)
               if v == result:
                  pass
                  #print(f'{ " ".join(line[1:- 1])} = {k}')
            #print(defs[f[1]], f[2], defs[f[3]])
            #print(f[2])
         except KeyError:
            pass
            #print(f'{line[add - 1]} + {line[add + 1]} = unknown')
         if '+' in line and '-' in line:
            try:
               add = line.index('+')
               sub = line.index('-')
               result = defs[line[add - 1]] + defs[line[add + 1]]
               - defs[line[sub + 1]]
               #print(result)
               for j in range(1, len(line), 2):
                  line[j] = defs[line[j]]
               newl = line[1:-1]
               print(newl)
               i = 0
               total = 0
               while i < len(newl):
                  #total = 0
                  if newl[i] == '-':
                     total = newl[i - 1] - newl[i + 1]
                     #print(total)
                     elif newl[i] == '+':
                       total = total + newl[i + 1]
                     print(total)
                  i = i + 1
               if v != result:
                  pass
                  #print(f'{" ".join(line[1:])} unknown')
            except KeyError:
               print('err')
               

print(defs)
