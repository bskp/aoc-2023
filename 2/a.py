#!/usr/bin/env python

import sys
import re

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

color_pattern = re.compile(r'(\d+) (red|green|blue)')

max_red = 12
max_green = 13
max_blue = 14

def validate_draw(draw: str):
    for count, color in color_pattern.findall(draw):
        c = int(count)
        if color == 'red' and c > max_red: return False
        if color == 'green' and c > max_green: return False
        if color == 'blue' and c > max_blue: return False

    return True

sum = 0

def validate_game(game_draws: str):
    for draw in game_draws.split(';'):
        if not validate_draw(draw): return False

    return True


with open(fname) as f:
    for game in f:
        game_str, _, draws = game.partition(':')
        game_nr = int(game_str.rpartition(' ')[2])

        if validate_game(draws):
            sum += game_nr

print(sum)