#!/usr/bin/env python

import sys
import re

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

color_pattern = re.compile(r'(\d+) (red|green|blue)')

sum = 0

with open(fname) as f:
    for game in f:
        game_str, _, draws = game.partition(':')
        game_nr = int(game_str.rpartition(' ')[2])

        min_red = 0
        min_green = 0
        min_blue = 0

        for draw in draws.split(';'):
            for count, color in color_pattern.findall(draw):
                c = int(count)
                if color == 'red': min_red = max(min_red, c)
                if color == 'green': min_green = max(min_green, c)
                if color == 'blue': min_blue = max(min_blue, c)

        sum += min_red*min_green*min_blue


print(sum)