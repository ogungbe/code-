#!/usr/bin/env python3

import sys

s = sys.stdin.read().split()
#for line in s:
   #print(line)
bword = [line for line in s]
#print(bword)
with open(sys.argv[1], 'r') as f:
   txt = [line.strip() for line in f.readlines()]
   #print(txt)

for word in bword:
   for text in txt:
      if word in text:
         text = text.replace(word, len(word) * '@')
         print(text)
