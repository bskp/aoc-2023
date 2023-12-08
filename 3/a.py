#!/usr/bin/env python

import sys
import re
from collections import defaultdict

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

symbol = re.compile(r'[^\d\s\.]')
number = re.compile(r'(\d+)')

sum = 0
map = defaultdict(list)

def lookup_cogs(y: int, x_min, x_max):
    for cog in map[y + 1]:
        if x_min <= cog and x_max >= cog: return True
    for cog in map[y]:
        if x_min <= cog and x_max >= cog: return True
    for cog in map[y - 1]:
        if x_min <= cog and x_max >= cog: return True
    return False

with open(fname) as f:
    for idx, row in enumerate(f):
        map[idx] = [m.start() for m in symbol.finditer(row)]

    f.seek(0)
    for idx, row in enumerate(f):
        for m in number.finditer(row):
            if lookup_cogs(idx, m.start() - 1, m.end()):
                sum += int(m.group())

    print(sum)



