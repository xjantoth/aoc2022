#!/usr/bin/env python3

# Rock defeats Scissors,
# Scissors defeats Paper
# Paper defeats Rock.

import argparse, pathlib

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

score = { "RS": [0, -1], "SR": [6, 1], "SP": [0, -1], "PS": [6,  1], "PR": [0,-1], "RP": [6, 1] }
weigth = { "R" : 1, "P" : 2, "S" : 3, }

me = { "X" : ["R", -1, 0], "Y" : ["P", 0, 3], "Z" : ["S", 1, 6]}
you = { "A" : "R", "B" : "P", "C" : "S", }

print("part1: ", sum([score.get(f"{you[i.split(' ')[0]]}{me[i.split(' ')[1]][0]}", [3, 0])[0] + weigth[f"{you[i.split(' ')[0]]}{me[i.split(' ')[1]][0]}"[-1]] for i in lines]))


part2 = 0

for i in lines:
    #print("you: ", you[i.split(' ')[0]], "me: ", me[i.split(' ')[1]][1])
    _state = dict(filter(lambda s: s[1][1] == me[i.split(' ')[1]][1], score.items()))
    _eq = dict(filter(lambda s: s[0][0] == you[i.split(' ')[0]], _state.items()))
    if len(_eq) == 1:
        _eq = list(_eq.keys())[0][1]
    else:
        _eq = you[i.split(' ')[0]]

    part2 += (me[i.split(' ')[1]][2] + weigth[_eq])


print(f"part2: {part2}")
