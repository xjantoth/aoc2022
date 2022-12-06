#!/usr/bin/env python3
import argparse
import pathlib
import re

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]


a = 14
a = 4

for l in lines:
    for x in range(0, len(l)):
        if len(set(l[x:x+a])) == a:
            print(x+a)
            break

