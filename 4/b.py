#!/usr/bin/env python

import sys
import re
from functools import cache

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = './input.txt'

number = re.compile(r'(\d+)')


winners_by_card = dict()

with open(fname) as f:
    for idx, row in enumerate(f, 1):
        l, _, r = row.partition(':')[2].partition('|')

        winning = {int(n) for n in number.findall(r)}
        mine = {int(n) for n in number.findall(l)}
        n = len(mine.intersection(winning))

        winners_by_card[idx] = range(idx + 1, idx + n + 1)

    @cache
    def card_score(nr: int):
        score = 1 + sum([card_score(n) for n in winners_by_card[nr]])
        print(nr, " gives ", score)
        return score

    total = sum(card_score(n) for n in winners_by_card.keys())
    print(total)






