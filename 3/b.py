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

cog_usage = defaultdict(lambda: defaultdict(lambda: 0))

def lookup_cogs(y: int, x_min: int, x_max: int, gear_value: int):
    for o in [1, 0, -1]:
        y_ = y + o
        for cog in map[y_]:
            if x_min <= cog and x_max >= cog:
                prev = cog_usage[y_][cog]
                cog_usage[y_][cog] = gear_value
                return gear_value * prev
    return False

with open(fname) as f:

    for idx, row in enumerate(f):
        map[idx] = [m.start() for m in symbol.finditer(row)]

    f.seek(0)
    for idx, row in enumerate(f):
        for m in number.finditer(row):
            gear_size = int(m.group())
            sum += lookup_cogs(idx, m.start() - 1, m.end(), gear_size)

    print(sum)



