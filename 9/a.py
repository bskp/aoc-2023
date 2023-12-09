#!/usr/bin/env python

def extrapolate(values: [int]):
    diff = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    if all([d == 0 for d in diff]):
        return values[0]
    return values[-1] + extrapolate(diff)

sum = 0
with open('input.txt', 'r') as f:
    for row in f:
        values = [int(v) for v in row.split(' ')]
        extra = extrapolate(values)
        print(extra)
        sum += extra

print('Sum', sum)
