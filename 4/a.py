#!/usr/bin/env python

import sys
import re
from collections import defaultdict

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

number = re.compile(r'(\d+)')

sum = 0
with open(fname) as f:
    for idx, row in enumerate(f):
        l, _, r = row.partition(':')[2].partition('|')

        winning = {int(n) for n in number.findall(r)}
        mine = {int(n) for n in number.findall(l)}

        n = len(winning.intersection(mine))
        print(n)
        if n < 1: continue
        sum += 2**(n - 1)

    print(sum)






