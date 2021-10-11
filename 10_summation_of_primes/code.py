import time
import sys

sys.path.append(".")
from utils.prime_utils import load_primes  # noqa: E402


tic = time.perf_counter()

primes = load_primes("10_summation_of_primes/primes.txt")


temp_idx = 0

while primes[temp_idx] < 2000000:
    temp_idx += 1

primes = primes[:temp_idx]


toc = time.perf_counter()
print(sum(primes))
print(toc - tic)
