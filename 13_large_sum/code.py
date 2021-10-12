import time
import sys

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()


f = open("13_large_sum/num_list.txt", "r")

sum_ = 0

for line in f:
    sum_ += int(line)

print(str(sum_)[:10])
"""
Your code goes here
"""

toc = time.perf_counter()
print(toc - tic)
