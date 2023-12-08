#!/usr/bin/env python

import re
from mmap import mmap

def parse_to_reverse_map(rows: [str]):
    spans = []

    for row in rows:
        dest, source, size = row.split(b' ')
        spans += (range(int(dest), int(dest) + int(size)), int(source) - int(dest)),

    def map(i):
        for span, offset in spans: 
            if i in span:
                return i + offset
        return i  # not in spans -> identity function
    return map

map_pattern = re.compile(rb'([a-z]+)-to-([a-z]+) map:\n([\s\d]*)')
seed_pair = re.compile(r'(\d+) (\d+)')
maps = []

with open('input.txt', 'r+') as f:
    seeds_ranges = [range(int(start), int(start) + int(length)) for start, length in seed_pair.findall(f.readline())]
    data = mmap(f.fileno(), 0)
    for i, (target, source, block) in enumerate(map_pattern.findall(data)):
        label = f'{source.decode()} to {target.decode()}'
        maps += (label, parse_to_reverse_map(block.strip().split(b'\n'))),

    for location in range(9999999999):
        #print(location, end=' -> ')
        code = location
        for label, m in reversed(maps):
            code = m(code)
        #print(code)
        if any(map(lambda r: code in r, seeds_ranges)):
            break
    print(location)




'''
seed
soil
fertilizer
water
light
temperature
humidity
location
'''