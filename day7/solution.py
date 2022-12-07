#!/usr/bin/env python3
import argparse
import pathlib
import re, time

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with open(args.file) as f:
    lines = [line.rstrip('\n') for line in f]

#coll = {} # {"0/": ["dir a", "14848514 b.txt", ...], "1a": [...]}

level = [-1]
t = list()
chdir = ["/"]
dec = 0

couples = []
for i in lines:
    if i.split(" ")[-2] == "cd" and i.split(" ")[-1] != "..":
        #print(level[-1], chdir[-1], t)
        tpp = list()
        for _e in t:
            if re.search('^[1-9]', _e):
                tpp.append(_e.split(' ')[0])
            else:
                tpp.append(f"{level[-1]+1}{_e.split(' ')[1]}")

        couples.append([level[-1], chdir[-1], tpp])
        # below the magic had to be done when it comes to decrementing
        if dec != 0:
            _t = level[-1] + dec
            level.pop()
            level.append(_t)
            dec = 0
        level.append(level[-1] + 1)
        chdir.append(i.split(" ")[-1])
        t = list() # clear up list
        tpp = list()
    elif re.search('^.*\.\.$', i):
        dec -= 1
    elif re.search('^d|[1-9]', i):
        t.append(i)
    time.sleep(0.0002)

#print(level[-1], chdir[-1], t)

tpp = list()
for _e in t:
    if re.search('^[1-9]', _e):
        tpp.append(_e.split(' ')[0])
    else:
        tpp.append(f"{level[-1]+1}{_e.split(' ')[1]}")
couples.append([level[-1], chdir[-1], tpp])
tpp = list()


# ....................

e = sorted(couples, key=lambda x: x[0])
o = e[::-1][:-2]

# create dictionary of unique keys
spec = {f"{i[0]}{i[1]}": i[2] for i in o}

print(o)
print(spec)

def convertme(_list, _dict):
   tmp = []
   for i in _list:
       try:
           tmp.append(_dict[i][0])
       except:
           tmp.append(i)
   return tmp

part1 = 0

for i in o:
    #print(spec[f"{i[0]}{i[1]}"])
    x = convertme(spec[f"{i[0]}{i[1]}"] ,spec)
    s = sum([int(i) for i in x])
    # print(f"{i[:2]}", s)
    if s < 100000:
        print(f"{i[:2]}", s)
        part1 +=s

print(f"Part 1: {part1}")

