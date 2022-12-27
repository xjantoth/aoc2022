#!/usr/bin/env python3
import math
import time

data = [int(line) for line in open(0).read().splitlines()]
#print(data)

real = 0
c = 0
print(f"{'real': >5} {'c': >5} {'data[c]': >8}", data)
while c < 7:
    # c = 0                    # => original index 
    new_idx = c + data[c]    # => new index 1 
    p_value = data[c]        # => original value 1
    n_value = data[new_idx]  # => next value 2

    tmp = data

    tmp[new_idx] = p_value
    tmp[c] = n_value
    print(f"{real: >5} {c: >5} {data[c]: >8}", tmp)
    data = tmp
    c +=1
    if c == 7:
        print("-"*22)
        print(f"{'real': >5} {'c': >5} {'data[c]': >8}")
        c = 0
    time.sleep(1)
    real += 1

#for e,i in enumerate(data): 
#    print(e,i)
