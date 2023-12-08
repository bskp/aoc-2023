#!/usr/bin/env python

import re
import sys

sum = 0
pattern = re.compile(r'\d')

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'input.txt'

with open(fname) as f:
    for row in f:
        digits = pattern.findall(row)
        sum += int(digits[0] + digits[-1])

print(sum)
