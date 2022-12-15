#!/usr/bin/env python3
import math

data = [line for line in open(0).read().splitlines()]
#print(data)
s = (0 + 0j)
tail_pos = [s]

for e,i in enumerate(data[:]):
    direction = i.split(' ')[0]   # R
    move = int(i.split(' ')[1])   # 4
    print()
    print("*********",e,"->", i, "**********")
    if direction in ["R"]:
        head = s + 1
        tail = tail_pos[-1]
        c = head.real
        print(c, head, tail)
        for i in range(int(c),int(c) + int(move)):
            head = i + 1j*s.imag
            if abs(head - tail) > math.sqrt(1**2 + 1**2):
                tail = head - 1
                tail_pos.append(tail)
            print(f"moving ... {tail} -> {head}")
        print(f"t:{tail} --> h: {head}")
        s = head

    if direction in ["L"]:
        head = s - 1 # 3 + 4j
        tail = tail_pos[-1]
        c = head.real
        print(c, head, tail)
        for i in range(int(c),int(c-move),-1):
            head = i + 1j*s.imag
            if abs(head - tail) > math.sqrt(1**2 + 1**2):
                tail = head + 1
                tail_pos.append(tail)
            print(f"moving c: {c}... {tail} -> {head}")
        print(f"t:{tail} --> h: {head}")
        s = head

    if direction in ["U"]:

        head = s + 1j# (4 +0j)
        tail = tail_pos[-1]
        c = head.imag # 4 + 0j   --> 0
        print(c, head, tail)
        # previous head: -1 -1j
        #  current head: -1 + 0j
        #current head c:      0
        #        range(int(0), int(2))
        for i in range(int(c),int(c+move)):
            # i = 0j; s = -1 -1j
            # i = 1j; s = -1 -1j
            # -------------------
            # 
            head = i*1j + s.real
            if abs(head - tail) > math.sqrt(1**2 + 1**2):
                #tail = c*1j + s - 1
                tail = head - 1j
                tail_pos.append(tail)
            print(f"moving ... {tail} -> {head}")
        print(f"t:{tail} --> h: {head}")
        s = head

    if direction in ["D"]:
        head = s - 1j# (4 +0j)
        tail = tail_pos[-1]
        c = head.imag # 4 + 0j   --> 0
        print(c, head, tail)
        for i in range(int(c),int(c-move),-1):
            head = i*1j + s.real # (4 +1j) - (3+0j)
            if abs(head - tail) > math.sqrt(1**2 + 1**2):
                #tail = c*1j + s - 1
                tail = head + 1j
                tail_pos.append(tail)
            print(f"moving ...{c} {tail} -> {head}")
        print(f"t:{tail} --> h: {head}")
        s = head

print()
print(f"tail poditions: {tail_pos}")
print(f"p1: {len(set(tail_pos))}")

