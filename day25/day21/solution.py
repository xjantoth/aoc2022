#!/usr/bin/env python3
import re
from sympy import symbols, solve

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '=': lambda x, y: x == y,
      }

data = [line for line in open(0).read().splitlines()]
d = {row.split(':')[0]: int(row.split(':')[1])
     for row in data if re.search('^[0-9]', row.split(':')[1].strip(' '))}


_len = [0]
unprocessed = {}
while True:
    for row in data:
        k, v = row.split(':')
        if re.search('^[a-z]', v.strip(' ')):
            u = v.strip(' ').split(' ')
            # u[0] -> first monkey
            # u[1] -> math operation
            # u[2] -> second monkey
            f, s = d.get(u[0], False), d.get(u[2], False)
            if f and s:
                d[k] = op[u[1]](f, s)
            else:
                unprocessed[k] = v
                #print(f"{f} {u[1]} {s}")

    # print(d, len(d))
    #time.sleep(1)
    _len.append(len(d))
    if _len[-1] == _len[-2]:
        print('cannot proceed anymore',_len[-1], _len[-2])
        #for _k, _v in  unprocessed.items():
            #print(_k, _v)
        break

    if len(d) == len(data):
        #print("root", [i for i in data if i.split(':')[0] == 'root'])
        print("p1:", d['root'])
        break


print("d:", len(d))
print("unprocessed:", len(unprocessed))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Part 2
# deleted "humn: key" to process second part (must Download an original input.txt if calculating Part1)
# changed to "=" sign at "root: key"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print("Starting calculating solution part 2 ...")

root = [i for i in data if i.split(':')[0] == 'root']
a, b = root[0].split(':')[1].strip(' ').split(' = ')

uncover = unprocessed
plain = d

del uncover['root'] # root not needed!

def calculate_expr(_paceholder):
    cc = 0
    placeholder = _paceholder
    l = []
    while True:
        f = uncover.get(placeholder, False)                # cczh / lfqf
        if not f:
            print(">>> --- >>> Must get here - stop searching ...:", placeholder)
            break
        s = f.split(' ')                            # ["cczh", "/", "lfqf"]
        t = list(map(str, list(map(lambda x: plain.get(x, x), s)))) # ["cczh", "/", 4]
        try:
            p = list(filter(lambda s: re.match('^[a-z]', s), t))[0]
            cc +=1
        except:
            #print("I am in except block:", s, t)
            l.append((t, False))
            break
        #print(t, p)
        placeholder = p
        l.append((t, p))
        #time.sleep(0.2)

    couples = {}
    for e, i in enumerate(l):
        if e == len(l)-1:
            break
        couples[l[e][1]] = l[e+1][0]
    #print(couples)

    ladj = [i[0] for i in l]

    ini = ' '.join(ladj[0]) # ['cczh', '/', '4'] cczh
    e = 0
    while True:
        if e == len(l)-1:
            break
        p = re.findall('[a-z]+', ini)[0]# p = cczh
        ini = re.sub('[a-z]+', f"({' '.join(couples[p])})", ini)
        e +=1
        #time.sleep(0.2)

    return ini, cc, l

ls, ls_c, ls_l= calculate_expr(a)
rs, rs_c, rs_l = calculate_expr(b)

humn = symbols('humn')
expr = f"{ls} - ({rs})"
print("part2:", solve(expr))
print(ls_c, rs_c, len(plain), len(uncover))

#print(ls_l)
