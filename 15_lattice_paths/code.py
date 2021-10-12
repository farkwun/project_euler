import time
import sys

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()

NUM_ROWS = 21
NUM_COLS = 21

memo = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

memo[0][0] = 1

DIRS = [(-1, 0), (0, -1)]


def get_val_from_memo(row, col):
    if row >= 0 and col >= 0 and row < NUM_ROWS and col < NUM_COLS:
        return memo[row][col]
    return 0


for row, row_list in enumerate(memo):
    for col in range(len(row_list)):
        vals = []
        for d in DIRS:
            vals.append(get_val_from_memo(row + d[0], col + d[1]))
        memo[row][col] += sum(vals)

print(memo[-1][-1])


toc = time.perf_counter()
print(toc - tic)
