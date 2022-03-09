#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
a = []
for line in s:
   line = line.strip('\n')
   line = line.lower()
   a.append(line)

for line in a:
   alpha = 'abcdefghijklmnopqrstuvwxyz'
   for lett in line:
      if lett in alpha:
         alpha = alpha.replace(lett, '')
         if len(alpha) == 0:
            pass
            print('pangram')
   if len(alpha) != 0:
      print(f'missing {alpha}')
