#!/usr/bin/env python

import re
from math import lcm

pattern = re.compile(r'([\w]{3})')

m = dict()
with open('input.txt', 'r') as f:
    track = f.readline().strip()
    f.readline()
    positions = []
    for row in f:
        p, l, r = pattern.findall(row)
        m[p] = (l, r)
        if p.endswith('A'):
            positions += p,

    steps = 0
    hits = [[] for _ in positions]
    while not all(len(h) >= 2 for h in hits):
        dir_idx = 0 if track[steps % len(track)] == 'L' else 1
        positions = [m[pos][dir_idx] for pos in positions]
        for i, pos in enumerate(positions):
            if pos.endswith('Z'): 
                hits[i] += steps,

        steps += 1

    # Calculate phases
    phases = [h[1] - h[0] for h in hits]
    print(lcm(*phases))



