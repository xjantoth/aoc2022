#!/usr/bin/env python3
import argparse, pathlib, string

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

l = {i: ord(i)-96 for i in string.ascii_lowercase}
u = {i: ord(i)-38 for i in string.ascii_uppercase}
l.update(u)

s, c = 0, 0
for i in lines:
  spl = len(i) // 2
  s1 = set(i[:spl])
  s2 = set(i[-spl:])
  isec = s1.intersection(s2)
  s += l[''.join(isec)]
  #print(isec, l[''.join(isec)])

print(f"part1: {s}")

for i in range(0, len(lines), 3):
  tmp_sets = [set(k) for k in lines[i:i+3]]
  c += l[''.join(tmp_sets[0].intersection(tmp_sets[1], tmp_sets[2]))]

print(f"part2: {c}")
