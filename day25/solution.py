#!/usr/bin/env python3
import time

data = [line for line in open(0).read().splitlines()]
op = {"=": -2, "-": -1}
oop = {"-2": "=", "-1": "-"}

s = 0
for i in data:
    for x in zip([e for e in i], [5**x for x in range(len(i))][::-1]):
        #print(x, int(op.get(x[0], x[0]))* x[1])
        s += int(op.get(x[0], x[0]))* x[1]
    print()
print("target number:", s)


p = 0
highest = 0
while True:
    if 5**p < s:
        pass
    else:
        _min = 5**(p-1)
        _max = 5**p
        highest = (_min, p-1) if abs(_min - s) < abs(_max -s) else (_max, p)
        #highest = (5**p, 5**(p-1))
        break
    time.sleep(0.1)
    p +=1

print("highest:", highest)

#highest = 0
#while True:
#    print([*range(5**p, 5**(p+1)+1)])
#    if s in [*range(5**p, 5**(p+1)+1)]:
#        _min = 5**p
#        _max = 5**(p+1)+1
#        highest = (_min, p) if abs(_min - s) < abs(_max -s) else (_max, p+1)
#        # returns number, power 
#        # e.g if power 5, then SNAUF will definitelly have 6 places
#        # 5, 4, 3, 2, 1, 0
#        # each number can be multiplied by 
#        # one of [-2, -1, 0, 1, 2] in order to get number s = 4890 (for sample.txt)
#        print(highest)
#        break
#    #time.sleep(0.1)
#    p +=1
#
x = [-2, -1, 0, 1, 2] # these are possible weights
start = [(abs(((5**highest[1]) * e) - s) , e) for e in x]
s_point = min(start, key=lambda tup: tup[0])
print("first SNAUF character", s_point, highest)

p1 = str(s_point[1])
init = s_point[1] * highest[0] # 2 * 3125 = 6250 
for i in [*range(highest[1] - 1, -1, -1)]:
    #print(5**i, min([(((5**i) * e) + init, e) for e in x], key=lambda tup: tup[0]))
    t = min([(abs(((5**i) * e) + init - s), e) for e in x], key=lambda tup: tup[0])
    print(5**i, t)
    p1 += oop.get(str(t[1]), str(t[1]))
    init = init + (t[1] * 5**i)
    #print(5**i, [(abs(((5**i) * e) - s) , e) for e in x])
print("p1:", p1)
# 2=-1=0


