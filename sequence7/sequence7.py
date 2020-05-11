#!/usr/bin/env python3


import time
import datetime
import math
import input_helper as ih


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or not n % 2:
        return False

    for i in range(3, math.trunc(math.sqrt(n)), 2):
        if not n % i:
            return False

    return True


def prime_factors(n):
    c = 0
    while not n % 2:
        n /= 2
        c += 1

    l = []
    if c:
        l.append((2, c))

    for i in range(3, math.trunc(n) + 1, 2):
        if not is_prime(i):
            continue

        c = 0
        while not n % i:
            n /= i
            c += 1
        if c:
            l.append((i, c))

    return l


n = ih.get_pint("How many terms of the sequence should be computed?")

s = [1]

# Time is obtained twice not to interfere with the actual timing of the computation.
print(f"Initiated the computation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

for i in range(2, n):
    l = prime_factors(i)
    r = False
    for j in l:
        if j[1] > 1:
            s.append(0)
            r = True
            break
    if r:
        continue

    if len(l) % 2:
        s.append(-1)
    else:
        s.append(1)

t1 = time.time()

print(
    f'Completed the computation on {datetime.datetime.fromtimestamp(t1)}.\nWriting the results to the file "sequence".'
)

s = str(s)

with open("sequence", "w+") as f:
    f.write(f"Time started\t{t0}\nTime finished\t{t1}\nTerms computed\t{n}\nSequence\t")
    for i in s:
        f.write(i)
    f.write("\n")

print("Writing completed.")
