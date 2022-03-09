#!/usr/bin/env python3

import sys


s = sys.stdin.readlines()
for line in s:
   print(line.casefold().split(" ")[0] in line.casefold().split(" ")[1])
