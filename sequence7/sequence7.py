#!/usr/bin/env python3


import time
import datetime
import math
import input_helper as ih
import num_helper as nh


n = ih.get_pint("How many terms of the sequence should be computed?")

s = [1]

# Time is obtained twice not to interfere with the actual timing of the computation.
print(f"Initiated the computation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

for i in range(2, n + 1):
    l = nh.prime_factors(i)
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
