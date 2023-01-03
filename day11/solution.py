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

def lcc(_m):
    lc = []
    for i in _m:
        for l in _m[i][0]:
            lc.append(l)

    return math.lcm(*lc)

count = 20
#count = 10000

nlcm = lcc(m)

while 0 < count:
    for i in m:
        for e, n in enumerate(m[i][0]):

            m[i][5] += 1 # how many times monkey inspected an item
            expr = re.sub('old', str(n), m[i][1]) # old * 19
            #worry_lvl = eval(expr) // 3  # Part 1
            worry_lvl = eval(expr) % nlcm # Part 2
            condition = (worry_lvl) % int(re.findall('[0-9]+', m[i][2])[0]) == 0
            monkey = re.findall('[0-9]+',m[i][3])[0] if condition else re.findall('[0-9]+',m[i][4])[0]
            worry_lvl = eval(expr) % nlcm
            condition = (worry_lvl) % int(re.findall('[0-9]+', m[i][2])[0]) == 0
            print(f"monkey {i}, item: {n} -> goes to {monkey}, wl {worry_lvl}")
            m[int(monkey)][0].append(worry_lvl) # pushing newly calculated worry level to a respective monkey
            #time.sleep(0.1)
        m[i][0] = [] # deleting currently processed worry item
    count -= 1

for i in m:
    print(i, m[i][0], m[i][5])

print(math.prod(sorted(([m[i][5] for i in m]))[-2:]))
print("nlcm:",nlcm)
#print(solve(monkeys, 20, floordiv, 3))  // 3
#
#// 3
#% <nejake cislo>
#
#print(solve(monkeys, 10_000, mod, lcm(*(m[TEST] for m in monkeys))))  # Use least common multiple
