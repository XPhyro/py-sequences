#!/usr/bin/env python3

import time
import datetime
import math
import input_helper as ih

n = ih.get_int_rng("How many terms of the sequence should be computed?", low=3) 

s = []

# Time is obtained twice not to interfere with the actual timing of the computation.
print(f"Initiated the computation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

log5 = math.log10(5)
for i in range(3, n):
    s.append(math.ceil(log5 / math.log10(1 + 2 / (i - 2))))

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
