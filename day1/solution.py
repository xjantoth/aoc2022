#!/usr/bin/env python3

import argparse, pathlib

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

groupped = []

suma = 0
for cal in lines:
    if isinstance(cal, str) and cal != '':
      suma += int(cal)
    else:
      # print(suma)
      groupped.append(suma)
      suma = 0

groupped.append(suma)

sorting = sorted(groupped, reverse=True)[0:3]

print(f'First part: max callories: {max(groupped)}')
print(f'Second part: max 3 El. callories: {sum(sorting)}')



