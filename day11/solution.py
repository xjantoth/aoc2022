#!/usr/bin/env python3
import re
import time
import math

data = [line for line in open(0).read().splitlines()]

def processme(_tmp, _m, _c):
    _tmp = _tmp[1:]
    _tmp[0] = list(map(int, re.findall('[0-9]+', _tmp[0])))
    _tmp[1] = _tmp[1].split("=")[1].strip(' ') # re.sub(..,.) + eval()
    _tmp.append(0)
    _m[_c] = _tmp
    return _m

m = {}
c = 0
tmp = []
for i in data:
    if i != '':
        tmp.append(i.strip(' '))
    else:
        m = processme(tmp, m, c)
        c +=1
        tmp = []

m = processme(tmp, m, c)

count = 20
#count = 10000

while 0 < count:
    print(f"*********************** {count} *************************")
    for i in m:
        #print(i, m[i])
        for e, n in enumerate(m[i][0]):
            m[i][5] += 1 # how many times monkey inspected an item
            expr = re.sub('old', str(n), m[i][1])
            worry_lvl = eval(expr) // 3
            #worry_lvl = eval(expr) // math.gcd(*m[i][0])
            condition = (worry_lvl) % int(re.findall('[0-9]+', m[i][2])[0]) == 0
            monkey = re.findall('[0-9]+',m[i][3])[0] if condition else re.findall('[0-9]+',m[i][4])[0]
            #print(f"monkey {i}, item: {n} - {eval(expr)}, {eval(expr) // 3}  --> goes to m {monkey}, wl {worry_lvl}")
            #print(f"monkey {i}, item: {n} - {eval(expr)}, {eval(expr)}  --> goes to m {monkey}, wl {worry_lvl}")
            m[int(monkey)][0].append(worry_lvl) # pushing newly calculated worry level to a respective monkey
            #time.sleep(1)
        m[i][0] = [] # deleting currently processed worry item
    count -= 1

for i in m:
    print(i, m[i][0], m[i][5])

print(math.prod(sorted(([m[i][5] for i in m]))[-2:]))
