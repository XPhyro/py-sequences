#!/usr/bin/env python3

import time
import datetime
import math
import scipy.special as sp
import input_helper as ih

n = ih.get_pint("How many terms of the sequence should be computed?") 

s = []
# adapted from: https://codegolf.stackexchange.com/q/69993
m = lambda n: 1 / n - sum(m(k) for k in range(1, n) if n % k < 1)

# Time is obtained twice not to interfere with the actual timing of the computation.
print(f"Initiated the computation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

for i in range(3, n):
    a = 0
    for j in range(2, i + 1):
        a += sp.binom(abs(m(j)), abs(m(math.floor(j / 2))))
        # a += sp.comb(abs(m(j)), abs(m(math.floor(j / 2))), exact=True)
    s.append(int(a))

t1 = time.time()

print(f"Completed the computation on {datetime.datetime.fromtimestamp(t1)}.\nWriting the results to the file \"sequence\".")

s = str(s)

with open("sequence", "w+") as f:
    f.write(f"Time started\t{t0}\nTime finished\t{t1}\nTerms computed\t{n}\nSequence\t")
    for i in s:
        f.write(i)
    f.write("\n")
    f.close()

print("Writing completed.")
