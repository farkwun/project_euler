import time
import sys

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()

EXP = 1000

num_str = str(2 ** EXP)

sum_ = 0
for c in num_str:
    sum_ += int(c)

print(sum_)


"""
Your code goes here
"""

toc = time.perf_counter()
print(toc - tic)
