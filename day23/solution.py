#!/usr/bin/env python3
#import re
#from sympy import symbols, solve

data = [line for line in open(0).read().splitlines()]

# a = <0, len(data)>
# b = 

#     row  col      
# n = (a,  b)  -> (a-1 + b), (a-1, b-1), (a-1, b+1) 
# s = (a,  b)  -> (a+1 + b), (a+1, b-1), (a+1, b+1)
# w = (a,  b)  -> (a + b-1), (a-1, b-1), (a+1, b-1)
# e = (a,  b)  -> (a + b+1), (a-1, b+1), (a+1, b+1)

elves = {}
for a, i in enumerate(data):
    print(i)
    for b, el in enumerate(i):
        if el == '#':
            elves[(a, b)] = 1
print(elves)



