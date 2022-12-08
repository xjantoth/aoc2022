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
chdir = []
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
                tpp.append(f"{_e.split(' ')[1]}")


        chdir.append(i.split(" ")[-1])
        #print(level[-1], '/'.join(chdir[:-1]), tpp)
        couples.append([level[-1], '/'.join(chdir[:-1]), tpp])

        #  fix chdir list if there was decrement before
        if dec != 0:
            chdir = chdir[:dec - 1]
            chdir.append(i.split(" ")[-1])

        if dec != 0:
            _t = level[-1] + dec
            level.pop()
            level.append(_t)
            dec = 0

        level.append(level[-1] + 1)
        t = list() # clear up list
        tpp = list()
        #print()
    elif re.search('^.*\.\.$', i):
        dec -= 1
    elif re.search('^d|[1-9]', i):
        #print("adding:", i)
        t.append(i)
    time.sleep(0.0000005)

tpp = list()
for _e in t:
    if re.search('^[1-9]', _e):
        tpp.append(_e.split(' ')[0])
    else:
        tpp.append(f"{_e.split(' ')[1]}")

#print(level[-1], '/'.join(chdir), tpp)
couples.append([level[-1], '/'.join(chdir), tpp])
tpp = list()

# END OF LOOPING
e = sorted(couples, key=lambda x: x[0])
#o = e[::-1][:-2]
o = e[::-1][:-1]

for i in o:
    #print("before remake:", i)
    # add full paths to lists of file sizes 
    # if folder inside this list
    _t = []
    for x in i[2]:
        if re.search('^[a-z]', x):
            _t.append(f"{i[1]}/{x}")
        else:
            _t.append(x)
    i[2] = _t

# create dictionary of unique keys
spec = {f"{i[1]}": i[2] for i in o}
part1 = 0

# Must update dict named "spec" in place dude !!!

for item in o:
    # item[1] <--- key
    # item[2] <--- value (defacto list that needs to be transformed)
    #print(item[1:])
    tempo = []
    for element in item[2]:
        # if element is path istead of number
        if not re.search('^[0-9]', element):
            tempo.append(spec[element])
        else:
            tempo.append(element)
    spec[item[1]] = tempo


p1 = 0
p2 = []
total = sum([int(i) for i in re.findall('[0-9]+', str(spec['/']))])
needed = 30000000 - abs(total - 70000000)
print("total:", total, "needed:", needed)

for k,v in spec.items():
    nums = sum([int(i) for i in re.findall('[0-9]+', str(v))])
    print(nums)
    if nums < 100000:
        p1 += nums
    if nums > needed:
        p2.append(nums)
print("Part1:", p1)
print("Part2:", min(p2))




