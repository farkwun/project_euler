import math


def get_all_squares_below(limit):
    squares = {}
    for i in range(1, limit + 1):
        squares[i] = i * i
    return squares


C_SQUARES_DICT = get_all_squares_below(1000)
C_SQUARES_LIST = [(a, b) for a, b in C_SQUARES_DICT.items()]
C_SQUARES_SET = {square for _, square in C_SQUARES_LIST}


triplet_dict = {}

for idx_a, a in enumerate(C_SQUARES_LIST):
    idx_b = idx_a + 1
    while idx_b < len(C_SQUARES_LIST):
        b = C_SQUARES_LIST[idx_b]
        sum_ = a[1] + b[1]
        if sum_ in C_SQUARES_SET:
            triplet_dict[(a, b)] = (int(math.sqrt(sum_)), sum_)
        idx_b += 1

for item, value in triplet_dict.items():
    ([a, _], [b, _]) = item
    c, _ = value
    if a + b + c == 1000:
        print(a, b, c)
        print(a * b * c)
