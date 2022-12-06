#!/usr/bin/env python3
import argparse
import pathlib
import re

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

# items
s = []
r = []
for i in lines:
    if i != "":
        s.append([i[idx]for idx in [i+1 for i in range(0, len(i), 4)]])
    if i == "":
        break

for i in lines:
    if i.startswith("move"):
        _r = re.findall('\d+', i)
        r.append(list(map(int, _r)))

a = [list(o) for o in [i[::-1] for i in list(zip(*s))]]

t = {}
for i in a:
    t[[j for j in i if j != " "][0]] = [j for j in i if j != " "][1:]

#print(t)
#print(r)
for i in r:
    # i[0] how many to move
    # i[1] from ...
    # i[2] to ...
    # Part 1
    #t[str(i[2])] = t[str(i[2])] + t[str(i[1])][-i[0]:][::-1] # we want to append this to ...
    # Part 2
    t[str(i[2])] = t[str(i[2])] + t[str(i[1])][-i[0]:] # we want to append this to ...
    t[str(i[1])] = t[str(i[1])][:-i[0]]
    print(t)

code = ""
for i in range(1, len(t) +1):
    print(t[str(i)][-1])
    code += t[str(i)][-1] 

print(code)
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# print(a)

