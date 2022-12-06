#!/usr/bin/env python3

# Rock defeats Scissors,
# Scissors defeats Paper
# Paper defeats Rock.

import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

p1 = 0
p2 = 0
for i in lines:
    a = (i.split(',')[0].replace('-', ','))
    b = i.split(',')[1].replace('-', ',')
    aa = {_i for _i in range(int(a.split(',')[0]), int(a.split(',')[1]) + 1)}
    bb = {_i for _i in range(int(b.split(',')[0]), int(b.split(',')[1]) + 1)}
    inter = aa.intersection(bb)
    print(inter)
    if len(inter) != 0:
        p2 += 1
    if inter == aa or inter == bb:
        p1 += 1

print(p1)
print(p2)
