#!/usr/bin/env python3
from collections import deque

data = [line for line in open(0).read().splitlines()]
m = {"S": "a", "E": "z"}
# a = 97
# z = 122
# S = (0, 0)
# E = (5, 2)
E = 0 + 0j
S = 0 + 0j
co = {}

for y, d in enumerate(data):
    for x, i in enumerate(d):
        if i == "E":
            E = x + y*1j
        if i == "S":
            S = x + y*1j
        co[(x + y*1j)] = [m.get(i, i), ord(m.get(i, i))]

# "x" cannot get to nexative numbers and beyond data width
# (...,-2, -1, | 0 , 1, 2, 3, ... len(data[0]) | ...)
# if x - 1 >= 0 and x <= len(data[0]) and y - 1 >= 0 and y <= len(data) 

def dfs(grid, start, end):
    buffer = deque([(start, 0)])
    seen = set()

    while buffer:
        current = buffer.popleft()
        #print(f"processing: {current}")
        if current[0] in seen:
            continue

        # Part 1
        if current[0] == end:
            return current[1], seen, len(seen)
        # Part 2
        #if co[current[0]][0] == end:
        #    return current[1], seen, len(seen)

        seen.add(current[0])

        neighbours = [
            current[0] + (-1 + 0j),
            current[0] + (1 + 0j),
            current[0] + (0 + -1j),
            current[0] + (0 + 1j)
        ]
        for n in neighbours:
            if n.real < 0 or n.imag < 0 or n.real >= len(data[0]) or n.imag >= len(data):
                #print(n)
                continue
            if grid[n][1] <= grid[current[0]][1] + 1:
            #if grid[n][1] - grid[current[0]][1] in [1, 0]:
            #if abs(grid[n][1] - grid[current[0]][1]) in [0, 1]:
                #print(grid[n][1] - grid[current[0]][1])
                #print(n, current[1]+1)
                buffer.append((n, current[1]+1))
    return

print(S, E)
print(dfs(co, S, E)[0])
#print(dfs(co, E, "a"))

def odfs(grid, start, end):
    buffer = deque([(start, 0)])
    seen = set()

    while buffer:
        current = buffer.popleft()
        #print(f"processing: {current}")
        if current[0] in seen:
            continue

        # Part 2
        if co[current[0]][0] == end:
            return current[1], seen, len(seen)

        seen.add(current[0])

        neighbours = [
            current[0] + (-1 + 0j),
            current[0] + (1 + 0j),
            current[0] + (0 + -1j),
            current[0] + (0 + 1j)
        ]
        for n in neighbours:
            if n.real < 0 or n.imag < 0 or n.real >= len(data[0]) or n.imag >= len(data):
                continue
            if grid[n][1] + 1 >= grid[current[0]][1]:
                #print(n, current[1]+1)
                buffer.append((n, current[1]+1))
    return -1

print(odfs(co, E, "a")[0])
