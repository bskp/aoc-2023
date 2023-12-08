#!/usr/bin/env python

import re

pattern = re.compile(r'([\w]{3})')

m = dict()
with open('input.txt', 'r') as f:
    track = f.readline().strip()
    f.readline()
    for row in f:
        p, l, r = pattern.findall(row)
        m[p] = (l, r)

    pos = 'AAA'
    steps = 0
    while pos != 'ZZZ':
        direction = track[steps % len(track)]
        print(pos, direction)
        pos = m[pos][0 if direction == 'L' else 1]
        steps += 1

    print(steps)



