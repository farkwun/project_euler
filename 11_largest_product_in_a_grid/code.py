import time
import sys

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()


def load_grid(filename):
    f = open(filename, "r")
    grid = []
    for line in f:
        line_arr = line.split()
        grid.append([int(num) for num in line_arr])
    return grid


GRID = load_grid("11_largest_product_in_a_grid/grid.txt")

DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]

NUM_STEPS = 4


def get_directional_product(point, direction):
    def should_traverse(point):
        r, c = point
        return r >= 0 and c >= 0 and r < len(GRID) and c < len(GRID[0])

    def traverse(steps_left, point):
        r, c = point
        num = GRID[r][c]
        if steps_left == 0:
            return num
        d = direction
        new_point = (r + d[0], c + d[1])
        if should_traverse(new_point):
            return num * traverse(steps_left - 1, new_point)
        return 0

    return traverse(NUM_STEPS - 1, point)


largest_prod = float("-inf")

for row, row_arr in enumerate(GRID):
    for col in range(len(row_arr)):
        for d in DIRS:
            prod = get_directional_product((row, col), d)
            if prod > largest_prod:
                largest_prod = prod

print(largest_prod)


toc = time.perf_counter()
print(toc - tic)
