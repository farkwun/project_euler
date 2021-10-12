import time
import sys
import math

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()


def get_divisors(n):
    divisor_set = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if i in divisor_set:
            continue
        if n % i == 0:
            divisor_set.add(i)
            divisor_set.add(n // i)
    return divisor_set


triangle = 1
n = 1
while True:
    if triangle > 1000000:
        divisors = get_divisors(triangle)
        print(triangle, len(divisors))
        if len(get_divisors(triangle)) > 500:
            print("Answer: ", triangle)
            break
    n += 1
    triangle += n


toc = time.perf_counter()
print(toc - tic)
