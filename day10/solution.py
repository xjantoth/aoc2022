#!/usr/bin/env python3
import math
import re

data = [line for line in open(0).read().splitlines()]
p = {}
X = 1 # register
cycle = 0

for e, instruction in enumerate(data[:]):
    if re.search('^a', instruction):
        t = instruction.split(' ')[0]
        inc = int(instruction.split(' ')[1])
        # increment 2 cycles
        cycle += 1
        p[cycle] = [X * cycle, t, inc, X]
        cycle += 1
        p[cycle] = [X * cycle, t, inc, X]
        X += inc
    else:
        t = "noop"
        inc = "_"
        cycle += 1
        p[cycle] = [X * cycle, t, inc, X]
    print("X:", X)

print()
for i in p[20], p[60],p[100], p[140], p[180], p[220]:
    print(i)
print(p[20][0] + p[60][0] + p[100][0] + p[140][0] + p[180][0] + p[220][0])



#for k,v in p.items():
#    print(k, v)

