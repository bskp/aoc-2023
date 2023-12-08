#!/usr/bin/env python

import re
from mmap import mmap

def parse_to_map(rows: [str]):
    # A map is made up by a set of input ranges, called "spans", which refer
    # to an "offset" used for output calculation 
    spans = []

    for row in rows:
        dest, source, size = row.split(b' ')
        spans += (range(int(source), int(source) + int(size)), int(dest) - int(source)),

    def map(i):
        for span, offset in spans: 
            if i in span:
                return i + offset
        return i  # not in spans -> identity function
    return map

map_pattern = re.compile(rb'([a-z]+)-to-([a-z]+) map:\n([\s\d]*)')
maps = []

with open('input.txt', 'r+') as f:
    seeds = [int(s) for s in f.readline().rpartition(':')[2].strip().split(' ')]
    data = mmap(f.fileno(), 0)
    for i, (source, target, block) in enumerate(map_pattern.findall(data)):
        label = f'{source.decode()} to {target.decode()}'
        maps += (label, parse_to_map(block.strip().split(b'\n'))),

    locations = []
    for seed in seeds:
        print(seed, end=' -> ')
        code = seed
        for label, m in maps:
            code = m(code)
        print(code)
        locations += code,

    print(min(locations))


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