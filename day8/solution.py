#!/usr/bin/env python3

import time

data = [list(map(int, [*line])) for line in open(0).read().splitlines()]

# horizontal
horizontal = [tuple(i) for i in data]
vertical = [i for i in zip(*data)]

h = {i[0]: i[1] for i in enumerate(horizontal)}
v = {i[0]: i[1] for i in enumerate(vertical)}

seen = []
count = 0
wc = []

row = 0
for line in data:
    for i in enumerate(line):
        # (0, 3)
        # (1, 0)
        # ...
        idx_hh = i[0]
        idx_vv = row
        _v = v[idx_hh]
        _h = h[idx_vv]
        # processing _h (rows)
        left = _h[:idx_hh]
        right = _h[idx_hh+1:]
        ## processing _v (columns)
        _left = _v[:idx_vv]
        _right = _v[idx_vv+1:]

        r = []
        d = []
        l = []
        u = []
        for _e in right:
            if ((idx_hh or idx_vv) in [0, len(line)-1]):
                break
            if _e < i[1]: # does not work when [5] (4,9) 
                r.append(i[1])
            if _e >= i[1]:
                r.append(i[1])
                break
        #time.sleep(1)

        for _e in left[::-1]:
            if ((idx_hh or idx_vv) in [0, len(line)-1]):
                break
            if _e < i[1]:
                l.append(i[1])
            if _e >= i[1]:
                l.append(i[1])
                break
        #time.sleep(1)
        for _e in _right:
            if ((idx_hh or idx_vv) in [0, len(line)-1]):
                break
            if _e < i[1]:
                d.append(i[1])
            if _e >= i[1]:
                d.append(i[1])
                break
        #time.sleep(1)

        for _e in _left[::-1]:
            if ((idx_hh or idx_vv) in [0, len(line)-1]):
                break
            if _e < i[1]:
                u.append(i[1])
            if _e >= i[1]:
                u.append(i[1])
                break
        #time.sleep(1)
        wc.append(len(r) * len(l) * len(d) * len(u))
        print(idx_vv, idx_hh,":", "r","l","d","u", left, f"[{i[1]}]", right)
        print(idx_vv, idx_hh,":", len(r),len(l),len(d),len(u))
        print()

        if len(left) == 0 or len(right) == 0 or max(left) < i[1] or max(right) < i[1] or len(_left) == 0 or len(_right) == 0 or max(_left) < i[1] or max(_right) < i[1]:
            seen.append(i)

    row += 1

#print("seen", seen)
print("p1:", len(seen))
print(wc)
print("p2:", max(wc))
