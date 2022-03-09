#!/usr/bin/env python3

import sys

table = sys.stdin.readlines()
def getclublen(table):
   maxclublen = 0
   for line in table:

      line = line.split()
      cn = ' '.join(line[1:-8])
      if len(cn) > maxclublen:
         maxclublen = len(cn)
   return maxclublen


maxclublen = getclublen(table)

print(f'{"POS":>3s}', f'{"CLUB":{maxclublen}s}', f'{"P":>2s}',
      f'{"W":>3s}', f'{"D":>3s}', f'{"L":>3s}', f'{"GF":>3s}',
      f'{"GA":>3s}', f'{"GD":>3s}', f'{"PTS":>3s}')
for line in table:
   line = line.split()
   cn = ' '.join(line[1:-8])
   print(f'{line[0]:>3s}', f'{cn:{maxclublen}s}', f'{line[-8]:>2s}',
         f'{line[-7]:>3s}', f'{line[-6]:>3s}', f'{line[-5]:>3s}',
         f'{line[-4]:>3s}', f'{line[-3]:>3s}', f'{line[-2]:>3s}',
         f'{line[-1]:>3s}')
