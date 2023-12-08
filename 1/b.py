#!/usr/bin/env python

import re
import sys

sum = 0
pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

def parseNumberLiteral(s: str):
    if s.isdigit(): return s
    if s == 'one': return '1'
    if s == 'two': return '2'
    if s == 'three': return '3'
    if s == 'four': return '4'
    if s == 'five': return '5'
    if s == 'six': return '6'
    if s == 'seven': return '7'
    if s == 'eight': return '8'
    if s == 'nine': return '9'
    raise ValueError

with open(fname) as f:
    for row in f:
        digits = pattern.findall(row)
        sum += int(parseNumberLiteral(digits[0]) + parseNumberLiteral(digits[-1]))

print(sum)
